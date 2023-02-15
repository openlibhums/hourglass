import os
import shutil

from django.conf import settings
from django.core.management import call_command

THEME_NAME = 'path'

ASSETS_PATH = os.path.join(settings.BASE_DIR, 'themes', THEME_NAME, 'assets')

OTHER_SOURCE_PATHS = [
    os.path.join(
        settings.BASE_DIR, 'themes', THEME_NAME, 'node_modules', 'lunr', 'lunr.min.js'
    ),
    os.path.join(
        settings.BASE_DIR, 'themes', THEME_NAME, 'js', 'search.js'
    ),
    os.path.join(
        settings.BASE_DIR, 'themes', THEME_NAME, 'js', 'dropdown.js'
    ),
]

JANEWAY_STATIC_PATH = os.path.join(settings.BASE_DIR, 'static', THEME_NAME)


def collect_assets():
    for path in OTHER_SOURCE_PATHS:
        shutil.copy(path, ASSETS_PATH)


def build():
    print(f"Copying files for {THEME_NAME} theme:")
    print(f"Collecting assets in {ASSETS_PATH}")
    collect_assets()
    print(f"Copying assets to {JANEWAY_STATIC_PATH}")
    shutil.copytree(ASSETS_PATH, JANEWAY_STATIC_PATH, dirs_exist_ok=True)
    call_command('collectstatic', '--noinput')
