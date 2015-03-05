from django.forms import ModelForm
from zendine.models import User

class SignUpForm(ModelForm):
	class Meta:
		model = User
		fields = ['email', 'zen_lunch_time']