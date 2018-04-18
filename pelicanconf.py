#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Sitio
SITENAME = 'Sistema Anticorrupción del Estado de Coahuila de Zaragoza'
SITEURL = 'http://www.seacoahuila.org.mx'
SITELOGO = 'imagenes/coahuila.png'

# Directorio donde esta el contenido
PATH = 'content'

# Directorios que tienen los articulos
ARTICLE_PATHS = ['comunicados']

# Directorios que tienen páginas fijas, no artículos
PAGE_PATHS = ['anuncios', 'cpc', 'licencias', 'secretaria-ejecutiva', 'terminos']

# Directorios y archivos que son fijos
# Agregue también los directorios con archivos para las artículos
STATIC_PATHS = ['imagenes', 'CNAME', 'favicon.ico', 'LICENSE', 'README.md',
                'comunicados', 'cpc', 'secretaria-ejecutiva']

# Usar el nombre del directorio como la categoría
USE_FOLDER_AS_CATEGORY = True

# Los artículos van en directorios por categoría
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'

# Autor por defecto
AUTHOR = 'SEA Coahuila'

# Las páginas fijas van en directorios autor/categoria/titulo/
# Autores: CPC, Secretaría Ejecutiva, Términos, Licencias
PAGE_URL = '{author}/{category}/{slug}/'
PAGE_SAVE_AS = '{author}/{category}/{slug}/index.html'

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

# Copiar las fuentes
OUTPUT_SOURCES = False

# En desarrollo, los URL son relativos
RELATIVE_URLS = True
LOAD_CONTENT_CACHE = False
DELETE_OUTPUT_DIRECTORY = False

# Paginacion
#DEFAULT_PAGINATION = False
DEFAULT_PAGINATION = 8
DEFAULT_ORPHANS = 2
