from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postdata):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postdata['pw']) < 8:
            errors['pw'] = "password must be 8 Charcters long"
        if len(postdata['fname']) < 2 or len(postdata['lname']) < 2:
            errors['name'] = "First name must be at least 2 Charcters long"
        if not EMAIL_REGEX.match(postdata['email']):
            errors['email'] = "email must be valid"
        return errors        


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email =  models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()
