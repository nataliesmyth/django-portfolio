from django.db import models

# Create your models here.
# Textfield and Charfield are similar, but TextField can be used for longer form text because it doesn't have a max length limit.
# FilePathField also holds a string, but must point to a file path name
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")