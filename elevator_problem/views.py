from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Elevator, ElevatorRequest
from .serializers import ElevatorSerializer, ElevatorRequestSerializer
import traceback

class ElevatorViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            queryset = Elevator.objects.all()
            serializer = ElevatorSerializer(queryset, many=True)
            print(serializer)
            return Response({'success':True, 'data': serializer.data})
        except Exception as e:
            return Response({'success':False, 'message':f'ERROR: {str(e)}'})
    
    def partial_update(self, request, pk=None):
        try:
            if pk is None:
                raise Exception("Elevator id is mandatory")
            
            try:
                elevator = Elevator.objects.get(id = pk)
            except Elevator.DoesNotExist:
                raise Exception(f"Elivator with id {pk} does not exist")
            
            serializer = ElevatorSerializer(elevator, data=request.data, partial = True)
            if serializer.is_valid():
                print(serializer.validated_data)
                serializer.save()
                elevator.save()
            print(serializer.data)
            return Response({'success':True, 'message':'call added successfuly', 'data': serializer.data})
        except Exception as e:
            traceback.print_exc()
            return Response({'success':False, 'message':f'ERROR: {str(e)}'})
        
    @action(detail=True, methods=['get'])
    def status(self, request, pk=None):
        print(pk)
        elevator = Elevator.objects.get(id = pk)
        serialize = ElevatorSerializer(elevator)
        print(serialize.data)
        # Fetch elevator's current floor, state, and operational status
        # Return elevator status

        return Response({'success':True,'message': f'Status of Elevator {pk}','data': {'status': serialize.data['state']}})
    
    @action(detail=False, methods=['post'])
    def initiate(self, request):
        try:
            elevator = Elevator()
            try:
                num = request.data['num']
            except Exception as e:
                raise Exception("Number of elevators is mandatory")
            
            try:
                num = int(num)
            except Exception as e:
                raise Exception(f"num of elevators should be of type int recieved {type(num)}")
            
            Elevator.objects.bulk_create([elevator for _ in range(num)])
            return Response({'success':False,'message':f'{num} elevators initialised'})
        except Exception as e:
            return Response({'success':False,'message' : f'ERROR: {str(e)}'})
        
    
class ElevatorRequestViewSet(viewsets.ViewSet):

    def create(self, request):
        try:
            print("in here")
            print(request.data)
            serializer = ElevatorRequestSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                print(serializer.data)
                return Response(serializer.data)
            else:
                print(serializer.error_messages())
        except Exception as e:
            return Response({'success':False, 'message':f'ERROR: {str(e)}'})
    
    
    def list(self, request):
        try:
            queryset = ElevatorRequest.objects.all()
            serializer = ElevatorRequestSerializer(queryset, many=True)
            print(serializer)
            return Response({'success':True, 'data': serializer.data})
        except Exception as e:
            return Response({'success':False, 'message':f'ERROR: {str(e)}'})