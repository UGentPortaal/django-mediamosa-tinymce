from django.views.generic import ListView

from django_mediamosa.base import api


class TinyMceAssetSelectionDialog(ListView):
    template_name = 'mediamosa_tinymce/tinymce_asset_dialog.html'
    paginate_by = 10

    def get_queryset(self):
        asset_list = api.asset_list()
        return asset_list
