===================================
Mediamosa plugin for django-tinymce
===================================

This django application will add a mediamosa plugin to your tinymce
editor.

----------
Installing
----------

Install django-mediamosa-tinymce using pip.

Configure django-mediamosa first. In settings.py of your project:

.. code:: python

    MEDIAMOSA_URL = 'http://api-mediamosa.example.com'
    MEDIAMOSA_USERNAME = 'mediamosa-user'
    MEDIAMOSA_PASSWORD = 'mediamosa-password'

Add mediamosa_tinymce to INSTALLED_APPS in settings.py for your project:

.. code:: python

    INSTALLED_APPS = (
        ...
        'mediamosa_tinymce',
        ...
    )

Update your TinyMce configuration so it will load the new plugin and shows
a mediamosa button:

.. code:: python

    TINYMCE_DEFAULT_CONFIG = {
        ...
        'plugins': "table,spellchecker,paste,searchreplace,mediamosa",
        ...
        'theme_advanced_buttons3_add': 'mediamosa'
     }


Add the mediamosa_tinymce.urls to urls.py for your project:

.. code:: python

    urlpatterns = patterns('',
        ...
        url(r'^mediamosa/tinymce', include('mediamosa_tinymce.urls')),
        ...
    )

Run the django collectstatic command to copy the mediamosa plugin for tinymce to your statics directory.

::

    python ./manage.py collectstatic

-----
Usage
-----

*************************
Enabling Mediamosa plugin
*************************

In order for the tinymce mediamosa to call the correct url's, you need to set
the ModelAdmin's change_form template file:

.. code:: python

    class MyModelAdmin(admin.ModelAdmin):
        ...
        change_form_template = 'admin/mediamosa_tinymce_change_form.html'
        ...

This will load the correct url's to query in the plugin's javascript.

*****************************
Playing an inserted mediafile
*****************************

When you now output the model attribute containing the mediamosa entry you just
inserted, you can initialize it by adding the following code to your template.

.. code:: html

    <script type="text/javascript">
        var mediamosaPlayerURI = "{% url mediafile-play %}";
    </script>
    <script type="text/javascript" src="{{ STATIC_URL }}js/mediamosa-player.js"></script>

This will initialize the URI the ajax call should connect to and launch the
code that will replace the still with the actual video.
