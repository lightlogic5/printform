from django.shortcuts import render,get_object_or_404
from django.views.generic.base import View
from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.edit import CreateView
from django.http import Http404
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

from .models import Prints
from .forms import PrintForm


# 更新打印机信息
class updatepr(UpdateView):
    model = Prints
    template_name = 'form.html'
    form_class = PrintForm

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.user != self.request.user:
            raise Http404()
        return obj


# 创建打印机信息
class PrintCreate(CreateView):
    model = Prints
    template_name = 'form.html'
    form_class = PrintForm

    # Associate form.instance.user with self.request.user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# class delpr(UpdateView):
#     model = Prints
#     success_url = reverse_lazy('users:employee')
#     fields = []
#
#     def get_object(self, queryset=None):
#         obj = super().get_object(queryset=queryset)
#         if obj.user != self.request.user:
#             raise Http404()
#         return obj
#
#     def form_valid(self, form):
#         form.instance.state = 2
#         return super().form_valid(form)

class delpr(View):
    def get(self, request, pk):
        print1 = Prints.objects.get(id=pk)
        print1.state = 2
        print1.save()
        aa = request.user
        printers = aa.user_printer.filter(user=aa, state=1)
        return render(request, "employee.html",{'printers':printers})
