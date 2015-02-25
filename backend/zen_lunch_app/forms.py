from django.forms import ModelForm
from zendesk_lunch_app.models import User

class SignUpForm(ModelForm):
	class Meta:
		model = User
		fields = ['email', 'zen_lunch_time']