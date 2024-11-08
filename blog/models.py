from django.db import models
import uuid
from django.core.validators import MinValueValidator
# Create your models here.




class LanguageChoices(models.TextChoices):
    FR = 'FR', 'French'
    EN = 'EN', 'English'
    IT = 'IT', 'Italian'

class Blog(models.Model):
    blog_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    details = models.TextField()
    age = models.IntegerField(validators=[MinValueValidator(18)],null=True)
    # language = models.CharField(max_length=10,choices=LanguageChoices.choices,default=LanguageChoices.EN)
    language = models.CharField(max_length=10,default=LanguageChoices.EN)
    """
    if we use choices=LanguageChoices.choice we can not validate the language field
    """