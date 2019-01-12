from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.http import Http404
from django.views.generic.base import View
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import PrintForm
from printers.models import Prints
from .forms import MyPrintForm

# 提交故障页面
@method_decorator(login_required, name='dispatch')
class UpFormView(View):
    def get(self, request):
        user = request.user
        prints = user.user_printer.filter(state=1)
        return render(request, "uploadform.html", {'user': user, 'prints':prints})

    def post(self, request):
        user = request.user
        print_form = MyPrintForm(request.POST)
        if print_form.is_valid():
            prints = request.POST.get('prints', "")
            prints = Prints.objects.get(pk=prints)
            print_form1 = print_form.save(commit=False)
            print_form1.pub_date = timezone.now()
            print_form1.repair_man = user
            print_form1.prints = prints
            print_form1.save()
            prints.service_num += 1
            prints.save()
            return HttpResponse('{"status":"您的故障已提交成功，请在主页持续关注"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"添加出错"}', content_type='application/json')


# 所有在维修的打印机页面
class FormListView(View):
    def get(self, request):
        all_forms = PrintForm.objects.all().order_by("-id")
        # 搜索框
        search_keywords = request.GET.get('keywords', "")
        if search_keywords:
            all_forms = all_forms.filter(repair_man__user_employee__name__icontains=search_keywords)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_forms, 10,  request=request)

        all_forms1 = p.page(page)
        # print(all_forms)

        return render(request, 'showforms.html', {
            "all_forms": all_forms1
        })
