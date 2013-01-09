from distutils.core import setup

long_desc = open('README.md').read()

setup(
    name='MediaMosa Plugin for TinyMCE',
    version='0.0.1',
    author='UGent Portaal Team',
    author_email='portaal-tech@ugent.be',
    packages=['mediamosa_tinymce'],
    scripts=[],
    url='http://www.mediamosa.org',
    license='LICENSE.txt',
    description='TinyMCE plugin for MediaMosa in Django.',
    long_description=long_desc
)