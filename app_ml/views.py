
from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect

from .forms import CardioForm
import pandas as pd
import numpy as np
import joblib

def result(request):
    return render(request, 'result.html')

def predict(request):
    return render(request, 'predict.html')

@csrf_protect
def index(request):
    if request.method == 'POST':
        form = CardioForm(request.POST)
        if form.is_valid():
            # Recebe os dados do formulário
            name = form.cleaned_data['name']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            age = float(form.cleaned_data['age'])
            gender = float(form.cleaned_data['gender'])
            weight = float(form.cleaned_data['weight'])
            height = float(form.cleaned_data['height'])
            systolic_pressure = float(form.cleaned_data['systolic_pressure'])
            diastolic_pressure = float(form.cleaned_data['diastolic_pressure'])
            glucose = float(form.cleaned_data['glucose'])
            smoker = float(form.cleaned_data['smoker'])
            cholesterol = float(form.cleaned_data['cholesterol'])
            alcohol_intake = float(form.cleaned_data['alcohol_intake'])
            physical_activity = float(form.cleaned_data['physical_activity'])

            imc = int(weight / (height / 100) ** 2)
            # Carrega o modelo treinado
            model = joblib.load('./model/random_forest_cardio.pkl')

            # Realiza as previsões usando o modelo treinado
            X = np.array([age, gender, weight, height, systolic_pressure, diastolic_pressure, glucose, smoker, cholesterol, alcohol_intake, physical_activity])
            X = X.reshape(1, -1)
            X = X.astype(np.float32)
            y_pred = model.predict(X)
            
            # Transforma a previsão em uma mensagem para enviar por e-mail
            if y_pred[0] == 0:
                resultado = 'Não foi identificado nenhum indício de doença cardíaca.'
            else:
                resultado = 'Há indícios de doença cardíaca!'
            
            # Envia o resultado por e-mail para o usuário
            html_content = render_to_string('result.html', {'name': name, 'lastname': lastname, 'resultado': resultado, 'imc': imc})
            text_content = strip_tags(html_content)

            subject = 'Resultado da previsão de doença cardíaca'
            message = "Olá {} {}! Gostaríamos de informar que o resultado da sua análise preditiva é: {}".format(name, lastname, resultado)

            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]
            e_mail = EmailMultiAlternatives(
                subject,
                text_content,
                from_email,
                recipient_list,
            )
            e_mail.attach_alternative(html_content, 'text/html')
            e_mail.send()

            return HttpResponseRedirect('/predict/')
    else:
        form = CardioForm()
        resultado = 'Verifique se preencheu corretamente o formulário'

    # Renderiza a página de resultado
    return render(request, 'index.html', {'form': form, 'resultado': resultado})

