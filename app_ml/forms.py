from django import forms
from .models import Patient

SEXO_COICES = (
    ('Masculino', 1),
    ('Feminino', 0),
)
class CardioForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields =(
            "name",
            "lastname",
            "email",
            "age",
            "gender",
            "weight",
            "height",
            "diastolic_pressure",
            "systolic_pressure",
            "glucose",
            "cholesterol",
            "smoker",
            "alcohol_intake",
            "physical_activity",

        )
