from django.conf.urls.defaults import url, patterns, include

from django_mediamosa.views import PlayMediaFile

from views import TinyMceAssetSelectionDialog

urlpatterns = patterns('',

    # Asset browser dialog
    url(r'^/assets/$', TinyMceAssetSelectionDialog.as_view(),
        name='tinymce-mmasset-select-dialog'),

    # Asset player

    url(r'^/mediamosa', include('django_mediamosa.urls')),

)
