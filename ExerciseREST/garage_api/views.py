from django.db.models.aggregates import Count, Min, Max
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Manufacturer, Car
from .serializers import ManufacturerSerializer, ManufacturerModelSerializer, CarModelSerializer
from rest_framework.generics import get_object_or_404


"""
    ListCreateAPIView will enable the listing and creating of objects, 
    overriding the get() and post() methods.
"""

class ListCreateAPIManufacturerView(APIView):
    def get(self, request: Request) -> Response:
        manufacturers = Manufacturer.objects.all()
        serializer = ManufacturerSerializer(manufacturers, many=True)
        return Response({'manufacturers': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = ManufacturerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'manufacturer': serializer.data}, status=status.HTTP_201_CREATED)


"""
    DetailAPIView will enable the retrieving, updating (completely and partially) 
    and deleting of objects, overriding the get(), put(), patch() and delete() methods.
"""

class DetailAPIManufacturerView(APIView):
    def get_object(self, pk: int) -> 'Manufacturer':
        return get_object_or_404(Manufacturer, pk=pk)

    def get(self, request: Request, pk: int) -> Response:
        manufacturer = self.get_object(pk)
        serializer = ManufacturerModelSerializer(manufacturer)
        return Response({"manufacturer": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int) -> Response:
        manufacturer = self.get_object(pk)
        serializer = ManufacturerModelSerializer(manufacturer, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"manufacturer": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request: Request, pk: int) -> Response:
        manufacturer = self.get_object(pk)
        serializer = ManufacturerModelSerializer(manufacturer, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"manufacturer": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request: Request, pk: int) -> Response:
        manufacturer = self.get_object(pk)
        manufacturer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListCreateAPICarView(APIView):
    def get(self, request: Request) -> Response:
        cars = Car.objects.all()
        serializer = CarModelSerializer(cars, many=True)
        return Response({"cars": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = CarModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"car": serializer.data}, status=status.HTTP_201_CREATED)


class DetailAPICarView(APIView):
    def get_object(self, pk: int) -> 'Car':
        return get_object_or_404(Car, pk=pk)

    def get(self, request: Request, pk: int) -> Response:
        car = self.get_object(pk)
        serializer = CarModelSerializer(car)
        return Response({"car": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int) -> Response:
        car = self.get_object(pk)
        serializer = CarModelSerializer(car, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"car": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request: Request, pk: int) -> Response:
        car = self.get_object(pk)
        serializer = CarModelSerializer(car, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"car": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request: Request, pk: int) -> Response:
        car = self.get_object(pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CarStatsAPIView(APIView):
    def get(self, request: Request) -> Response:
        stats = Car.objects.aggregate(
            total_cars=Count('id'),
            oldest_year=Min('year'),
            newest_year=Max('year'),
        )

        return Response({"stats": stats}, status=status.HTTP_200_OK)



class ListCreatePartAPIView(APIView):
    ...


class DetailPartAPIView(APIView):
    ...