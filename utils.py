from datetime                import datetime
from django.contrib.gis.geos import Point

from areas.models            import ForbiddenArea, ParkingZone, Area
from use.models              import Use

def discount_fee(deer, member, total_fee):
    use            = Use.objects.filter(deer_name=deer, member=member).last()
    arrive_point   = Point((use.end_lat, use.end_lng))
    parking_zone   = ParkingZone.objects.get(area=deer.area)
    parking_point  = Point((parking_zone.center_lat, parking_zone.center_lng))
    parking_circle = parking_point.buffer(parking_zone.radius)
    
    if parking_circle.contains(arrive_point):
        return total_fee * 0.7
       
    return total_fee     

def add_fee(deer, member, total_fee):
    use          = Use.objects.filter(deer_name=deer, member=member).last()
    arrive_point = Point((use.end_lat, use.end_lng))
    surcharge    = 0
    
    forbidden_areas = ForbiddenArea.objects.all()
    
    for forbidden_area in forbidden_areas:
        if forbidden_area.boundary.contains(arrive_point):
            surcharge += 6000
            break
       
    distance = Area.objects.get(deer=deer).boundary.distance(arrive_point) * 8880
    surcharge += 10 * distance
    
    return total_fee + surcharge

def calculate_time(start, end):
    start_time = datetime.strptime(str(start), "%Y-%m-%d %H:%M:%S")
    end_time   = datetime.strptime(str(end), "%Y-%m-%d %H:%M:%S")
    
    return end_time - start_time

def convert_time(time):
    return datetime.strptime(time, "%Y-%m-%d %H:%M:%S")