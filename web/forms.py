from django import forms
from .models import News, Community, DemoResource

class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ('titleen', 'contenten', 'submenu_id')

class CommunityForm(forms.ModelForm):

    class Meta:
        model = Community
        fields = ('titleen', 'contenten', 'writer', 'submenu_id')

class DemoForm(forms.ModelForm):

    class Meta:
        model = DemoResource
        fields = ('titleen', 'contenten', 'writer', 'submenu_id')

