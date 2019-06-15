# -*- coding: utf-8 -*-

extensions = ['recommonmark']
templates_path = [
    '/home/docs/checkouts/readthedocs.org/readthedocs/templates/sphinx',
    'templates', '_templates', '.templates']
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
master_doc = 'README'
project = u'drf-microservice'
copyright = u'2019'
version = 'latest'
release = 'latest'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
htmlhelp_basename = 'drf-microservice'
file_insertion_enabled = False
latex_documents = [
    ('index', 'drf-microservice.tex', u'drf-microservice Documentation',
     u'', 'manual'),
]
