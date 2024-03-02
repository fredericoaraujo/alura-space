from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Usuário",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder': 'Ex.: João Silva',
                'autocomplete':"off",
            }
        )
    )
    
    senha_login = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form-control',
                'autocomplete':"off",
            }
        )
    )

class CadastroForms(forms.Form):
    nome_login = forms.CharField(
        label="Usuário",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder': 'Ex.: João Silva',
                'autocomplete':"off",
            }
        )
    )
    
    email_login = forms.EmailField(
        label="E-mail",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class' : 'form-control',
                'placeholder': 'Ex.: joaosilva@xpto.com.br',
                'autocomplete':"off",
            }
        )
    )
    
    senha_login = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form-control',
                'autocomplete':"off",
            }
        )
    )
    
    confirma_senha_login = forms.CharField(
        label="Confirmação de Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form-control',
                'autocomplete':"off",
            }
        )
    )

