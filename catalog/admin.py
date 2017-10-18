from django.contrib import admin
from catalog.models import Genre, Author, Book, BookInstance, Language

admin.site.register(Genre)
# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(BookInstance)
admin.site.register(Language)


# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


#                                 alternative way to register

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    raw_id_fields = ("book",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre_display')
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book', 'status', 'borrower', 'due_back', 'id' )

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status','due_back', 'borrower')
        }),
    )
