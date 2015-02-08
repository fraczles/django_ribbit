from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'ribbit_app.views.index'), #root
	url(r'^login$', 'ribbit_app.views.login_view'), #login
	url(r'^logout$', 'ribbit_app.views.logout_view'), #logout
	url(r'^signup$', 'ribbit_app.views.signup'), #signup
	url(r'^submit$', 'ribbit_app.views.submit'), #submit new ribbit
	url(r'^ribbits$', 'ribbit_app.views.public'), #public ribbits
)
