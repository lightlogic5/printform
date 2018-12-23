import xadmin

from .models import Prints

class PrintsAdmin(object):
    list_display = ['SN', 'type', 'pub_date','service_num','comment']
    search_fields = ['SN', 'type','service_num','comment']
    list_filter = ['SN', 'type', 'pub_date','service_num','comment']
    model_icon = 'fa fa-university'

xadmin.site.register(Prints, PrintsAdmin)