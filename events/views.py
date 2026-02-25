
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Event, Participant, Category  
from django.db.models import Count
from django.db.models import Q
from django.utils import timezone
from django.db.models import Sum
from django.shortcuts import redirect
from .forms import EventForm, ParticipantForm, CategoryForm

def event_list(request):

    events = Event.objects.select_related('category') \
                          .prefetch_related('participants') \
                          .annotate(participant_count=Count('participants'))

    # SEARCH
    search_query = request.GET.get('search')
    if search_query:
        events = events.filter(
            Q(name__icontains=search_query) |
            Q(location__icontains=search_query)
        )

    # FILTER BY CATEGORY
    category_id = request.GET.get('category')
    if category_id:
        events = events.filter(category_id=category_id)

    # FILTER BY DATE RANGE
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        events = events.filter(date__range=[start_date, end_date])

    categories = Category.objects.all()

    context = {
        'events': events,
        'categories': categories
    }

    return render(request, 'events/event_list.html', context)

def event_detail(request, pk):
    event = Event.objects.select_related('category') \
                         .prefetch_related('participants') \
                         .get(pk=pk)

    return render(request, 'events/event_detail.html', {'event': event})



def dashboard(request):
    today = timezone.now().date()

    total_events = Event.objects.count()
    total_participants = Participant.objects.count()

    upcoming_events = Event.objects.filter(date__gt=today)
    past_events = Event.objects.filter(date__lt=today)
    today_events = Event.objects.filter(date=today)

    filter_type = request.GET.get('filter')

    if filter_type == 'upcoming':
        events = upcoming_events
    elif filter_type == 'past':
        events = past_events
    else:
        events = today_events

    context = {
        'total_events': total_events,
        'total_participants': total_participants,
        'upcoming_count': upcoming_events.count(),
        'past_count': past_events.count(),
        'events': events,
    }

    return render(request, 'events/dashboard.html', context)
# EVENT CRUD
def event_create(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('event_list')
    return render(request, 'events/form.html', {'form': form, 'title': 'Add Event'})

def event_update(request, pk):
    event = Event.objects.get(pk=pk)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('event_list')
    return render(request, 'events/form.html', {'form': form, 'title': 'Edit Event'})

def event_delete(request, pk):
    event = Event.objects.get(pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'events/confirm_delete.html', {'object': event, 'title': 'Delete Event'})

# PARTICIPANT CRUD
def participant_create(request):
    form = ParticipantForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('event_list')
    return render(request, 'events/form.html', {'form': form, 'title': 'Add Participant'})

def participant_update(request, pk):
    participant = Participant.objects.get(pk=pk)
    form = ParticipantForm(request.POST or None, instance=participant)
    if form.is_valid():
        form.save()
        return redirect('event_list')
    return render(request, 'events/form.html', {'form': form, 'title': 'Edit Participant'})

def participant_delete(request, pk):
    participant = Participant.objects.get(pk=pk)
    if request.method == 'POST':
        participant.delete()
        return redirect('event_list')
    return render(request, 'events/confirm_delete.html', {'object': participant, 'title': 'Delete Participant'})

# CATEGORY CRUD
def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('event_list')
    return render(request, 'events/form.html', {'form': form, 'title': 'Add Category'})

def category_update(request, pk):
    category = Category.objects.get(pk=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('event_list')
    return render(request, 'events/form.html', {'form': form, 'title': 'Edit Category'})

def category_delete(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('event_list')
    return render(request, 'events/confirm_delete.html', {'object': category, 'title': 'Delete Category'})

def participant_list(request):
    participants = Participant.objects.all()
    return render(request, 'events/participant_list.html', {'participants': participants})