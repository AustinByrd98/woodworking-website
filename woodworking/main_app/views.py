from django.shortcuts import render, redirect
from .models import Tool
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import MaintenanceForm
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
    maintenance_form= MaintenanceForm()
    return render(request, 'tools/details.html', {'tool':tool, 'maintenance_form':maintenance_form})

def add_maintenance(request,tool_id):
    form= MaintenanceForm(request.POST)
    if form.is_valid():
        new_maintenance= form.save(commit=False)
        new_maintenance.tool_id= tool_id
        new_maintenance.save()
    return redirect('tool_details',tool_id=tool_id)

class CreateTool(CreateView):
    model= Tool
    fields= '__all__'
    success_url= '/tools/'

class ToolUpdate(UpdateView):
    model= Tool
    fields= '__all__'

class ToolDelete(DeleteView):
    model= Tool
    success_url= '/tools/'
