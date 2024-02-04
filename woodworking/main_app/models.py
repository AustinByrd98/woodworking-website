from django.db import models

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