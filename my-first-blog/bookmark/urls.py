from django.conf.urls import url
from . import views
from django.conf.urls import include

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^logedin$', views.logedin, name='logedin'),
    url(r'^verify$', views.verify, name='verify'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^getting-started$',views.getting_started, name='getting-started'),
    url(r'^contact$',views.contact, name='contact'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signin$', views.signin, name='signin'),
    url(r'^add$', views.add, name='add'),
    url(r'^user$', views.user, name='user'),
    url(r'^validate_username$', views.validate_username, name='validate_username'),
    url(r'^welcome$', views.welcome ,name='welcome'),
    url(r'^add_get$', views.add_get, name='add_get'),
    url(r'^delete_bookmark$', views.delete_bookmark ,name='delete_bookmark'),
    url(r'^update_frequency$', views.update_frequency ,name='update_frequency'),
    url(r'^extension_check$', views.extension_check ,name='extension_check')
]