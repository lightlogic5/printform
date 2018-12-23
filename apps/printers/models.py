from django.db import models
from django.contrib.auth.models import User


class Prints(models.Model):
    TYPE_CHOICES = (
        ('1', '惠普7110'),
        ('2', '惠普1108'),
        ('3', '三星2070'),
        ('4', '惠普5200'),
        ('5','爱普生1600k')
    )
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user_printer', null=True, blank=True)
    SN = models.IntegerField(default=0, verbose_name="打印机编码")
    pub_date = models.DateTimeField(verbose_name="发放日期", null=True, blank=True)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default=1, verbose_name="打印机型号")
    service_num = models.IntegerField(default=0, verbose_name="维修次数")
    comment = models.TextField(verbose_name="管理员备注", null=True, blank=True)

    class Meta:
        verbose_name = '打印机信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.SN, self.type)
