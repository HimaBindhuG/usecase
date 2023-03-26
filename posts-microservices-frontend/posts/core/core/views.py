from rest_framework.views import APIView
from .models import Post

class PostAPIView(APIView):
    def get(self,request):
        posts = Post.objects.all()
        serializers =Post