from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
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
        # Recebe os dados do formulário
        name = request.POST['name']
        lastname = request.POST['lastname']
        email = request.POST['email']
        age = float(request.POST['age'])
        gender = float(request.POST['gender'])
        weight = float(request.POST['weight'])
        height = float(request.POST['height'])
        systolic_pressure = float(request.POST['systolic_pressure'])
        diastolic_pressure = float(request.POST['diastolic_pressure'])
        glucose = float(request.POST['glucose'])
        smoker = float(request.POST['smoker'])
        cholesterol = float(request.POST['cholesterol'])
        alcohol_intake = float(request.POST['alcohol_intake'])
        physical_activity = float(request.POST['physical_activity'])

        imc= int(weight /(height/100)**2)
        # Carrega o modelo treinado
        model = joblib.load('./model/random_forest_cardio.pkl')
        
        # Realiza as previsões usando o modelo treinado
        
        X = np.array([age, gender, weight, height, systolic_pressure, diastolic_pressure, glucose, smoker, cholesterol, alcohol_intake, physical_activity])
        X = X.reshape(1, -1)
        X = X.astype(np.float32)
        y_pred = model.predict(X)
        # Transforma a previsão em uma mensagem para enviar por e-mail
        if y_pred[0] == 0:
            resultado = 'sem sintomas de doença cardíaca'
        else:
            resultado = 'com possivel doença cardíaca'
        
        
        # Envia o resultado por e-mail para o usuário
         # Envia o resultado por e-mail para o usuário
        html_content = render_to_string('result.html', {'name': name, 'lastname': lastname, 'resultado': resultado, 'imc':imc})
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
        resultado = 'Verifique se preencheu corretamente o formulário'
        
    # Renderiza a página de resultado
    return render(request, 'index.html', {'resultado': resultado})


