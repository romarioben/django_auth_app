from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name="login"),
    path('logout/', views.MyLogoutView.as_view(), name="logout"),
    path('password-change/', views.MyPasswordChangeView.as_view(), name="password-change"),
    path('password_change/done/', views.MyPasswordChangeDoneView.as_view(), name="login"),
    path('password_reset/', views.MyPasswordResetView.as_view(), name="login"),
    path('password_reset/done/', views.MyPasswordResetDoneView.as_view(), name="login"),
    path('reset/<uidb64>/<token>/', views.MyPasswordResetConfirmView.as_view(), name="login"),
    path('reset/done/', views.MyPasswordResetConfirmView.as_view(), name="login"),
]






# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']