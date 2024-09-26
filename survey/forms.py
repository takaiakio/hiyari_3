from django import forms
from .models import NearMissReport

class NearMissReportForm(forms.ModelForm):
    class Meta:
        model = NearMissReport
        fields = ['title', 'description', 'frequency', 'mitigation']
        labels = {
            'title': '題名',
            'description': '遭遇場面',
            'frequency': '遭遇頻度',
            'mitigation': '回避事由'
        }
