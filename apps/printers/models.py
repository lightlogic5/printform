from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Prints(models.Model):
    TYPE_CHOICES = (
        ('1', '惠普7110'),
        ('2', '惠普1108'),
        ('3', '三星2070'),
        ('4', '惠普5200'),
        ('5','爱普生1600k')
    )
    STATE_CHOICES = (
        ('1', '在使用'),
        ('2', '报废'),
    )

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user_printer', null=True, blank=True)
    SN = models.CharField(max_length=50,default=0, verbose_name="打印机编码")
    pub_date = models.DateField(verbose_name="发放日期", null=True, blank=True)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default=1, verbose_name="打印机型号")
    service_num = models.IntegerField(default=0, verbose_name="维修次数")
    comment = models.TextField(verbose_name="管理员备注", null=True, blank=True)
    state = models.CharField(max_length=1, choices=STATE_CHOICES, default=1, verbose_name="打印机状态")

    class Meta:
        verbose_name = '打印机信息'
        verbose_name_plural = verbose_name


    def __str__(self):
        return '{0}({1}){2}'.format(self.SN, self.type,self.get_type_display())

    def get_absolute_url(self):
        return reverse('users:employee')
