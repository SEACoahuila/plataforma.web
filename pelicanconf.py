#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Autoría
AUTHOR = 'SEA Coahuila'
SITENAME = 'Secretaría Ejecutiva del Sistema Anticorrupción del Estado de Coahuila de Zaragoza'
SITEURL = 'http://www.seacoahuila.org.mx'
SITELOGO = 'imagenes/coahuila.png'

# Directorio donde esta el contenido
PATH = 'content'

# Directorios que tienen las publicaciones
ARTICLE_PATHS = ['comunicados']

# Directorios que tienen páginas, no publicaciones
PAGE_PATHS = ['contacto', 'declaraciones', 'institucional', 'transparencia']

# Directorios y archivos que son estáticos
# Agregue los que tienen subdirectorios con archivos para las publicaciones
STATIC_PATHS = ['comunicados', 'declaraciones', 'imagenes', 'transparencia',
                'CNAME', 'favicon.ico', 'LICENSE', 'README.md']

# Tema Clean Blog
#THEME = 'themes/startbootstrap-clean-blog'

# Tema Modern Business EN DESARROLLO
THEME = 'themes/startbootstrap-modern-business'

# Zona horaria y lenguaje
TIMEZONE = 'America/Mexico_City'
DEFAULT_LANG = 'es'

# Feed generation
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

# Se usa la categoría como estructura de directorios
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
PAGE_URL = '{category}/{slug}.html'
PAGE_SAVE_AS = '{category}/{slug}.html'

# Copiar las fuentes
OUTPUT_SOURCES = False

# En desarrollo
DEFAULT_PAGINATION = False
RELATIVE_URLS = True
LOAD_CONTENT_CACHE = False
DELETE_OUTPUT_DIRECTORY = False
