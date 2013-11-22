from django.db import models


class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255) 
    last_paid_date = models.DateField(null=True, blank=True)
    moral_entity = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)
