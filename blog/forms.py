from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form for submitting comments on blog posts.

    This class defines a form for users to submit their comments to blog posts. It is based on the 
    `Comment` model and includes only the necessary fields required for comment submission.

    The form is a subclass of `forms.ModelForm`, which means it automatically generates form fields 
    based on the `Comment` model. In this case, the form includes a single field: `body`, 
    which holds the content of the comment.

    Attributes:
        Meta (class): The inner Meta class tells Django that this form is associated with the 
                      `Comment` model and specifies the fields to be included in the form.
    
    Fields:
        - body (str): The content of the comment, a required text field where users can write 
                      their thoughts or responses to the post.
    """
    class Meta:
        model = Comment
        fields = ('body',)