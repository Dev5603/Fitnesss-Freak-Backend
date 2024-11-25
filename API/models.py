from django.db import models

# Create your models here.
TYPES = (
    ('GOLD', 'Gold'),
    ('DIAMOND', 'Diamond')
)

class News(models.Model):
    class Meta:
        verbose_name_plural = 'News'

    title = models.CharField(max_length=500)
    content = models.TextField()
    image = models.CharField(max_length=500)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'image': self.image
        }

    def __str__(self) -> str:
        return str(self.id)
    
class Contact(models.Model):
    class Meta:
        verbose_name_plural = 'Contact'

    name = models.CharField(max_length=200)
    number = models.CharField(max_length=10)
    email = models.EmailField()

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'number': self.number,
            'email': self.email
        }
    
    def __str__(self) -> str:
        return self.name
    
class Membership(models.Model):
    name = models.CharField(max_length=50)
    amount = models.CharField(max_length=6)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'amount': self.amount
        }
    
    def __str__(self) -> str:
        return f'{self.name} Plan'
    
class PT(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=TYPES)
    amount = models.CharField(max_length=6)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'amount': self.amount
        }
    
    def __str__(self) -> str:
        return f'{self.name} {self.type} Plan'