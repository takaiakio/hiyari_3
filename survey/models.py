from django.db import models

class NearMissReport(models.Model):
    title = models.CharField(max_length=200, verbose_name="題名")
    description = models.TextField(verbose_name="遭遇場面")
    frequency = models.IntegerField(verbose_name="遭遇頻度")
    mitigation = models.TextField(verbose_name="ミス回避策")

    def __str__(self):
        return self.title
