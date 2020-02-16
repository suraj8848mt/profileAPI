from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, BaseUserManager



class UserProfileManager(BaseUserManager):
	'''
	Helps django work with our custom user model
	'''
	def create_user(self, email, name, password=None):
		''' Creates a new user profile object '''
		if not email:
			raise ValueError('User Must have an Email Address')
		email = self.normalize_email(email)
		user = self.model(email=email, name=name)
		user.set_password(password)
		user.save(using=self._db)

		return user


	def create_super_user(self, email,name, password):
		''' creates and saves a new superuser with given details '''
		user = self.create_user(email, name, password)
		user.is_superuser = True
		user.is_staff = True

		user.save(using=self._db)



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
