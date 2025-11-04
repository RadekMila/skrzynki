from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'characters', views.CharacterViewSet)
router.register(r'monsters', views.MonsterViewSet)
router.register(r'items', views.ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('play-json/<int:character_id>/', views.play_game_api, name="play_game_api"),
    path('play/<int:character_id>/', views.play_page, name="play_page"),
]
