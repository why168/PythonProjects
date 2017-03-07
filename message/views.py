from django.shortcuts import render
import MySQLdb

from models import UserMessage


# Create your views here.

def getform(request):
    all_messages = UserMessage.objects.all()

    print 'all = ', all_messages.__doc__

    print '\n'

    for message in all_messages:
        print message.name

    return render(request, 'message_form.html')
