from django import forms
from .models import Course,Tag

class CourseForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    class Meta:
        model = Course
        fields = ['title', 'description', 'price', 'subject', 'tags', 'start_date']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter description'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter price'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Enter subject'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        instructor = kwargs.pop('instructor', None)
        super(CourseForm, self).__init__(*args, **kwargs)
        if instructor:
            self.instance.instructor = instructor

    def save(self, commit=True):
        course = super(CourseForm, self).save(commit=False)
        if commit:
            course.save()
        return course
