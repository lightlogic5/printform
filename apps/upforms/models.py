from django.db import models
from django.contrib.auth.models import User

from printers.models import Prints


class PrintForm(models.Model):
    STATE_CHOICES = (
        ('1', '提交中'),
        ('2', '已接收'),
        ('3', '已修好'),
        ('4', '已确认取回'),
    )
    service_category = models.CharField(max_length=200, verbose_name="故障类型", null=True, blank=True)
    pub_date = models.DateTimeField(verbose_name="提交日期", null=True, blank=True)
    receive_date = models.DateTimeField(verbose_name="接收日期", null=True, blank=True)
    over_date = models.DateTimeField(verbose_name="处理完毕日期", null=True, blank=True)
    back_date = models.DateTimeField(verbose_name="取回日期", null=True, blank=True)
    repair_man = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='form_employee', null=True, blank=True)
    content = models.TextField(verbose_name="故障描述")
    state = models.CharField(max_length=1, choices=STATE_CHOICES, default=1)
    comment = models.TextField(verbose_name="管理员备注", null=True, blank=True)
    prints = models.ForeignKey(Prints,on_delete=models.DO_NOTHING,related_name='form_pr', null=True, blank=True)


    class Meta:
        verbose_name = '表单信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.repair_man.__str__()
