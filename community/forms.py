from django import forms


class CommunicationForm(forms.Form):
    writer = forms.CharField(max_length=None,
    widget=forms.TextInput(
        attrs={
            'class': 'input',
            'value': '{{request.user.username }}',
            'type': 'hidden',
        }
    ))

    author = forms.CharField(max_length=None),
    widget=forms.TextInput(
        attrs={
            'class': 'input',
            'value': '{{request.user.username}}',
            'type': 'hidden',
        }
    )

    title = forms.CharField(max_length=100,
    error_messages={
        'required': '제목을 입력해주세요',
        'invallid': '제목이 너무 깁니다. 100자 이내로 써주세요',
    },
    widget=forms.TextInput(
        attrs={
            'class': 'input', 
            'placeholder': '소통내용의 제목을 입력해주세요',
        }
    ))

    content = forms.CharField(max_length=None,
    error_messages={
        'required': '소통 내용을 입력해주세요',
    },
    widget=forms.Textarea(
        attrs={
            'class': 'textarea',
            'placeholder': '소통 내용을 입력해 주세요'
        }))

