from .models import ImageCut
from django.forms import ModelForm, FileInput


class ImageForm(ModelForm):
	class Meta:
		model = ImageCut
		fields = ['img']

		widgets = {
			"img": FileInput(attrs={
				'class':'image_upload',
				'placeholder':'Put your image...'
			})
		}