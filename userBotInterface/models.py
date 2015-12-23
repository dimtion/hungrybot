from django.db import models

class choice_str(models.Model):
    text = models.CharField(max_length=200)

class hello_morning(models.Model):
    text = models.CharField(max_length=200)

class what_morning(models.Model):
    text = models.CharField(max_length=200)    

class what_dejeuner(models.Model):
    text = models.CharField(max_length=200)

class entree_str(models.Model):
    text = models.CharField(max_length=200)
    
class plat_str(models.Model):
    text = models.CharField(max_length=200)    

class dessert_str(models.Model):
    text = models.CharField(max_length=200)
    
class hello_dinner(models.Model):
    text = models.CharField(max_length=200)

class what_dinner(models.Model):
    text = models.CharField(max_length=200)    
    

    
