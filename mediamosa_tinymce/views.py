import json

from django.views.generic import ListView, DetailView
from django.http import HttpResponse, Http404

from django_mediamosa.base import api


class TinyMceAssetSelectionDialog(ListView):
    template_name = 'mediamosa_tinymce/tinymce_asset_dialog.html'
    paginate_by = 10

    def get_queryset(self):
        asset_list = api.asset_list()
        return filter(lambda asset: asset.has_streamable_mediafiles, asset_list)


class JSONTinyMceMediafileId(DetailView):

    def get_object(self, queryset=None):
        asset_id = self.request.GET.get('id')
        try:
            mediafile = api.asset(asset_id).get_mediafile()
        except:
            return None
        return mediafile

    def render_to_response(self, context, **response_kwargs):
        if self.object is None:
            raise Http404
        else:
            return HttpResponse(
                json.dumps({'mediafile_id': self.object.id}))
