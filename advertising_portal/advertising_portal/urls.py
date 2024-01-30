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
    path('main/save_opinion', main_views.save_opinion, name='save_opinion'),
    # reservation urls
    path('main/make_reservation/<offert_id>/', main_views.make_reservation, name='make_reservation'),
    path('main/user_reservations/', main_views.user_reservations, name='user_reservations'),
    path('main/client_reservations/', main_views.client_reservations, name= 'client_reservations'),
    path('main/accept_reservation/<reservation_id>', main_views.accept_reservation, name='accept_reservation'),
    path('main/reject_reservation/<reservation_id>', main_views.reject_reservation, name='reject_reservation'),
    path('main/delait_reservation/<reservation_id>', main_views.delait_reservation, name='delait_reservation'),
    path('main/contact_info_user/<user_id>', main_views.contact_info_user, name='contact_info_user'),
    path('main/contact_info_client/<user_id>', main_views.contact_info_client, name='contact_info_client'),
    # user urls
    path('user/signup/', user_views.signup, name='login'),
    path('user/logout/', user_views.signout, name='logout'),
    path('user/signin/', user_views.signin, name='signin'),
    path('user/update_profile/', user_views.edit_user_profile),
    path('user/password/', user_views.change_password),
    #path('user/password_change_done/', user_views.password_change_done, name='password_change_done')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)