from django.db import models
from django.utils import timezone
from rembg import remove
from PIL import Image
import os
from django.core.files.base import ContentFile
from django.contrib.sessions.models import Session

# Create your models here.

class ImageCut(models.Model):
	img = models.ImageField(upload_to="images")
	out_img = models.ImageField(blank=True, upload_to="out_images")
	uploader_session = models.CharField(max_length=60, blank=True)
	created_at = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return str(self.id)
	
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		if self.img and not self.out_img:
			input_image_path = self.img.path
			output_image_path = f"{self.img.name.split('.')[0]}_out.png"  # Имя файла для выходного изображения

			with open(input_image_path, "rb") as f:
					image_data = f.read()

			processed_image_data = remove(image_data)

			# Сохранение обработанного изображения
			# with open(output_image_path, "wb") as f:
			# 		f.write(processed_image_data)

			self.out_img.save(f"{output_image_path}", ContentFile(processed_image_data), save=False)
			super().save(*args, **kwargs)