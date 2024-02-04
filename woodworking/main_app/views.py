from django.shortcuts import render
from .models import Tool
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')



def tools_index(request):
    tools = Tool.objects.all()
    return render(request,'tools/index.html', {'tools': tools})

def tool_details(request, tool_id):
    tool= Tool.objects.get(id= tool_id)
    return render(request, 'tools/details.html', {'tool':tool})

class CreateTool(CreateView):
    model= Tool
    fields= '__all__'
    success_url= '/tools/'

class ToolUpdate(UpdateView):
    model= Tool
    fields= '__all__'