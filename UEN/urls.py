"""
URL configuration for UEN project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from user.views import (UserViewSet, OrganizationViewSet, 
                        SellerViewSet, VolonteerViewSet)
from posts.views import (PostViewSet, PostLikeViewSet, FavouriteViewSet,
                         CommentViewSet, CommentLikeViewSet, CommentAnswerViewSet,
                         CommentAnswerLikeViewSet)


router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'volonteer', VolonteerViewSet)
router.register(r'orgnanization', OrganizationViewSet)
router.register(r'seller', SellerViewSet)
router.register(r'post', PostViewSet)
router.register(r'post_like', PostLikeViewSet)
router.register(r'favourite', FavouriteViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'comment_like', CommentLikeViewSet)
router.register(r'comment_answer', CommentAnswerViewSet)
router.register(r'comment_answer_like', CommentAnswerLikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path("admin/", admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
