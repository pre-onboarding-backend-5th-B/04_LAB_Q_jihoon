import requests
import os
import datetime

from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from apiserver.models import SeoulGu
from apiserver.models import DrainLocation
from apiserver.models import RainLocation
from apiserver.serializers import SeoulGuSerializer

API_KEY = os.environ.get("API_KEY")


class GuInfoApiView(APIView):
    # 조회가능한 옵션(구별 id로 검색)조회

    def get(self, request):
        seoul_gu = SeoulGu.objects.all()
        return Response(
            SeoulGuSerializer(seoul_gu, many=True).data, status=status.HTTP_200_OK
        )


class GuInfoDetailApiView(APIView):
    # 해당 구청의 하수관 수위, 강우량을 관측소별로 최신값을 조회

    def get(self, request, gu_id):
        gu_obj = SeoulGu.objects.get(id=gu_id)
        drain_gu_num = gu_obj.drain_gu_code  # 하수관 수위는 구청식별코드로 조회
        rain_gu_name = gu_obj.name  # 강우량은 구청명으로 조회

        drain_location = DrainLocation.objects.filter(gu=gu_id)
        drain_location_num = len(drain_location)  # 해당 구의 하수도 수위 관측소 갯수
        rain_location = RainLocation.objects.filter(gu=gu_id)
        rain_location_num = len(rain_location)  # 해당 구의 강우량 관측소 갯수

        r_url = f"http://openapi.seoul.go.kr:8088/{API_KEY}/json/ListRainfallService/1/{rain_location_num}/{rain_gu_name}"
        r_response = requests.get(r_url)
        r_response_data = r_response.json()
        rain_info = r_response_data["ListRainfallService"]
        rain_data = rain_info["row"]

        if len(drain_gu_num) == 1:
            drain_gu_num = (
                "0" + drain_gu_num
            )  # 하수관 수위 openAPI에서 해당 구청식별 코드가 한자리 수 일때 01, 02 식으로 입력받기에 문자열 "0" 추가

        time_now = datetime.datetime.today()
        hour_before = time_now - datetime.timedelta(hours=1)

        insert_time = time_now.strftime("%Y%m%d%H")
        b_insert_time = hour_before.strftime("%Y%m%d%H")

        d_url = f"http://openapi.seoul.go.kr:8088/{API_KEY}/json/DrainpipeMonitoringInfo/1/1000/{drain_gu_num}/{insert_time}/{insert_time}"
        d_response = requests.get(d_url)
        d_response_data = d_response.json()
        
        try:
            drain_info = d_response_data["DrainpipeMonitoringInfo"]

        except KeyError: # 시간단위가 바뀌면 하수관수위 데이터가 바로 갱신되지 않기 때문에 한시간 전으로 조회
            d_url = f"http://openapi.seoul.go.kr:8088/{API_KEY}/json/DrainpipeMonitoringInfo/1/1000/{drain_gu_num}/{b_insert_time}/{b_insert_time}"
            d_response = requests.get(d_url)
            d_response_data = d_response.json()
            drain_info = d_response_data["DrainpipeMonitoringInfo"]
        drain_row_count = drain_info["list_total_count"]  # 해당 시간대의 총 데이터 갯수
        drain_data = drain_info["row"]  # 리스트

        target_data_index = (
            drain_row_count - drain_location_num
        )  # 요청받은 데이터중 가장 최신의 데이터 시작 인덱스

        return Response(
            {
                "gu_data": SeoulGuSerializer(gu_obj).data,
                "drain_data": drain_data[target_data_index:drain_row_count],
                "rain_data": rain_data,
            },
            status=status.HTTP_200_OK,
        )
