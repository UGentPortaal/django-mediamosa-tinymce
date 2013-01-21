$(document).ready(function() {

    do_ajax_call = function(context, asset_id, mediafile_id) {
        // query django-mediamosa for the player code
        $.ajax({
            url: mediamosaPlayerURI +"?asset_id=" + asset_id
                 + "&mediafile_id=" + mediafile_id,
            context: context
        }).done(function(data) {
            $(this).replaceWith(data);
        });
    }

    // looks for mediamosa classes and activates the player
    $('img.mediamosa').each(function(index) {
        var asset_id = $(this).data('asset');
        var mediafile_id = $(this).data('mediafile');

        do_ajax_call($(this), asset_id, mediafile_id);
    });

    // support for previous mediamosa tags
    $('div.mediamosa').each(function(index) {
        var pattern = /asset_id=(\w+)&mediafile_id=(\w+)/;
        var results = $(this).text().match(pattern);
        var asset_id = results[1];
        var mediafile_id = results[2];

        do_ajax_call($(this), asset_id, mediafile_id);
    });

})