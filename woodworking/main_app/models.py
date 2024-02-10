from django.db import models
from django.urls import reverse

TYPES= (
        ('S','Sharpen'),
        ('C','Clean'),

)
# Create your models here.
'''i need a table:
 for tools
  a way of catorizing those tools 
   to tutorials about using those tools and general techniques
    for projects 
     and i want all these conected  '''


class Tool(models.Model):
   
        name= models.CharField(max_length = 100)
        desc = models.CharField(max_length = 100)
        tutorial = models.CharField(max_length = 100)

        def get_absolute_url(self):
                return reverse('tool_details', kwargs={'tool_id': self.id})
        
class Maintenance(models.Model):
        date = models.DateField('Maintenance Date')
        maintenance_type= models.CharField(
                max_length=1,
                choices= TYPES,
                )
        tool= models.ForeignKey(Tool, on_delete= models.CASCADE)
        def __str__(self) -> str:
                return f"{self.get_maintenance_type_display()} on {self.date}"
        
        class Meta:
                ordering= ['-date']