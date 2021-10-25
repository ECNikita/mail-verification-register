from django.shortcuts import render
from datetime import *
import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import calendar


@api_view(['GET'])
def get_chart_data(request):
    if request.method == 'GET':
        datalist = []
        Sdate = datetime.strptime("2021-01-01", "%Y-%m-%d")
        for x in range(0, 50):
            t = calendar.timegm(Sdate.timetuple()) * 1000
            data = [t, random.randrange(50, 100)]
            print(calendar.timegm(Sdate.timetuple()))
            datalist.append(data)
            Sdate = Sdate + timedelta(days=1)
        return JsonResponse(datalist, safe=False)


def view_chart(request):
    return render(request, 'chart_demo.html')
from django.shortcuts import render

