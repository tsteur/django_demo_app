from mayday.models import Book
from mayday.models import Person
from mayday.models import BookCollection
from mayday.models import BookCollectionInline
from mayday.forms import BookCollectionInlineForm
from django.contrib import admin


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'price', 'rating', 'isCheap', 'last_modified']
    search_fields = ['title', 'info_text']
    list_filter = ['last_modified', 'price', 'authors', 'active']
    date_hierarchy = 'last_modified'
    filter_horizontal = ('authors',)
    fieldsets = [
        (None,         {'fields':  ['title', 'active']}),
        ('Links',      {'fields':  ['amazon_url'],
                        'classes': ('grp-collapse grp-open',)}),
        ('Metadaten',  {'fields':  ['price', 'info_text', 'preview_image', 'authors'],
                        'classes': ('grp-collapse grp-open',)}),
    ]


class BookCollectionInlineAdmin(admin.TabularInline):
    fields = ('book', 'position')
    sortable_field_name = 'position'
    model = BookCollectionInline
    extra = 3
    form = BookCollectionInlineForm


class BookCollectionAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [BookCollectionInlineAdmin]
    related_lookup_fields = {
        'generic': [['content_type', 'object_id']],
    }


admin.site.register(Person)
admin.site.register(Book, BookAdmin)
admin.site.register(BookCollection, BookCollectionAdmin)
