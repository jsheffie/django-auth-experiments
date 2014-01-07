from django.conf.urls import patterns, include, url
from rest_framework import routers
from quickstart import views as qs_views

from django.contrib import admin
admin.autodiscover()

# automagically generating some view's for our viewset's
router = routers.DefaultRouter()
router.register(r'users', qs_views.UserViewSet)
router.register(r'groups', qs_views.GroupViewSet)


# Wire up our API usig automatic URL routing.
# Additionally, we include the login URL's for the browsable API.

urlpatterns = patterns('',
	url(r'^', include(router.urls)),
	url(r'testing_users/', qs_views.testing_users),
	url(r'logout/', qs_views.logout_view),
	(r'^accounts/login/$', 'django.contrib.auth.views.login'),
	url(r'no/auth/view/', qs_views.no_auth_view),
	url(r'auth/view/',    qs_views.auth_view),

	# rest_framework's browsable url's
	url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # url(r'^$', 'djauth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
