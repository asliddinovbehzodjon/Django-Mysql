from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150,verbose_name='Post Title',help_text='Enter post title')
    description = models.TextField(verbose_name='Post Description',help_text='Enter post description')
    def __str__(self):
        return self.title
    class Meta:
        db_table ='Maqolalar'
