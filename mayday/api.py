from tastypie.resources import ModelResource
from mayday.models import Book, Person, BookCollection
from tastypie import fields


class PersonResource(ModelResource):
    class Meta:
        queryset = Person.objects.all()


class BookResource(ModelResource):
    authors = fields.ToManyField(PersonResource, 'authors')

    class Meta:
        queryset = Book.objects.all()
        excludes = ['active']
        allowed_methods = ['get']
        resource_name = 'books'


class BookCollectionResource(ModelResource):
    class Meta:
        queryset = BookCollection.objects.all()
        resource_name = 'bookcollections'
