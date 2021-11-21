import json, jwt, os

from decimal           import Decimal
from django.test       import TestCase, Client
from django.contrib.gis.geos import Polygon

from members.models    import Member
from areas.models      import Area, ParkingZone, ForbiddenArea, RatePlan
from .models           import Use, Deer

client = Client()


class UseViewTest(TestCase):
    def setUp(self):
        Member.objects.create(
            id = 1,
            email = "qhsdnr0@naver.com",
            password = "asdf1234!"
        )
        
        RatePlan.objects.create(
            id = 1,
            basic = 1000,
            per_minute = 100
        )
        
        RatePlan.objects.create(
            id = 2,
            basic = 800,
            per_minute = 90
        )
        
        polygon2 = Polygon(((127.333333, 37.555555), (127.445444, 37.777777), (127.333333, 37.666666), (127.333333, 37.555555)))
        polygon3 = Polygon(((127.555555, 37.777777), (127.666666, 37.666666), (127.555555, 37.444444), (127.555555, 37.777777)))
        
        Area.objects.create(
            id = 1,
            boundary = polygon2,
            center_lat = polygon2.centroid[0],
            center_lng = polygon2.centroid[1],
            coords = polygon2.boundary,
            rate_plan_id = 1
        )
        
        Area.objects.create(
            id = 2,
            boundary = polygon3,
            center_lat = polygon3.centroid[0],
            center_lng = polygon3.centroid[1],
            coords = polygon3.boundary,
            rate_plan_id = 2
        )
        
        ParkingZone.objects.create(
            id = 1,
            center_lat = Decimal("127.333334"),
            center_lng = Decimal("37.562222"),
            radius = Decimal("0.000263063"),
            area_id    = 1
        )
        
        polygon1 = Polygon(((127.4, 37.7), (127.4, 37.733333), (127.395, 37.7), (127.4, 37.7)))
        
        ForbiddenArea.objects.create(
            id = 1,
            boundary = polygon1,
            coords = polygon1.boundary
        )
        
        Deer.objects.create(
            name = "DH1",
            area_id = 1,
        )
        
        Deer.objects.create(
            name = "DH2",
            area_id = 2
        )
        
        Use.objects.create(
            end_lat = 127.333324,
            end_lng = 37.634555,
            start_at = "2021-11-19 20:00:00",
            end_at = "2021-11-19 21:00:30",
            deer_name = Deer.objects.get(name='DH2'),
            member_id = 1
        )

    def tearDown(self):
        Use.objects.all().delete()
        Deer.objects.all().delete()
        Area.objects.all().delete()
        ParkingZone.objects.all().delete()
        ForbiddenArea.objects.all().delete()
        RatePlan.objects.all().delete()
        Member.objects.all().delete()

    def test_use_post_normal(self):
        
        
        headers = {'HTTP_Authorization': jwt.encode({'id' : 1}, os.environ['DEER_SECRET_KEY'], algorithm=os.environ['DEER_ALGORITHM'])}
        
        data = {
            'end_lat'   : 127.333333,
            'end_lng'   : 37.555555,
            'deer_name' : "DH1",
            'start_at'  : "2021-11-20 21:01:00",
            'end_at'    : "2021-11-20 22:01:35",
        }

        response = client.post('/use', json.dumps(data), content_type='application/json', **headers)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {
            'message' : 'CREATED',
            'cost'    : 7000.0
        })

    def test_use_post_parking_zone(self):

        
        headers = {'HTTP_Authorization': jwt.encode({'id' : 1}, os.environ['DEER_SECRET_KEY'], algorithm=os.environ['DEER_ALGORITHM'])}
        
        data = {
            'end_lat'   : 127.333334,
            'end_lng'   : 37.562222,
            'deer_name' : "DH1",
            'start_at'  : "2021-11-20 03:00:00",
            'end_at'    : "2021-11-20 04:00:05",
        }

        response = client.post('/use', json.dumps(data), content_type='application/json', **headers)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {
            'message' : 'CREATED',
            'cost'    : 4900
        })

    def test_use_post_discount_basic(self):
        
        
        headers = {'HTTP_Authorization': jwt.encode({'id' : 1}, os.environ['DEER_SECRET_KEY'], algorithm=os.environ['DEER_ALGORITHM'])}
        
        data = {
            'end_lat'   : 127.333333,
            'end_lng'   : 37.566666,
            'deer_name' : "DH1",
            'start_at'  : "2021-11-19 21:10:00",
            'end_at'    : "2021-11-19 22:10:05",
        }

        response = client.post('/use', json.dumps(data), content_type='application/json', **headers)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {
            'message' : 'CREATED',
            'cost'    : 6000
        })
        
    def test_use_post_add_fee_forbidden_area(self):
        
        
        headers = {'HTTP_Authorization': jwt.encode({'id' : 1}, os.environ['DEER_SECRET_KEY'], algorithm=os.environ['DEER_ALGORITHM'])}
        
        data = {
            'end_lat'   : 127.398,
            'end_lng'   : 37.700001,
            'deer_name' : "DH1",
            'start_at'  : "2021-11-20 21:10:00",
            'end_at'    : "2021-11-20 22:10:05",
        }

        response = client.post('/use', json.dumps(data), content_type='application/json', **headers)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {
            'message' : 'CREATED',
            'cost'    : 13000
        })
        
    def test_use_post_add_fee_range_out_of_area(self):
        
        
        headers = {'HTTP_Authorization': jwt.encode({'id' : 1}, os.environ['DEER_SECRET_KEY'], algorithm=os.environ['DEER_ALGORITHM'])}
        
        data = {
            'end_lat'   : 127.333333,
            'end_lng'   : 37.0,
            'deer_name' : "DH1",
            'start_at'  : "2021-11-20 21:10:00",
            'end_at'    : "2021-11-20 22:10:05",
        }

        response = client.post('/use', json.dumps(data), content_type='application/json', **headers)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {
            'message' : 'CREATED',
            'cost'    : 56330.0
        })
        
    def test_use_post_key_error(self):
        
        
        headers = {'HTTP_Authorization': jwt.encode({'id' : 1}, os.environ['DEER_SECRET_KEY'], algorithm=os.environ['DEER_ALGORITHM'])}
        
        data = {
            'end_lat'   : 127.333333,
            'end_lng'   : 37.0,
            'deer_name' : "DH1",
            'start_at'  : "2021-11-20 21:10:00",
        }

        response = client.post('/use', json.dumps(data), content_type='application/json', **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'message' : 'KEY_ERROR',
        })