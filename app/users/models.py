from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
    # 일반유저 생성
    def create_user(self, email, password):
        if not email:
            raise ValueError("Please enter your email address.")
        
        user = self.model(email = email)
        user.set_password(password) # set_password: hashed password
        user.save(using = self._db) # save in db

        return user

    # 슈퍼유저
    def create_superuser(self, email, password):
        # 일반유저 생성후에 관리자 권한 부여
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True

        user.save()

        return user


# createsuperuser -> email, username(required), password(required)
class User(AbstractBaseUser,  PermissionsMixin):
    # CharField -> Varchar(255)
    email = models.CharField(max_length = 255, unique = True)
    nickname = models.CharField(max_length = 255)
    is_business = models.BooleanField(default = False)

    # distinguish SuperUser and GeneralUser : PermissionMixin (manage access autority) 
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    # username 필드를 email로 대신하겠다는 명령
    USERNAME_FIELD = 'email'
    
    objects = UserManager() # create and manage user (admin user, general user)

    def __str__(self):
        return f'email: {self.email}, nickname: {self.nickname}'

