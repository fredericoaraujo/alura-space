from django import forms

class LoginForms(forms.Form):
    username = forms.CharField(
        label="Usuário",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder': 'Ex.: João Silva',
            }
        )
    )
    
    password = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form-control',
            }
        )
    )

class CadastroForms(forms.Form):
    username = forms.CharField(
        label="Usuário",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder': 'Ex.: João Silva',
            }
        )
    )
    
    email = forms.EmailField(
        label="E-mail",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class' : 'form-control',
                'placeholder': 'Ex.: joaosilva@xpto.com.br',
            }
        )
    )
    
    password = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form-control',
            }
        )
    )
    
    confirm_password = forms.CharField(
        label="Confirmação de Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form-control',
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("As senhas não coincidem.")

        return cleaned_data

