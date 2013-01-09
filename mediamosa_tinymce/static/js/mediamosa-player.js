$(document).ready(function() {

    // looks for mediamosa classes and activates the player
    $('img.mediamosa').each(function(index) {
        var asset_id = $(this).data('asset');
        var mediafile_id = $(this).data('mediafile');

        // query django-mediamosa for the player code
        $.ajax({
            url: mediamosaPlayerURI +"?asset_id=" + asset_id
                 + "&mediafile_id=" + mediafile_id,
            context: $(this)
        }).done(function(data) {
            $(this).replaceWith(data);
        });
    });

})