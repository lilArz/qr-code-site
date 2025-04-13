from django.shortcuts import render
import qrcode
import io
import base64
from django import forms

class QRForm(forms.Form):
    data = forms.CharField(label='Введите текст или ссылку', max_length=200)

def home(request):
    qr_image = None

    if request.method == 'POST':
        form = QRForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['data']


            qr = qrcode.make(data)
            buffer = io.BytesIO()
            qr.save(buffer, format='PNG')
            img_str = base64.b64encode(buffer.getvalue()).decode()
            qr_image = f'data:image/png;base64,{img_str}'

    else:
        form = QRForm()


    return render(request, 'qr_app/home.html', {'form': form, 'qr_image': qr_image})