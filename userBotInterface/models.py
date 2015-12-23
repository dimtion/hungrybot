from django.db import models

class choice_str(models.Model):
    text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.text

class hello_morning(models.Model):
    text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.text

class what_morning(models.Model):
    text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.text

class what_dejeuner(models.Model):
    text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.text

class entree_str(models.Model):
    text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.text
    
class plat_str(models.Model):
    text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.text

class dessert_str(models.Model):
    text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.text
    
class hello_dinner(models.Model):
    text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.text

class what_dinner(models.Model):
    text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.text
    

    
