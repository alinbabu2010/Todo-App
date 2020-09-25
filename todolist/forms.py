from django import forms


class TodoListForm(forms.Form):
    text = forms.CharField(max_length=45, widget=forms.TextInput(attrs={
                           'class': 'form-control p-4', 'placeholder': 'Enter todo e.g. Wash my car', 'aria-label': 'Todo', 'aria-describedby': 'button-addon2'}))
