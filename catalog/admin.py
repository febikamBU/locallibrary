from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    pass


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


class GenreAdmin(admin.ModelAdmin):
    pass


# Register the admin class with the associated model
admin.site.register(Genre, GenreAdmin)


class BookAdmin(admin.ModelAdmin):
    pass


# Register the admin class with the associated model
admin.site.register(Book, BookAdmin)


class BookInstanceAdmin(admin.ModelAdmin):
    pass


# Register the admin class with the associated model
admin.site.register(BookInstance, BookInstanceAdmin)


class LanguageAdmin(admin.ModelAdmin):
    pass


# Register the admin class with the associated model
admin.site.register(Language, LanguageAdmin)
