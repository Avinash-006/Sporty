from django.shortcuts import render
from .models import Event

def event_list(request):
    events = Event.objects.all() # Fetch all events from the database
    return render(request, 'SportEventapp/Ehome.html', {'events': events})


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EventForm

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event created successfully!')
            return redirect('Events')  # You can redirect to a list view or event detail page
    else:
        form = EventForm()

    return render(request, 'Userauthapp/create_event.html', {'form': form})


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Event


# Delete event view
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':  # If form is submitted (post method)
        event.delete()  # Delete the event from the database
        messages.success(request, 'Event deleted successfully!')
        return redirect('event_list')  # Redirect to the event list after deletion

    return render(request, 'delete_event_confirm.html', {'event': event})

from django.urls import reverse_lazy
from django.views.generic import DeleteView
from .models import Event

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'SportEventapp/delete_event_confirm.html'
    success_url = reverse_lazy('Events')


from django.shortcuts import render
from .models import Event  # Assuming you have an Event model

def events(request):
    query = request.GET.get('search', '')
    events = Event.objects.filter(name__icontains=query)
    return render(request, 'events.html', {'events': events, 'query': query})
