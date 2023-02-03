import os
import shutil

from django.conf import settings
from django.core.management import call_command

THEME_NAME = 'path'
THEME_DIST_PATH = 'assets'


def build():
    src_path = os.path.join(settings.BASE_DIR, 'themes', THEME_NAME, THEME_DIST_PATH)
    dest_path = os.path.join(settings.BASE_DIR, 'static', THEME_NAME)
    print(f"Copying files for {THEME_NAME} theme:")
    print(f"From: {src_path}")
    print(f"To: {dest_path}")
    shutil.copytree(src_path, dest_path, dirs_exist_ok=True)
    call_command('collectstatic', '--noinput')
