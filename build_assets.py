import os
import sys
import shutil
from nodejs import node, npm

from django.conf import settings
from django.core.management import call_command

THEME_NAME = 'path'

THEME_PATH = os.path.join(settings.BASE_DIR, 'themes', THEME_NAME)

COMPILE_PATH = os.path.join(THEME_PATH, 'compile.js')
# Note! See also paths defined in compile.js

ASSETS_PATH = os.path.join(THEME_PATH, 'assets')

OTHER_SOURCE_PATHS = [
    os.path.join(THEME_PATH, 'node_modules', 'lunr', 'lunr.min.js'),
    os.path.join(THEME_PATH, 'js'),
    os.path.join(THEME_PATH, 'fonts'),
]

JANEWAY_STATIC_PATH = os.path.join(settings.BASE_DIR, 'static', THEME_NAME)


def install_theme_dependencies():

    """
    Runs `npm install` to pick up the theme's
    Node dependencies listed in package.json.
    """

    python_dir = os.getcwd()
    os.chdir(THEME_PATH)
    print(f"Installing as Node.js module: {THEME_PATH}")
    npm.run(['install'], check=True)
    os.chdir(python_dir)


def compile_sass():
    python_dir = os.getcwd()
    os.chdir(THEME_PATH)
    node.run([COMPILE_PATH], check=True)
    os.chdir(python_dir)


def collect_assets():

    print(f"Collecting other assets in {ASSETS_PATH}")

    for path in OTHER_SOURCE_PATHS:
        print(path)
        if os.path.isdir(path):
            shutil.copytree(path, ASSETS_PATH, dirs_exist_ok=True)
        else:
            shutil.copy(path, ASSETS_PATH)


def copy_assets_to_static():

    print(f"Copying assets to {JANEWAY_STATIC_PATH}")
    shutil.copytree(ASSETS_PATH, JANEWAY_STATIC_PATH, dirs_exist_ok=True)


def build():

    print('\n')
    print(f"Building theme: {THEME_NAME}")

    if not os.path.exists(ASSETS_PATH):
        os.makedirs(ASSETS_PATH)
    install_theme_dependencies()
    compile_sass()
    collect_assets()
    copy_assets_to_static()
    print('\n')
    call_command('collectstatic', '--noinput')
