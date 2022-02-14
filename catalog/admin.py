from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Register the Admin classes for Author using the decorator


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name',
                    'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# Register the Admin classes for Genre using the decorator


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for Book using the decorator


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    fieldsets = (
        ("Book Information", {
            'fields': ('title', 'author', 'isbn', 'summary', ('genre', 'language'))
        }),
    )

# Register the Admin classes for BookInstance using the decorator


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        ("Book Instance", {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

# Register the Admin classes for BookInstance using the decorator


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


admin.site.site_header = "Local Library Admin"
admin.site.site_title = "Local Library Admin Portal"
admin.site.index_title = "Welcome to Local Library Portal"
