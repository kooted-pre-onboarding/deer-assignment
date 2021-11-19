import json
from datetime       import datetime, timedelta

from django.views   import View
from django.http    import JsonResponse

from members.models import Member

from .models        import Use, Deer
from utils          import *

class UseView(View):
    def post(self, request):
        try:
            data      = json.loads(request.body)
            
            end_lat   = data['end_lat']
            end_lng   = data['end_lng']
            deer_name = data['deer_name']
            member    = Member.objects.get(id=data["member"])
            deer      = Deer.objects.select_related('area').get(name=deer_name)
            rate_plan = deer.area.rate_plan
            
            if Use.objects.filter(start_at = data['start_at'], member = member):
                return JsonResponse({'message' : 'INVALID_ACCESS'}, status = 400)
            
            use = Use.objects.create(
                end_lat   = data['end_lat'],
                end_lng   = data['end_lng'],
                start_at  = data['start_at'],
                end_at    = data['end_at'],
                deer_name = deer,
                member    = member
            )
            
            use_time = calculate_time(use.start_at, use.end_at)
            
            if use_time <= timedelta(seconds=60):
                return JsonResponse({'message' : 'CREATED', 'cost' : 0}, status = 201)
            
            total_fee = rate_plan.basic + ((use_time.seconds // 60 )) * rate_plan.per_minute
            
            if Use.objects.filter(member=member, end_at__lte=convert_time(use.start_at) - timedelta(seconds=1800)).exists():
                total_fee = ((use_time.seconds // 60 )) * rate_plan.per_minute
            
            adjusted_fee = add_fee(deer, member, discount_fee(deer, member, total_fee))
            
            return JsonResponse({'message' : 'CREATED', 'cost' : adjusted_fee}, status = 201)
            
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)