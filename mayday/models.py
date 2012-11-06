from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType


class Book(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField('Person')
    active = models.BooleanField(default=True)
    last_modified = models.DateTimeField(auto_now=True, auto_now_add=True, editable=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, help_text='For example 38.99')
    amazon_url = models.URLField(max_length=100,
                                 help_text='http://www.amazon.de/Pro-Django-Experts-Voice-Development/dp/1430210478/',
                                 verbose_name='Amazon URL')
    rating = models.PositiveSmallIntegerField(choices=((x, str(x)) for x in xrange(0, 11)), default=5)
    info_text = models.CharField(max_length=200, verbose_name='Info Text')
    preview_image = models.ImageField(upload_to='uploads/%Y/%m/%d', blank=True)

    def __unicode__(self):
        return u"%s (%s)" % (self.title, self.id)

    def isCheap(self):
        return self.price < 10
    isCheap.short_description = 'Is Cheap?'
    isCheap.boolean = True


class Person(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=2, choices=(('M', 'male'), ('F', 'female')))
    last_modified = models.DateTimeField(auto_now=True, auto_now_add=True, editable=False)
    photo = models.ImageField(upload_to='uploads/%Y/%m/%d')

    def __unicode__(self):
        return u"%s (%s)" % (self.name, self.id)


class BookCollection(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='uploads/%Y/%m/%d')
    content_type = models.ForeignKey(ContentType, blank=True, null=True,
                                                  related_name="bookcollection",
                                                  limit_choices_to={'model__in': ['Person']})
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey("content_type", "object_id")

    def __unicode__(self):
        return u"%s (%s)" % (self.name, self.id)


class BookCollectionInline(models.Model):
    bookcollection = models.ForeignKey('BookCollection')
    book = models.ForeignKey('Book', limit_choices_to={'active__exact': 1})
    position = models.PositiveSmallIntegerField('Position')

    class Meta:
        ordering = ['position']
        verbose_name = 'Book Collection'
        verbose_name_plural = 'Book Collections'
