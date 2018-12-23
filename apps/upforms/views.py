from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.http import Http404
from django.views.generic.base import View
from django.utils import timezone


from .forms import MyPrintForm


class FormView(View):
    def get(self, request):
        return render(request, "uploadform.html", {})

    def post(self, request):
        user = request.user
        print_form = MyPrintForm(request.POST)
        if print_form.is_valid():
            # print(print_form.cleaned_data)
            print_form1 = print_form.save(commit=False)
            print_form1.pub_date = timezone.now()
            print_form1.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"添加出错"}', content_type='application/json')