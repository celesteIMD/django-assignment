from django.urls import path, include
from . import views, admin

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.homePage, name='home'),

    path('newEvidence/', views.create_evidence, name='newEvidence'),
    path('create_evidence/', views.create_evidence, name='create_evidence'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),

    path('newBattle/', views.create_battle, name='newBattle'),
    path('create_battle/', views.create_battle, name='create_battle'),
    path('deletebattle/<int:id>', views.deletebattle, name='deletebattle'),
    path('updatebattle/<int:id>', views.updatebattle, name='updatebattle'),
    path('updatebattle/updatebattlerecord/<int:id>', views.updatebattlerecord, name='updaterecord'),
]