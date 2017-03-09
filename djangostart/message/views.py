# -*- coding: utf-8 -*-

import MySQLdb
import json

from django.shortcuts import render
from models import UserMessage


# Create your views here.

def getform(request):
    message = None
    all_messages = UserMessage.objects.all().filter(address='北京')
    if all_messages:
        message = all_messages[0]

    # all_messages.delete()

    # for message in all_messages:
    #     message.delete()
    #     print message.__str__()

    # 表单提交
    # if request.method == 'POST':
    #     name = request.POST.get('name', "")
    #     message = request.POST.get('message', "")
    #     address = request.POST.get('address', "")
    #     email = request.POST.get('email', "")
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.message = message
    #     user_message.address = address
    #     user_message.email = email
    #     user_message.object_id = "3"
    #     user_message.save()


    print message.object_id
    print message.name
    print message.message
    print message.address
    print message.email

    # return render(request, 'message_form.html')
    return render(request, 'message_form.html', {
        'my_message': message
    })
