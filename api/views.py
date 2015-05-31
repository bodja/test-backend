import requests
from urllib.parse import urlencode

from django.db import transaction
from django.contrib.auth.models import User
from django.conf import settings

from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from oauth2client.client import OAuth2WebServerFlow, FlowExchangeError

from accounts.models import Customer, CredentialsModel
from api.permissions import IsCreatorOrReadOnly
from api.serializers import CustomerSerializer


class AuthAPIView(APIView):
    def get(self, *args, **kwargs):
        return Response({'url': self.flow.step1_get_authorize_url()},
                        status.HTTP_200_OK)

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        try:
            credentials = self.flow.step2_exchange(request.DATA.get('code'))
        except (ValueError, FlowExchangeError) as err:
            return Response({'errors': [str(err)]},
                            status=status.HTTP_400_BAD_REQUEST)
        details = self.get_token_details(access_token=credentials.access_token)
        user, _ = User.objects.get_or_create(
            email=details['email'], username=details['email'].split('@')[0])
        user_credentials, _ = CredentialsModel.objects.get_or_create(user=user)
        user_credentials.credential = credentials
        user_credentials.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'id': user.id})

    @classmethod
    def get_token_details(cls, access_token):
        url = 'https://www.googleapis.com/oauth2/v1/tokeninfo'
        query_string = urlencode({'access_token': access_token})
        response = requests.get('{}?{}'.format(url, query_string))
        return response.json()

    @property
    def flow(self):
        return OAuth2WebServerFlow(
            client_id=settings.GOOGLE_OAUTH2_ID,
            client_secret=settings.GOOGLE_OAUTH2_SECRET,
            scope=settings.GOOGLE_OAUTH2_SCOPE,
            redirect_uri=settings.GOOGLE_OAUTH2_REDIRECT_URI)


class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsCreatorOrReadOnly)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
