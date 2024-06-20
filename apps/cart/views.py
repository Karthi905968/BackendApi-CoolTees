from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from ..users.mixens import CustomLoginRequiredMixin
from .models import CartModel
from .serializers import CartSerializer,CartAddSerializer

# Create your views here.

class CartList(CustomLoginRequiredMixin,generics.ListAPIView):
    queryset = CartModel.objects.all()
    serializer_class=CartAddSerializer


    def get(self, request, *args, **kwargs):
        self.queryset = CartModel.objects.order_by('-created_at').filter(user=request.login_user)
        return super().get(request, *args, **kwargs)
    
class CartAdd(CustomLoginRequiredMixin,generics.CreateAPIView):
    queryset=CartModel.objects.all()
    serializer_class=CartAddSerializer

    def post(self, request, *args, **kwargs):
        request.data['user']=request.login_user.id
        return super().post(request, *args, **kwargs)

class CartDelete(CustomLoginRequiredMixin,generics.DestroyAPIView):
    queryset=CartModel.objects.all()
    serializer_class=CartSerializer

    def delete(self, request, *args, **kwargs):
        cart = CartModel.objects.get(pk=self.kwargs['pk'])

        if cart.user.id != request.login_user.id:
            response = Response({'error':'You can not delete the cartlist not owened by you'},status=status.HTTP_404_NOT_FOUND)
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = 'application/json'
            response.renderer_context = {}
            return response
        return super().delete(request, *args, **kwargs)
    

class CartUpdate(CustomLoginRequiredMixin,generics.UpdateAPIView):
    queryset=CartModel.objects.all()
    serializer_class=CartSerializer

    def update(self, request, *args, **kwargs):
        cart = CartModel.objects.get(pk=self.kwargs['pk'])

        if cart.user.id != request.login_user.id:
            response = Response({'error':'You can not update the cart list not owened by you'},status=status.HTTP_404_NOT_FOUND)
            response.accepted_renderer=JSONRenderer()
            response.accepted_media_type = 'application/json'
            response.renderer_context={}
            return response
        
        cart.quantity = request.data['quantity']
        cart.save()
        serializer = CartSerializer([cart],many=True)

        return Response(serializer.data[0])
    

