from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length =150)
    author = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    

class Review(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE,related_name='reviews')   
    comment = models.TextField()

    def __str__(self):
        return f"Review for {self.book.title}"  
