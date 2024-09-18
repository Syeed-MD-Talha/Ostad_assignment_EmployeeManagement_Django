from django import forms  
from .models import  Employee  
  
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee 
        fields='__all__' 
        # widgets={
        #     'salary':forms.TextInput(attrs={'readonly':True}),
        #     'designation':forms.TextInput(attrs={'readonly':True}),
        # }
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        # If the form is updating an existing employee, disable the salary and designation fields
        if self.instance and self.instance.pk:
            self.fields['salary'].disabled = True
            self.fields['designation'].disabled = True