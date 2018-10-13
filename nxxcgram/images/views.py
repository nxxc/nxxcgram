from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . import models, serializers


class Feed(APIView):

    def get(self, request, format=None):

        user = request.user

        following_users = user.following.all()

        image_list = []

        for following_users in following_users:  # for following_users in following_users: 에서 첫번쨰 following_user는 그냥 변수

            user_images = following_users.images.all()[:2]  # 최근생성된 2개의 이미지까지만 저장

            for image in user_images:

                image_list.append(image)

        sorted_list = sorted(image_list, key=lambda image: image.created_at, reverse=True)  # 이미지를 생성날짜기준으로 정렬

        print(sorted_list)
        serializer = serializers.ImageSerializer(sorted_list, many=True)

        return Response(serializer.data)


class LikeImage(APIView):

    def get(self, request, image_id, format=None):

        user = request.user

        try:
            found_image = models.Image.objects.get(id=image_id)

        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # try -> 먼저 이미지를 찾는다 있으면 try에서 빠져나와 맨 밑에 HTTP_201_CREATED 리턴
        # except 이미지가 없으면 http status 404-> not found 를 리턴

        try:
            preexisting_like = models.Like.objects.get(
                creator=user,
                image=found_image
            )
            preexisting_like.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except models.Like.DoesNotExist:

            new_like = models.Like.objects.create(
                creator=user,
                image=found_image
            )

            # new_like.save()

        # try -> 좋아요가 있는지 찾고 preexisting_like.delete()를 이용해서 좋아요를 지우고 HTTP_204_NO_CONTENT리턴행
        # except -> 없으면 new_like = models.Like.objects.create()를 이용해서 좋아요 만들고 빠져나와 밑에 return Response(status=status.HTTP_201_CREATED) 실행

        return Response(status=status.HTTP_201_CREATED)


class CommentOnImage(APIView):

    def post(self, request, image_id, format=None):

        user = request.user                                         #Comment를 작성하는 유저는 HTTP에 요청을 하는 유저 

        try:
            found_image = models.Image.objects.get(id=image_id) 
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.CommnetSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(creator=user, image=found_image)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        else:

            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
