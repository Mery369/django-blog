from .models import CollaborateRequest
from django import forms


class CollaborateForm(forms.ModelForm):
    """
    Form for submitting a collaboration request.

    This form allows users to submit a collaboration request by providing their name, email, 
    and a message. It is based on the `CollaborateRequest` model and includes the necessary 
    fields to capture the relevant information.

    The form is a subclass of `forms.ModelForm`, which automatically generates form fields 
    based on the `CollaborateRequest` model. The fields included in the form are:
    - `name`: The name of the person requesting collaboration.
    - `email`: The email address of the person requesting collaboration.
    - `message`: A text field where the user can describe their collaboration proposal or 
      message.

    Attributes:
        Meta (class): The inner Meta class connects the form to the `CollaborateRequest` model 
                      and defines the fields that should be part of the form.

    Fields:
        - name (str): The name of the person submitting the collaboration request.
        - email (str): The email address of the person submitting the request.
        - message (str): The content of the collaboration request, where users can detail 
                         their interest in collaborating.
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name' , 'email','message')