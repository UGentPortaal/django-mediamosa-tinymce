tinyMCEPopup.requireLangPack();

var MediaMosaDialog = {
    preInit : function() {},

    init : function() {

    },

    resize : function() {},

    insert : function(data) {

        tinyMCEPopup.execCommand('mceMediaMosaInsert', false, {
            asset_id: data.asset_id,
            mediafile_id: data.mediafile_id,
            still_url: data.url
        });

        tinyMCEPopup.close();
    }
};

MediaMosaDialog.preInit();
tinyMCEPopup.onInit.add(MediaMosaDialog.init, MediaMosaDialog);