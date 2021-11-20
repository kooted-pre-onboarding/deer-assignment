import json, re, jwt, bcrypt
from json.decoder import JSONDecodeError

from django.http    import JsonResponse
from django.views   import View

from members.models import Member
from deer.settings  import SECRET_KEY

class SignUpView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            if Member.objects.filter(email=email).exists():
                return JsonResponse({'message': 'EMAIL_ALREADY_EXIST'}, status=400)

            if not re.match(r"^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
                return JsonResponse({'message': 'INVALID_EMAIL'}, status=404)
            
            if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$", password):
                return JsonResponse({'message': 'INVALID_PASSWORD'}, status=404)

            Member.objects.create(
                email    = email,
                password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
            )
            return JsonResponse({'message': 'SUCCESS'}, status=201)
            
        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

class SignInView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            if not Member.objects.filter(email=email).exists():
                return JsonResponse({'message': 'INVALID_EMAIL'}, status=401)
            
            member = Member.objects.get(email=email)

            if not bcrypt.checkpw(password.encode('utf-8'), member.password.encode('utf-8')):
                return JsonResponse({'message': 'INVALID_PASSWORD'}, status=401)
            
            token = jwt.encode({'id': member.id}, SECRET_KEY, algorithm='HS256')
            return JsonResponse({'token':token}, status=200)

        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)