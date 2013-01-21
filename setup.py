from setuptools import setup, find_packages

with open('README.rst', 'r') as file:
    long_desc = file.read()

version = __import__('mediamosa_tinymce').get_version()

setup(
    name='django-mediamosa-tinymce',
    version=version,
    author='UGent Portaal Team',
    author_email='portaal-tech@ugent.be',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    scripts=[],
    url='https://github.com/UGentPortaal/django-mediamosa-tinymce',
    license='BSD',
    description='Django integration for mediamosa in TinyMCE.',
    long_description=long_desc,
    install_requires=(
        'django-mediamosa',
        'django-tinymce',
    ),
    classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Topic :: Multimedia :: Video',
          'Topic :: Software Development :: Libraries',
          'Topic :: Utilities'
    ],
)
