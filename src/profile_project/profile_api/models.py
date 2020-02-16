from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class UserProfile(models.Model):
	'''
	Represents a user profile in our system
	'''
	email = models.EmailField(max_length=255, unique=True)
	name = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)


	objects = UserProfileManager()

	USERNAME_FIELD = 'email' # replacing username
	REQUIRED_FIELDS = ['name']


	# Helper Function
	def get_full_name(self):
		'''
			used to get a user full name.
		'''
		return self.name

	def get_short_name(self):
		'''
		used to get a user shor name
		'''
		return self.name

	def __str__(self):
		return self.email
