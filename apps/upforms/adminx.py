import xadmin

from .models import PrintForm

class PrintFormAdmin(object):
    list_display = ['service_category', 'pub_date', 'receive_date','over_date','back_date','repair_man','content','state','comment']
    search_fields = ['service_category','repair_man','content','state','comment']
    list_filter = ['service_category', 'pub_date', 'receive_date','over_date','back_date','repair_man','content','state','comment']
    model_icon = 'fa fa-university'

xadmin.site.register(PrintForm, PrintFormAdmin)

