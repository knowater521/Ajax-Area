from django.db import models


class AreaInfo(models.Model):
    title = models.CharField(max_length=255)
    parea = models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE)
    # parea 对应的表里的id 是parea_id
