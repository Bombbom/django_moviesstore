from django.db import models
from django.contrib.auth.models import User 
from movies.models import Movie 
# Create your models here.


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    
    total = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # email = models.EmailField()
    # address=models.CharField(max_length=250)
    # postal_code = models.CharField(max_length=20)
    # city=models.CharField(max_length=100)
    # created = models.DateTimeField(auto_now_add=True)
    # updated =    models.DateTimeField(auto_now=True)
    # paid = models.BooleanField(default=False)
    
    # class Meta:
    #     ordering = ['-created']
    
    def __str__(self):
        return str(self.id) + ' - ' + self.user.username 
    
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete= models.CASCADE)
    def __str__(self):
        return str(self.id) + ' - ' + self.movie.name 
