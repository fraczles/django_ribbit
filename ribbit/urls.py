from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'rabbit_app.views.index'), #root
	url(r'^login$', 'rabbit_app.views.login_view'), #login
	url(r'^logout$', 'rabbit_app.views.logout_view'), #logout
	url(r'^signup$', 'rabbit_app,views.signup'), #signup
)
