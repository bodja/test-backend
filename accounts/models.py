import uuid
from django.db import models
from django.contrib.auth.models import User
from localflavor.generic import models as lf_models
from oauth2client.django_orm import CredentialsField
from sorl.thumbnail.shortcuts import get_thumbnail


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

    def get_photo_thumbnail(self, width, height):
        if self.photo:
            return get_thumbnail(self.photo, '{}x{}'.format(width, height))
        return None

    @property
    def thumbnail_16x9(self):
        """
        returns thumbnail in 16:9 aspect ratio
        """
        return self.get_photo_thumbnail(600, 338) # 16:9

    @property
    def thumbnail_2x3(self):
        """
        returns thumbnail in 2:3 aspect ratio
        """
        return self.get_photo_thumbnail(400, 600)

    @property
    def thumbnail_small(self):
        """
        returns thumbnail in 2:3 aspect ratio
        """
        return self.get_photo_thumbnail(70, 70)


class CredentialsModel(models.Model):
    user = models.OneToOneField(User)
    credential = CredentialsField()
