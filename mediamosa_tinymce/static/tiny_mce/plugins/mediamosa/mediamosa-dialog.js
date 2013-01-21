tinyMCEPopup.requireLangPack();

var MediaMosaDialog = {
    preInit : function() {

    },

    init : function() {

    },

    resize : function() {

    },

    insert : function(data) {

        // fetch mediafile id
        $.ajax({
            url: MediafileIdQueryURI +"?id=" + data.asset_id
        }).done(function(jsondata) {

            // parse as json
            jsondata = jQuery.parseJSON( jsondata );

            // insert into tinymce
            tinyMCEPopup.execCommand('mceMediaMosaInsert', false, {
                asset_id: data.asset_id,
                mediafile_id: jsondata.mediafile_id,
                still_url: data.url
            });

            // close the dialog
            tinyMCEPopup.close();

        });

    }
};

MediaMosaDialog.preInit();
tinyMCEPopup.onInit.add(MediaMosaDialog.init, MediaMosaDialog);