from django.contrib.gis.db import models

from core.models           import TimeStampModel

class Area(TimeStampModel):
    boundary   = models.PolygonField()
    center_lat = models.DecimalField(max_digits=30, decimal_places=20)
    center_lng = models.DecimalField(max_digits=30, decimal_places=20)
    coords     = models.LineStringField()
    rate_plan  = models.ForeignKey('RatePlan', null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'areas'

class ParkingZone(TimeStampModel):
    center_lat = models.DecimalField(max_digits=30, decimal_places=20)
    center_lng = models.DecimalField(max_digits=30, decimal_places=20)
    radius     = models.DecimalField(max_digits=30, decimal_places=20)
    area       = models.ForeignKey(Area, on_delete=models.CASCADE)

    class Meta:
        db_table = 'parking_zones'
        
class ForbiddenArea(TimeStampModel):
    boundary = models.PolygonField()
    coords   = models.LineStringField()

    class Meta:
        db_table = 'forbidden_areas'
        
class RatePlan(TimeStampModel):
    basic      = models.PositiveIntegerField()
    per_minute = models.PositiveIntegerField()
    
    class Meta:
        db_table = 'rate_plans'