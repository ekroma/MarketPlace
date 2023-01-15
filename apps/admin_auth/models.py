from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class AdminManager(BaseUserManager):
    def _create(self, admin_name, email, password, **extra_fields):
        if not admin_name:
            raise ValueError('Admin must have name')
        if not email:
            raise ValueError('Admin must have email')
        user = self.model(
            admin_name=admin_name,
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, admin_name, email, password, **extra_fields):
        return self._create(admin_name, email, password, **extra_fields)

class Admin(AbstractBaseUser):
    admin_name = models.CharField('Admin', max_length=50, primary_key=True)
    email = models.EmailField('Email', max_length=255, unique=True)
    objects = AdminManager()
    is_staff = models.BooleanField(default=True)
    USERNAME_FIELD = 'admin_name'
    REQUIRED_FIELDS = ['email']
    

    def __str__(self) -> str:
        return self.admin_name

    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, obj=None):
        return self.is_staff


    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'

