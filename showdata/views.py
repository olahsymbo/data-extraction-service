from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import TaskSerializer
from django.shortcuts import render
import logging
from .models import Taskdata

# Get an instance of a logger
logger = logging.getLogger(__name__)


class showtask(generics.ListAPIView):

    """

    create a view to handle requests and return a response.
    in this view, we have "retrieve" method, whhich accepts a GET
    request and response with proper response message and data.

    the second method is "index" which also take a GET request and
    return the fetch in an HTML template "home.html"

    """

    queryset = Taskdata.objects.all()

    serializer_class = TaskSerializer

    def retrieve(self, request, *args, **kwargs):
        super(showtask, self).retrieve(request, args, kwargs)

        instance = self.get_object()

        serializer = self.get_serializer(instance)

        data = serializer.data

        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully retrieved",
                    "result": data}

        logger.info(data)

        return Response(response)

    def index(request):

        data = Taskdata.objects.all()

        context = {'data': data}

        logger.info(data)

        return render(request, 'home.html', context)