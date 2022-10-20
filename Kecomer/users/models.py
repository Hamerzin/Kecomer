from django.db import models
from django.contrib.auth.models import AbstractUser
from users.customuser import MyUserManager


class User(AbstractUser):

    genre_choice = [
        ('M', 'Male'),
        ('F', 'Fale'),
    ]

    username = models.CharField(max_length=25, unique=False)
    email = models.EmailField(max_length=80, unique=True)
    avatar = models.ImageField(default="no-avatar.jpg", upload_to='user/users', null=True, blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    genre = models.CharField(choices=genre_choice, null=True, blank=True, max_length=4)
    country = models.CharField(max_length=100, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField (default = True)
    is_admin = models.BooleanField (default = False)

    objetos = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def  __str__ (self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
