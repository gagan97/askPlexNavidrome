# -*- coding: utf-8 -*-
import logging
import os

SKILL_LOG_LEVEL=logging.INFO

# Plex Media Server config
PMS_SERVER_URL = os.getenv('PMS_SERVER_URL', 'https://')
PMS_SERVER_TOKEN = os.getenv('PMS_SERVER_TOKEN', '')
PMS_DEFAULT_SECTION_NAME = os.getenv('PMS_DEFAULT_SECTION_NAME', '')
PMS_DEFAULT_MAX_RESULTS = int(os.getenv('PMS_DEFAULT_MAX_RESULTS', '100'))

# Navidrome settings
NAVIDROME_URL = os.getenv('NAVIDROME_URL')
NAVIDROME_USER = os.getenv('NAVIDROME_USER')
NAVIDROME_PASSWORD = os.getenv('NAVIDROME_PASSWORD')
NAVIDROME_PORT = int(os.getenv('NAVIDROME_PORT', '4533'))
NAVIDROME_API_LOCATION = os.getenv('NAVIDROME_API_LOCATION', '/rest')
NAVIDROME_API_VERSION = os.getenv('NAVIDROME_API_VERSION', '1.16.1')

# Multi-source settings
PREFER_HIGH_BITRATE = os.getenv('PREFER_HIGH_BITRATE', 'false').lower() == 'true'
ENABLE_NAVIDROME = os.getenv('ENABLE_NAVIDROME', 'false').lower() == 'true'
ENABLE_PLEX = os.getenv('ENABLE_PLEX', 'true').lower() == 'true'
