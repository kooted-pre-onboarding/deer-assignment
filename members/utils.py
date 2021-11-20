import jwt

from django.http    import JsonResponse

from members.models import Member
from deer.settings  import SECRET_KEY

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token   = request.headers.get('Authorization', None)
            payload        = jwt.decode(access_token, SECRET_KEY, algorithms='HS256')
            member         = Member.objects.get(id=payload['id'])
            request.member = member
            
        except jwt.DecodeError:
            return JsonResponse({'MESSAGE' : 'INVALID_TOKEN'}, status=400)
            
        except Member.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'INVALID_MEMBER'}, status=400)
        
        return func(self, request, *args, **kwargs)
    
    return wrapper