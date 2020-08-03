from django.db import models


class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Publisher(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Friend(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, default=None, related_name="published_books")
    lend_to = models.ManyToManyField(Friend)
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(default=0, max_digits=11, decimal_places=2)

    def __str__(self):
        return self.title
