from django.shortcuts import render,get_object_or_404
from django.views.generic.base import View
from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.edit import CreateView
from django.http import Http404
# Create your views here.

from .models import Prints
from .forms import PrintForm

class updatepr(View):
    def get(self, request, id):
        printers = get_object_or_404(Prints, id=id)
        return render(request, 'updatepr.html', {'printers':printers})


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
