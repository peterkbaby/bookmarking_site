from django.contrib import admin
from .models import books

  
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    readonly_fields =('created',)

admin.site.register(books, BookAdmin)