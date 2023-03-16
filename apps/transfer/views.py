#rest
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import  CreateAPIView

#my imports
from .serializers import HistoryTransfer,HistoryTransferSerializer
from apps.transfer.models import User
# Create your views here.
class CreateTransferView(CreateAPIView):
    serializer_class = HistoryTransferSerializer
    def post(self, request):
        from_user_id = request.data.get('from_user')
        to_user_id = request.data.get('to_user')
        amount = request.data.get('amount')
        try:
            from_user = User.objects.get(id=from_user_id)
            to_user = User.objects.get(id=to_user_id)
            if float(amount) > float(from_user.balance):
                return Response({'detail': 'Недостаточно средств для перевода'}, status=status.HTTP_400_BAD_REQUEST)
            from_user.balance = float(from_user.balance) - float(amount)
            to_user.balance = float(to_user.balance) + float(amount)
            from_user.save()
            to_user.save()
            transfer = HistoryTransfer.objects.create(from_user=from_user, to_user=to_user, amount=amount)
            serializer = HistoryTransferSerializer(transfer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({'detail': 'Пользователь не найден'}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({'detail': 'Неверный формат суммы перевода'}, status=status.HTTP_400_BAD_REQUEST)

