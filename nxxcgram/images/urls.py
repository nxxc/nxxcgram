from django.urls import path
from . import views

app_name = "images"
urlpatterns = [
    path("", view=views.Feed.as_view(), name="feed"),
    path("<image_id>/likes/", view=views.LikeImage.as_view(), name="like_image"),
    path("<image_id>/comments/", view=views.CommentOnImage.as_view(), name="comment_image"),
    path("comments/<comment_id>/", view=views.Comment.as_view(), name="comment")
]


# /images/3/like
# 0 create the url and the view
# 1 take the id from the url
# 2 we want to find an image with this id
# 3 we want to create a like for that image
