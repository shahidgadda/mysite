import simplejson as json
from django.http import HttpResponse, HttpResponseRedirect
from haystack.query import SearchQuerySet
from django.core.mail import send_mail
from .forms import contactForm

''' Autocompletes the search based on Query '''
def autocomplete(request):
    sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get('q', ''))[:5]
    suggestions = [result.title for result in sqs]
    # Make sure you return a JSON object, not a bare list.
    # Otherwise, you could be vulnerable to an XSS attack.
    the_data = json.dumps({
        'results': suggestions
    })
    return HttpResponse(the_data, content_type='application/json')

''' Sends mail to owner ''' 
def sendMail(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['email']
            recipients = ['ayoub@trialx.com']
            send_mail(name, message, sender, recipients)
            return HttpResponseRedirect('/thanks/')
    else:
   	    return HttpResponseRedirect('/invalid/')


