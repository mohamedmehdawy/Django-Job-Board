from django import forms
from .models import Apply, Job

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = "__all__"
        exclude = ["job"]
class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__"
        exclude = ["owner","slug", "same_slugs"]