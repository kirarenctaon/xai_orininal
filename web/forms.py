from django import forms
from .models import News, Community

class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ('titleen', 'contenten', 'submenu_id')

class CommunityForm(forms.ModelForm):

    class Meta:
        model = Community
        fields = ('titleen', 'contenten', 'writer', 'submenu_id')
