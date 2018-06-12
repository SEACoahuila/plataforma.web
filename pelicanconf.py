#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Sitio web
SITENAME = 'Sistema Anticorrupción del Estado de Coahuila de Zaragoza'
SITEURL = 'http://www.seacoahuila.org.mx'
SITELOGO = 'theme/images/saec.png'
SITEDESCRIPTION = 'El Sistema Estatal Anticorrupción tiene las facultades de establecer principios, bases generales, políticas públicas y procedimientos para la coordinación entre las autoridades de los Entes Públicos en la prevención, detección y sanción de faltas administrativas y hechos de corrupción, así como en la fiscalización y control de recursos públicos.'
SITETWITTER = '@sesaecoah'

# Autor por defecto
AUTHOR = 'SEA Coahuila'

# Directorio donde esta el contenido
PATH = 'content'

# Directorios que tienen los articulos
ARTICLE_PATHS = ['comunicados']

# Directorios que tienen páginas fijas, no artículos
PAGE_PATHS = ['anuncios', 'cc', 'cpc', 'secretaria-ejecutiva', 'terminos']

# Directorios y archivos que son fijos
# Agregue también los directorios que tienen archivos para artículos y páginas
STATIC_PATHS = ['CNAME', 'favicon.ico', 'LICENSE', 'README.md', 'robots.txt',
                'comunicados', 'cc', 'cpc', 'secretaria-ejecutiva']

# Usar el nombre del directorio como la categoría
USE_FOLDER_AS_CATEGORY = True

# Los artículos van en directorios categoria/titulo/
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'

# Las páginas fijas van en directorios autor/categoria/titulo/
# Autores: CC, CPC, Secretaría Ejecutiva, General
PAGE_URL = '{author}/{category}/{slug}/'
PAGE_SAVE_AS = '{author}/{category}/{slug}/index.html'

# Tema
THEME = 'themes/startbootstrap-modern-business'

# Lenguaje y zona horaria
DEFAULT_LANG = 'es'
TIMEZONE = 'America/Mexico_City'

# Borrar toda la salida,
# Borra directorios ocultos en output como .git, mantenga en falso
DELETE_OUTPUT_DIRECTORY = False

# Para desarrollo, los vinculos son relativos
RELATIVE_URLS = True

# Para desarrollo, se desactiva la paginacion
DEFAULT_PAGINATION = False
#DEFAULT_PAGINATION = 8
#DEFAULT_ORPHANS = 2

# Para desarrollo, se desactiva la generacion de feeds
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

# Para desarrollo, recomendado mantener en falso
LOAD_CONTENT_CACHE = False
