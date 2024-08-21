from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import User
from .serializers import UserDetailSerializer
from property.serializers import ReservationsListSerializer
from django.contrib.auth import get_user_model

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def landlord_detail(request, pk):
    user = User.objects.get(pk=pk)
    serializer = UserDetailSerializer(user, many=False)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def reservations_list(request):
    reservations = request.user.reservations.all()
    serializer = ReservationsListSerializer(reservations, many=True)
    return JsonResponse(serializer.data, safe=False)

# Add the temporary superuser creation view
def create_superuser(request):
    User = get_user_model()
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("testadmin", "admintest@example.com", "testadminpassword123")
        return HttpResponse("Superuser created successfully!", status=200)
    else:
        return HttpResponse("Superuser already exists.", status=400)


