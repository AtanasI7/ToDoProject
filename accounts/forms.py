from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

UserModel = get_user_model()


# TODO: Need to fix these
class ToDoUserBaseForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('username', 'email')

class ToDoUserDeleteForm(ToDoUserBaseForm):
    pass

class ToDoUserEditForm(ToDoUserBaseForm):
    pass