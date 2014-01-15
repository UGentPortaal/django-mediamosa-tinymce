from django.conf.urls import url, patterns, include

from django_mediamosa.views import PlayMediaFile

from views import TinyMcePublicAssetSelectionDialog, JSONTinyMceMediafileId, TinyMcePrivateAssetSelectionDialog

urlpatterns = patterns('',

    # Asset browser dialog
    url(r'^/assets/$', TinyMcePublicAssetSelectionDialog.as_view(),
        name='tinymce-mmasset-select-dialog'),

    url(r'^/assets/my/$', TinyMcePrivateAssetSelectionDialog.as_view(),
        name='tinymce-mmasset-personal-select-dialog'),

    # JSON call to request mediafile_id
    url(r'^/asset\.json$', JSONTinyMceMediafileId.as_view(),
        name='tinymce-json-mediafile-query'),

    # Asset player

    url(r'^/mediamosa', include('django_mediamosa.urls')),

)
