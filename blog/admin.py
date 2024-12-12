from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
     Admin configuration for the Post model in the Django admin interface.

    This class customizes the admin interface for the Post model, allowing for easy management 
    of blog posts or articles. It integrates Summernote for rich text editing in the 'content' 
    field and provides various configurations for display and filtering.

    Attributes:
        list_display (tuple): Defines the fields to be displayed in the list view for each Post.
        search_fields (list): Specifies the fields that should be searchable in the admin interface.
        list_filter (tuple): Configures filter options in the sidebar, allowing admins to filter Posts by 
                              'status' and 'created_on' dates.
        prepopulated_fields (dict): Automatically populates the 'slug' field based on the 'title' field.
        summernote_fields (tuple): Enables the Summernote WYSIWYG editor for the 'content' field, allowing 
                                   for rich text editing.
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.

admin.site.register(Comment)