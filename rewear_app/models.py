from django.db import models
from django.urls import reverse


# Create your models here.
#Created this class

class Post(models.Model):
#List of choices for major value in database, human readable name
    Type = (
        ('Tops', 'Tops'),
        ('Bottoms', 'Bottoms'),
        ('Outerwear', 'Outerwear'),
        ('Shoes', 'Shoes'),
        ('Assosories', 'Assosories'),
        ('Dresses', 'Dresses'),
        ('Shirt', 'Shirt')
        )
    Size = (
        ('XXXS', 'Three XS'),
        ('XXS', 'Extra Extra Small'),
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Meduim'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Extra Extra Large'),
        ('XXL', 'Three XL'),
        ('Other', 'Other')
        )

    image = models.ImageField(upload_to='images')           # Make it into an array later so multiple images can be uploaded
    brand = models.CharField(max_length=200)                # might make it a dropdown with an other option
    contact_info = models.CharField(max_length=200)         # Place for user to input info
    type = models.CharField(max_length=200, choices=Type)   # type of clothing
    size = models.CharField(max_length=200, choices=Size)   # defualt size
    about = models.CharField(max_length=200,blank=True)     # Allows user to input more info
    more_sizing = models.BooleanField(default=False)        # Check allows users to sort by more sizes
    title = models.CharField(max_length=200)

    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.title
    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])