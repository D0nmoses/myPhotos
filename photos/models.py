from django.db import models

# Create your models here.


class Location(models.Model):
    location = models.CharField(max_length=20)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


class Category(models.Model):
    category = models.CharField(max_length=10)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


class Image(models.Model):
    image = models.ImageField(upload_to='images', default='default.png')
    image_name = models.CharField(max_length=20)
    imade_description = models.TextField()
    image_location = models.ForeignKey(Location,on_delete=models.CASCADE)
    image_category = models.ManyToManyField(Category)

    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_category(cls, search_term):
        images = cls.objects.filter(image_category__category__icontains=search_term)
        return images