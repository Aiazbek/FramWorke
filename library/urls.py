from django.contrib import admin
from django.urls import path, include
from api.views import TaskList, TaskCreate, TaskDetail
from .api import router
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/create/', TaskCreate.as_view(), name='task-create'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
]


