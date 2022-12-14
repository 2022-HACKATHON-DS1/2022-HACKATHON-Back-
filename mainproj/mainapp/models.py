from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='my_image')
    date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_year(self):
        return self.date.year