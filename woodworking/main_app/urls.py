from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about,name='about'),
    path('tools/',views.tools_index, name='tools_index'),
    path('tool/<int:tool_id>/', views.tool_details, name='tool_details'),
    path('tool<int:pk>/update', views.ToolUpdate.as_view(), name='tool_update'),
    path('tools/create/', views.CreateTool.as_view(), name= 'tool_create'),


    
]
