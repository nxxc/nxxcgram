from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'images'
urlpatterns = [
    path('', view=views.Images.as_view(), name='images'),
    path('search/', view=views.Search.as_view(), name='search'),
    path('<image_id>/', view=views.ImageDetail.as_view(), name='image_detail'),
    path('<image_id>/likes/', view=views.LikeImage.as_view(), name='like_image'),
    path('<image_id>/unlikes/', view=views.UnLikeImage.as_view(), name='unlike_image'),
    path('<image_id>/comments/', view=views.CommentOnImage.as_view(), name='comment_image'),
    path('comments/<comment_id>/', view=views.Comment.as_view(), name='comment'),
    path('<image_id>/comments/<comment_id>/', view=views.ModerateComments.as_view(), name='moderate_comments'),
    
]
