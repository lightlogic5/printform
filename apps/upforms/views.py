from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.http import Http404
from django.views.generic.base import View
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import MyPrintForm


@method_decorator(login_required, name='dispatch')
class UpFormView(View):
    def get(self, request):
        user = request.user
        return render(request, "uploadform.html", {'user': user})

    def post(self, request):
        user = request.user
        print_form = MyPrintForm(request.POST)
        if print_form.is_valid():
            # prints = request.prints
            prints = request.POST.get('prints', "")
            print_form1 = print_form.save(commit=False)
            print_form1.pub_date = timezone.now()
            print_form1.repair_man = user
            print_form1.prints = prints
            print_form1.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"添加出错"}', content_type='application/json')