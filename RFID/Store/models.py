from django.db import models

# Create your models here.
class Object(models.Model):

    allstatus = (('อยู่','อยู่'),('ไม่อยู่','ไม่อยู่'))

    tag_id = models.IntegerField(default=0)
    object_name = models.CharField(max_length=200)
    add_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=allstatus, default='อยู่')

    def __str__(self):
        return self.object_name +'-'+ self.status