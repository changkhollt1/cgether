from django.contrib import admin
from .models import Order, Comment
# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment

# admin.site.register(Order)

class PostAdmin(admin.ModelAdmin):
    list_display = ['table', 'custumer', 'date']
    list_filter =  ['table']
    search_fields = ['custumer']
    inlines = [CommentInline]
admin.site.register(Order, PostAdmin)


