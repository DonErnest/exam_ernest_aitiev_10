from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import json
from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView

from api_v1.serializers import UserSerializer
from webapp.models import SharedFile


class UserProvideAccessView(APIView):
    def patch(self, request, pk):
        file_id = self.kwargs['pk']
        file = get_object_or_404(SharedFile, pk=file_id)

        user_name = request.data['user_name'].strip()
        try:
            user = User.objects.get(username=user_name)
            if user in file.privately_accessed.all():
                return JsonResponse({'message': 'Пользователь уже добавлен'}, status=400)

            file.privately_accessed.add(user)

            serializer = UserSerializer(user)
            return JsonResponse(data=serializer.data)
        except ObjectDoesNotExist:
            print('I am here ')
            return JsonResponse({'message': 'Пользователь не найден'}, status=404)


class DepriveUserAccessView(APIView):
    def patch(self, request, pk):
        file_id = self.kwargs['pk']
        file = get_object_or_404(SharedFile, pk=file_id)

        serializer = UserSerializer(data=request.data, partial=True)

        if serializer.is_valid():
            user_id = request.data['id']
            user = get_object_or_404(User, pk=user_id)
            file.privately_accessed.remove(user)
        return JsonResponse(data=request.data)


class DownloadCounterIncrement(APIView):
    def patch(self, request, pk):
        file_id = self.kwargs['pk']
        file = get_object_or_404(SharedFile, pk=file_id)

        file.downloaded_count += 1
        file.save()

        return JsonResponse(data=request.data)