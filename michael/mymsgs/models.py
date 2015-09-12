from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name
    
class Message(models.Model):
    user = models.ForeignKey(User)
    content = models.CharField(max_length=1024)
    
    def __unicode__(self):
        return self.content