from django.test import TestCase
from django.contrib.auth import get_user_model

# TDD: test driven development
class UserTestCase(TestCase):
    # user test
    def test_create_user(self):
        email = 'abc@gmail.con'
        password = 'password123'

        user = get_user_model().objects.create_user(email= email, password = password)
        # 유저가 정상적으로 만들어졌는지 확인
        self.assertEqual(user.email, email)
        # self.assertEqal(user.check_password(password), True)
        self.assertTrue(user.check_password(password))
        # self.assertEqual(user.is_superuser, False)
        self.assertFalse(user.is_superuser)

    # run test
    # docker-compose run --rm app sh -c 'python manage.py test users'
    
    # error: Migration admin.0001_initial is applied before its dependency users.0001_initial on database 'default'.
    # docker-compose run --rm app sh -c 'python manage.py showmigrations' 
    # app settings.py urls.py에서 admin 주석처리 후 python manage.pu migrate 수행 -> 주석 처리 해제 후 다시 python manage.pu migrate 수행  

    # superuser test
    def test_create_superuser(self):
        email = 'super@gmail.com'
        password = 'admin123'

        user = get_user_model().objects.create_superuser(
            email = email,
            password = password
        )

        # 슈퍼유저
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)