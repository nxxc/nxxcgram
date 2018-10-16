from django.urls import path
from . import views

app_name = 'images'
urlpatterns = [
    path('', view=views.Feed.as_view(), name='feed'),
    path('<image_id>/likes/', view=views.LikeImage.as_view(), name='like_image'),
    path('<image_id>/unlikes/', view=views.UnLikeImage.as_view(), name='unlike_image'),
    path('<image_id>/comments/', view=views.CommentOnImage.as_view(), name='comment_image'),
    path('comments/<comment_id>/', view=views.Comment.as_view(), name='comment'),
    path('search/', view=views.Search.as_view(), name='search'),
    path('<image_id>/comments/<comment_id>/', view=views.ModerateComments.as_view(), name='moderate_comments'),
]
