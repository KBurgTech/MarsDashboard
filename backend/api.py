import datetime

from django.http import HttpResponse, JsonResponse
from django.views import View

from backend import faker


def sleep_api():
    sleep = faker.fake_sleep()
    interruptions = faker.fake_average_sleep_interruptions()
    labels = [(datetime.datetime.now() - datetime.timedelta(days=i)).strftime("%d.%m.%Y") for i in
              range(len(sleep))]
    labels.reverse()
    return {
        "labels": labels,
        "datasets": [
            {
                "type": 'line',
                "label": 'Hours of Sleep',
                "data": sleep,
                "yAxisID": 'hours',
                "borderColor": '#fca503'
            },
            {
                "type": 'bar',
                "label": 'Interruptions',
                "data": interruptions,
                "yAxisID": 'interruptions',
                "borderColor": '#b8000f',
                "backgroundColor": '#6b0009'

            }
        ]
    }


class SleepDataApi(View):

    def get(self, request, *args, **kwargs):
        return JsonResponse(sleep_api())


def hearbeat_api():
    heartbeat = faker.fake_heartbeat()
    labels = [(datetime.datetime.now() - datetime.timedelta(minutes=i)).strftime("%H:%M") for i in
              range(len(heartbeat))]
    labels.reverse()
    return {
        "labels": labels,
        "datasets": [{
            "label": 'Heartbeat',
            "data": heartbeat
        }]
    }


class HeartRateApi(View):

    def get(self, request, *args, **kwargs):
        return JsonResponse(hearbeat_api())
