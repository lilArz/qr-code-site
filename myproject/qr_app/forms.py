from django import Forms

class QRCodeForm(forms.Form):
    data=Forms.CharField(label='manasov arzuubek', max_length=300)
