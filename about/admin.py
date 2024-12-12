from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the 'About' model in the Django admin interface.

    This class customizes the admin interface for the 'About' model, enabling the Summernote 
    WYSIWYG (What You See Is What You Get) editor for the 'content' field. The admin interface 
    for the 'About' model will display a rich text editor for managing the content.

    The Summernote editor allows easy formatting and editing of the 'content' field, which might 
    contain detailed information such as the company's history, mission, or other important details.

    Attributes:
        summernote_fields (tuple): Specifies that the 'content' field in the About model will 
                                   use the Summernote rich text editor, allowing for a more user-friendly 
                                   text editing experience in the Django admin.

    Methods:
        - None (class-based configuration).
    """

    summernote_fields = ('content',)

# Register your models here.

# admin.site.register(About)
# Note: admin.ModelAdmin is the standard way of registering
#       our model with the admin panel. We do it differently
#       above because we are supplying Summernote fields.
#       If you want to customise the admin panel view in your
#       own projects, then inherit from admin.ModelAdmin like
#       we do below.

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
     """
    Admin configuration for the 'CollaborateRequest' model in the Django admin interface.

    This class customizes the admin interface for the 'CollaborateRequest' model, allowing 
    administrators to manage collaboration requests easily. The admin interface will display 
    specific fields and allow filtering, searching, and modification of the collaboration 
    request entries.

    Attributes:
        list_display (tuple): Defines the fields to be displayed in the list view for each 
                               CollaborateRequest entry. In this case, the 'message' and 'read' 
                               fields are shown, allowing admins to quickly review the requests 
                               and whether they have been read.

    Methods:
        - None (class-based configuration).
    """


     list_display = ('message', 'read',)