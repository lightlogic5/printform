import datetime
import xadmin

from .models import PrintForm

class PrintFormAdmin(object):
    list_display = ['service_category', 'pub_date', 'receive_date','over_date','back_date','repair_man','content','state','comment']
    search_fields = ['service_category','repair_man','content','state','comment']
    list_filter = ['service_category', 'pub_date', 'receive_date','over_date','back_date','repair_man','content','state','comment']
    model_icon = 'fa fa-university'
    list_editable = ['state',]


'''
    def save_models(self):
        print(self.new_obj.state)
         在改变维修state时，自动创建对应时间
        obj = self.new_obj
        obj.save()
        if obj.state=='2':
            obj.receive_date=datetime.datetime.now()
            obj.save()            
'''

xadmin.site.register(PrintForm, PrintFormAdmin)

