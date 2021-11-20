import jwt, bcrypt

from django.test    import TestCase, Client

from deer.settings  import SECRET_KEY
from members.models import Member

class SingUpTest(TestCase):
    def setUp(self):
        password = 'Test12345!@'
        member   = Member.objects.create(
            id       = 1,
            email    = 'member1@sample.com',
            password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        )
                
    def tearDown(self):
        Member.objects.all().delete()
    
    def test_sign_up_post_success(self):
        client = Client()
        data   = {
            'email'    : 'member2@sample.com',
            'password' : 'TestTest12!@'
        }
        response = client.post('/members/signup', data=data, content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'message':'SUCCESS'})
        
    def test_sign_up_post_email_duplicated_fail(self):
        client = Client()
        data   = {
            'email'    : 'member1@sample.com',
            'password' : 'Test12345!@'
        }
        response = client.post('/members/signup', data=data, content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message':'EMAIL_ALREADY_EXIST'})
        
    def test_sign_up_post_invalid_email_fail(self):
        client = Client()
        data   = {
            'email'    : 'member1.com',
            'password' : 'Test12345!@'
        }
        response = client.post('/members/signup', data=data, content_type='application/json')

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {'message':'INVALID_EMAIL'})

    def test_sign_up_post_invalid_password_fail(self):
        client = Client()
        data   = {
            'email'    : 'newmember@sample.com',
            'password' : 'wrongpassword'
        }
        response = client.post('/members/signup', data=data, content_type='application/json')

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {'message':'INVALID_PASSWORD'})

    def test_sign_up_post_key_error_fail(self):
        client = Client()
        data   = {
            'password' : 'wrongpassword'
        }
        response = client.post('/members/signup', data=data, content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message':'KEY_ERROR'})

class SingInTest(TestCase):
    def setUp(self):
        password = 'Test12345!@'
        member   = Member.objects.create(
            id       = 1,
            email    = 'member1@sample.com',
            password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        )
        global token
        token = jwt.encode({'id':member.id}, SECRET_KEY, algorithm='HS256')


    def tearDown(self):
        Member.objects.all().delete()
    
    def test_sign_in_post_success(self):
        client = Client()
        data   = {
            'email'    : 'member1@sample.com',
            'password' : 'Test12345!@'
        }
        response = client.post('/members/signin', data=data, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'token' : token})


    def test_log_in_post_invalid_email_fail(self):
        client = Client()
        data   = {
            'email'    : 'wrong@wrong.com',
            'password' : 'Test12345!@'
        }
        response = client.post('/members/signin', data=data, content_type='application/json')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(),{'message':'INVALID_EMAIL'})

    def test_log_in_post_invalid_password_fail(self):
        client = Client()
        data   = {
            'email'    : 'member1@sample.com',
            'password' : 'wrong!!!'
        }
        response = client.post('/members/signin', data=data, content_type='application/json')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(),{'message':'INVALID_PASSWORD'})

    def test_log_in_post_key_error_fail(self):
        client = Client()
        data   = {
            'password' : 'Test12345!@'
        }
        response = client.post('/members/signin', data=data, content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),{'message':'KEY_ERROR'})