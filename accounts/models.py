from django.db import models
from django.contrib.auth.models import User
from localflavor.generic import models as lf_models


class Customer(User):
    iban = lf_models.IBANField()
    photo = models.ImageField(upload_to='media/accounts/picture/%Y/%m/%d',
                              null=True)
    creator = models.ForeignKey('self', null=True)

    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'
