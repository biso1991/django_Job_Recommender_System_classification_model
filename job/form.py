from django import forms

from .models import User_apply_job


class ApplyJob(forms.ModelForm):
    class Meta:

        model = User_apply_job
        fields = ["name", "email","website","coverletter"]#"cv",
