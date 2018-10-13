from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . import models, serializers


class Feed(APIView):

    def get(self, request, format=None):

        user = request.user

        following_users = user.following.all()

        image_list = []

        for following_users in following_users:  # for following_users in following_users -> first "following_users"is  just variable

            user_images = following_users.images.all()[:2]  # images that is crated recently

            for image in user_images:

                image_list.append(image)

        sorted_list = sorted(image_list, key=lambda image: image.created_at, reverse=True)

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

        # try -> if the image has 'like' , run "return Response(status=status.HTTP_201_CREATED)" or run except ""

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

        # try -> Find preexisting_like on image -> if there is 'like' on image -> use preexisting_like.delete () to remove 'like' and return HTTP_204_NO_CONTENT
        # except -> if there is no 'like' on image-> use models.Like.objects.create() to make 'like' -> return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_201_CREATED)


class CommentOnImage(APIView):

    def post(self, request, image_id, format=None):

        user = request.user  # the user who write a comment is user who request to HTTP
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


class Comment(APIView):

    def delete(self, request, comment_id, format=None):

        user = request.user

        try:
            comment = models.Comment.objects.get(id=comment_id, creator=user)
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except models.Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

 