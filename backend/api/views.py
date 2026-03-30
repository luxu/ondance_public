from rest_framework import generics

from api.serializers import CitySerializer, CourseSerializer, StateSerializer, UserSerializer
from course.models import Course
from user.models import City, State, User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

users = UserList.as_view()


class UserCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

create_user = UserCreate.as_view()


class CityList(generics.ListAPIView):
    serializer_class = CitySerializer

    def get_queryset(self):
        qs = City.objects.select_related('state').order_by('name')
        state = self.request.query_params.get('state')
        if state:
            qs = qs.filter(state__abbreviation__iexact=state)
        return qs


cities = CityList.as_view()


class StateList(generics.ListAPIView):
    serializer_class = StateSerializer

    def get_queryset(self):
        qs = State.objects.order_by('name')
        search = self.request.query_params.get('search', '').strip()
        if len(search) >= 3:
            qs = qs.filter(name__icontains=search) | qs.filter(abbreviation__icontains=search)
        return qs


states = StateList.as_view()


class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.select_related('teacher').order_by('title')
    serializer_class = CourseSerializer


courses = CourseListCreate.as_view()
