from django.apps import AppConfig


class BlogConfig(AppConfig):
     """
    Configuration for the 'blog' app in the Django project.

    This class is used to configure settings and attributes for the 'blog' application within the 
    Django project. The 'BlogConfig' class is automatically discovered and used by Django when 
    the app is included in the project's INSTALLED_APPS.

    Attributes:
        default_auto_field (str): The field type used for automatically generated primary keys 
                                  for model fields. In this case, it's set to 'BigAutoField' 
                                  which creates a large integer field for primary keys.
        name (str): The name of the app. This is set to 'blog', which corresponds to the name 
                    of the application in the Django project.
    """
     default_auto_field = 'django.db.models.BigAutoField'
     name = 'blog'
