from django.db import models
import datetime
import os

def getFileName(request,filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)

class collection(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    created_at=models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.name

class places(models.Model):
    collections=models.ForeignKey(collection,on_delete=models.CASCADE)
    name=models.CharField(max_length=255,null=False,blank=False)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.name