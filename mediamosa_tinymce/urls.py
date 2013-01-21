from django.conf.urls.defaults import url, patterns, include

from django_mediamosa.views import PlayMediaFile

from views import TinyMceAssetSelectionDialog, JSONTinyMceMediafileId

urlpatterns = patterns('',

    # Asset browser dialog
    url(r'^/assets/$', TinyMceAssetSelectionDialog.as_view(),
        name='tinymce-mmasset-select-dialog'),

    # JSON call to request mediafile_id
    url(r'^/asset\.json$', JSONTinyMceMediafileId.as_view(),
        name='tinymce-json-mediafile-query'),

    # Asset player

    url(r'^/mediamosa', include('django_mediamosa.urls')),

)
