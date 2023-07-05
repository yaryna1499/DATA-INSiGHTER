from django.db import models

# Create your models here.

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255, default='#', blank=True, null=True)
    parent = models.ForeignKey("MenuItem", default='', null=True, blank=True, on_delete=models.PROTECT, related_name="childs")

    @property
    def child_items(self):
        return self.childs.all()


    def __str__(self):
        return self.title
