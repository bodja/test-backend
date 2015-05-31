import uuid
from django.db import models
from django.contrib.auth.models import User
from localflavor.generic import models as lf_models
from oauth2client.django_orm import CredentialsField


class Customer(User):
    iban = lf_models.IBANField()
    photo = models.ImageField(upload_to='media/accounts/picture/%Y/%m/%d',
                              null=True)
    creator = models.ForeignKey(User, null=True, related_name='creators')

    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = str(uuid.uuid4())
        super(Customer, self).save(*args, **kwargs)


class CredentialsModel(models.Model):
    user = models.OneToOneField(User)
    credential = CredentialsField()
