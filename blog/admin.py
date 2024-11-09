from django.contrib import admin
from .models import Post, Contact, Category, CommentPospt
from django.utils.html import format_html
from django.contrib import admin




admin.site.register(Contact)
admin.site.register(CommentPospt)


   




from django.utils.html import format_html
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'status', 'video_display')  

    list_filter = ('title',)
    search_fields = ('status',)
    prepopulated_fields = {'slug': ('title',)}

    def video_display(self, obj):
        if obj.video:
            return format_html(
                '<video width="320" height="240" controls>'
                '<source src="{}" type="video/mp4">'
                'Your browser does not support the video tag.'
                '</video>', 
                obj.video.url
            )
        return "Video yo'q"

    video_display.short_description = 'Video Preview'







@admin.register(Category)
class CategoryPage(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}
# Register your models here.



