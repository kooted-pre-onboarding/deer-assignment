from django.db      import models

from core.models    import TimeStampModel
from members.models import Member
from areas.models   import Area

class Deer(TimeStampModel):
    name = models.CharField(max_length=50, primary_key=True)
    area = models.ForeignKey(Area, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'deers'

class Use(models.Model):
    end_lat   = models.DecimalField(max_digits=30, decimal_places=20)
    end_lng   = models.DecimalField(max_digits=30, decimal_places=20)
    start_at  = models.DateTimeField()
    end_at    = models.DateTimeField()
    deer_name = models.ForeignKey(Deer, on_delete=models.CASCADE)
    member    = models.ForeignKey(Member, on_delete=models.CASCADE)

    class Meta:
        db_table = 'use'