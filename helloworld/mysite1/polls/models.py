from django.db import models


# Create your models here.
class question(models.Model):
    question_text = models.CharField(max_length=200)
    time_pub = models.DateTimeField()
class choice(models.Model):
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)
#class News(models.Model):
    #author = models.CharField(question, on_delete=models.CASCADE)
    #author = models.CharField(max_length=100)
    #title= models.CharField(max_length=100)
    #description = models.TextField()

 #   name = models.CharField(max_length=100)
  #  old = models.IntegerField(default=0)
   # def __str__(self):
    #    return self

#class POST(models.Model):

 #   choice_text = models.CharField(max_length=100)
  #  vote = models.IntegerField(default=0)
class News(models.Model):
    #author = models.CharField(question, on_delete=models.CASCADE)
    #author = models.CharField(max_length=100)
    #title= models.CharField(max_length=100)
    #description = models.TextField()

    name = models.CharField(max_length=100)
    old = models.IntegerField(default=0)
    adress = models.CharField(max_length=100)
    def __str__(self):
        return self.old

