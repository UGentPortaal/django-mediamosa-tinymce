django.jQuery(document).ready(function() {
    tinymce.PluginManager.requireLangPack('mediamosa');

    tinymce.create('tinymce.plugins.mediaMosaPlugin', {

        init: function(ed, url) {
            ed.addCommand('mceMediaMosa', function(ui, v) {
                ed.windowManager.open({
                    file   : mediamosaAssetDialogURI,
                    width  : ed.getParam('mediamosa_popup_width', 800),
                    height : ed.getParam('mediamosa_popup_height', 700),
                    inline : 1
                }, {
                    plugin_url : url
                });
            });

            ed.addButton('mediamosa', {
                title: 'mediamosa.title',
                cmd: 'mceMediaMosa',
                image: url + '/img/mediamosa.png'
            });

            ed.addCommand('mceMediaMosaInsert', function(ui, v) {
                var asset_id = v['asset_id'];
                var mediafile_id = v['mediafile_id'];
                var still_url = v['still_url'];

                var html = '<img src="'+still_url+'" '+
                                'alt="Mediamosa Mediafile" '+
                                'class="mediamosa" '+
                                'width="620" '+
                                'height="350" '+
                                'data-asset="'+asset_id+'" '+
                                'data-mediafile="'+mediafile_id+'" />';

                this.execCommand('mceInsertRawHTML', false, html);
                console.log(html);
            });
        },

        getInfo: function() {
            return {
                longname  : 'MediaMosa',
                author    : 'UGent Portaalteam',
                authorurl : 'http://www.ugent.be/',
                infourl   : 'http://www.ugent.be/',
                version   : '0.1'
            }
        }

    });

    tinymce.PluginManager.add('mediamosa', tinymce.plugins.mediaMosaPlugin);
});