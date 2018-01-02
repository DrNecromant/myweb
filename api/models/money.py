from django.db import models
from datetime import date
from django.conf import settings

__all__ = ('Payment', 'Category')


class Payment(models.Model):
    amount = models.PositiveSmallIntegerField()
    spent = models.DateField(default=date.today)
    category = models.ForeignKey(settings.CATEGORY_MODEL)

    def __unicode__(self):
        return u"{}_{}_{}".format(self.amount, self.spent, self.category)


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u"{}".format(self.name)

    @property
    def count(self):
        return Payment.objects.filter(category=self.id).count()