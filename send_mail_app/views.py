from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView

from send_mail_app.forms import ContactFormEmail
from .tasks import test_func
import re

def test(request):
    test_func.delay()
    return HttpResponse("Done")


def sendemail(request):
    if request.method == 'GET':
        form = ContactFormEmail()
    else:
        form = ContactFormEmail(request.POST)
        if form.is_valid():
            iemails = []
            vemails=[]
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            users = form.cleaned_data['email'].split(",")
            print(users)
            for user in users:
                print(user)
                if (re.fullmatch(regex, user)):
                    print(user, "is Valid Email")
                    vemails.append(user)
                else:
                    print(user, "is Invalid Email")
                    iemails.append(user)
            context = {
                'invalidemails': iemails
            }
            print(context)
            form.send_email()
            # if len(vemails)==0:
            #     return render(request, 'send_mail/invalid_emails.html', {'vemails': vemails})

            if len(iemails) >= 1 :
                print(iemails)
                return render(request, 'send_mail/invalid_emails.html', {'invalidemails': iemails, 'vemails':vemails})
            return HttpResponse("thanks for sending email")
    return render(request, 'send_mail/contact.html', {'form': form})



# class SendEmail(FormView, TemplateView):
#     template_name = "send_mail/contact.html"
#     form_class = ContactFormEmail
#
#     def form_valid(self, form):
#         iemails = []
#         regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#         users = form.cleaned_data['email'].split(",")
#         print(users)
#         for user in users:
#             print(user)
#             if (re.fullmatch(regex, user)):
#                 print(user, "is Valid Email")
#             else:
#                 print(user, "is Invalid Email")
#                 iemails.append(user)
#         context = {
#             'invalidemails': iemails
#         }
#         print(context)
#         form.send_email()
#
#         if len(iemails) >= 1 :
#             print(iemails)
#             # return HttpResponse(iemails, "invalid email")
#             return redirect('invalidemails')
#             # return render(request, 'send_mail/invalid_emails.html', context)
#         return HttpResponse("thanks for sending email")
#
