from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Register the Admin classes for Author using the decorator
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

# Register the Admin classes for Genre using the decorator
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for BookInstance using the decorator
@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass



