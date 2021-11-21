import json, datetime

from django.views   import View
from django.http    import JsonResponse

from .models        import Use, Deer
from members.utils  import login_decorator
from utils          import add_fee, discount_fee, calculate_time, convert_time

class UseView(View):
    @login_decorator
    def post(self, request):
        try:
            data      = json.loads(request.body)
            
            deer_name = data['deer_name']
            member    = request.member
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
            
            if use_time <= datetime.timedelta(seconds=60):
                return JsonResponse({'message' : 'CREATED', 'cost' : 0}, status = 201)
            
            total_fee = rate_plan.basic + (use_time.seconds // 60) * rate_plan.per_minute
            use_list = Use.objects.filter(member=member, end_at__gte=convert_time(use.start_at) - datetime.timedelta(seconds=1800))
            
            if use_list.exclude(id=use.id).exists():
                total_fee = (use_time.seconds // 60) * rate_plan.per_minute
            
            adjusted_fee = add_fee(deer, member, discount_fee(deer, member, total_fee))
            
            return JsonResponse({'message' : 'CREATED', 'cost' : round(adjusted_fee, -1)}, status = 201)
            
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)