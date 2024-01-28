"""
URL configuration for advertising_portal project.

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
import users.views as user_views
import main.views as main_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'), name = 'main'),
    # main site urls
    path('main/', include('main.urls')),
    path('main/user_offerts/', main_views.get_user_offerts),
    path('main/add_offert/', main_views.add_offert),
    path('main/edit_offert/<offert_id>/', main_views.edit_offert, name='edit_offert'),
    path('main/delete_offert/<offert_id>/', main_views.delete_offert, name='delete_offert'),
    path('main/offert_details/<offert_id>/', main_views.offert_details, name='offert_details'),
    path('main/user_offert_detail/<offert_id>', main_views.user_offert_detail, name='user_offert_detail'),
    # user urls
    path('user/signup/', user_views.signup, name='login'),
    path('user/logout/', user_views.signout, name='logout'),
    path('user/signin/', user_views.signin, name='signin'),
    path('user/update_profile/', user_views.edit_user_profile),
    path('user/password/', user_views.change_password),
    #path('user/password_change_done/', user_views.password_change_done, name='password_change_done')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)