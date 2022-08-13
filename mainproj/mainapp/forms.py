from django import forms
from .models import Post
from .widgets import PreviewFileWidget

class DateInput(forms.DateInput):
    input_type = 'date'

# 장고 폼 
class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','image', 'date', 'content']

        labels = {
            'title' : '',
            'content' : '',
        }

        widgets = {
            'image': PreviewFileWidget(),
            'date': DateInput(
                attrs={
                    'id':'datepicker'
                }
            ),
            'title' : forms.TextInput(
                attrs={
                    'class':'uploadTitle',
                    'placeholder': '제목'
                }
            ),
            'content' : forms.Textarea(
                attrs={
                    'class':'uploadTextarea',
                    'placeholder': '본문에 해쉬태그를 이용하여 태그를 사용해보세요! (최대 30개)',
                }
            ),
        }