import os
import shutil
from nodejs import node, npm

from django.conf import settings
from django.core.management import call_command

THEME_NAME = 'path'

THEME_PATH = os.path.join(settings.BASE_DIR, 'themes', THEME_NAME)

COMPILE_PATH = os.path.join(THEME_PATH, 'compile.js')
# Note! See also paths defined in compile.js

ASSETS_PATH = os.path.join(THEME_PATH, 'assets')

JANEWAY_STATIC_PATH = os.path.join(settings.BASE_DIR, 'static', THEME_NAME)

OTHER_SOURCE_PATHS = [
    (
        os.path.join(
            THEME_PATH,
            'node_modules',
            'jquery',
            'dist',
            'jquery.min.js',
        ),
        os.path.join(
            ASSETS_PATH,
            'js',
            'jquery.min.js',
        )
    ),
    (
        os.path.join(
            THEME_PATH,
            'node_modules',
            '@materializecss',
            'materialize',
            'dist',
            'js',
            'materialize.min.js',
        ),
        os.path.join(
            ASSETS_PATH,
            'js',
            'materialize.min.js',
        )
    ),
    (
        os.path.join(
            THEME_PATH,
            'node_modules',
            'lunr',
            'lunr.min.js',
        ),
        os.path.join(
            ASSETS_PATH,
            'js',
            'lunr.min.js',
        )
    ),
    (
        os.path.join(
            THEME_PATH,
            'node_modules',
            'list.js',
            'dist',
            'list.min.js',
        ),
        os.path.join(
            ASSETS_PATH,
            'js',
            'list.min.js',
        )
    ),
    (
        os.path.join(
            THEME_PATH,
            'js',
        ),
        os.path.join(
            ASSETS_PATH,
            'js',
        )
    ),
    (
        os.path.join(
            THEME_PATH,
            'fonts',
        ),
        os.path.join(
            ASSETS_PATH,
            'fonts',
        )
    ),
    (
        os.path.join(
            THEME_PATH,
            'node_modules',
            '@fortawesome',
            'fontawesome-free',
            'css',
            'fontawesome.min.css',
        ),
        os.path.join(
            ASSETS_PATH,
            'fonts',
            'fontawesome',
            'css',
            'fontawesome.min.css',
        )
    ),
    (
        os.path.join(
            THEME_PATH,
            'node_modules',
            '@fortawesome',
            'fontawesome-free',
            'css',
            'brands.min.css',
        ),
        os.path.join(
            ASSETS_PATH,
            'fonts',
            'fontawesome',
            'css',
            'brands.min.css',
        )
    ),
    (
        os.path.join(
            THEME_PATH,
            'node_modules',
            '@fortawesome',
            'fontawesome-free',
            'webfonts',
            'fa-brands-400.woff2',
        ),
        os.path.join(
            ASSETS_PATH,
            'fonts',
            'fontawesome',
            'webfonts',
            'fa-brands-400.woff2',
        )
    )
]


def install_theme_dependencies():

    """
    Runs `npm install` to pick up the theme's
    Node dependencies listed in package.json.
    """

    python_dir = os.getcwd()
    os.chdir(THEME_PATH)
    print(f"Installing as Node.js module: {THEME_PATH}")
    npm.run(['install', '--omit=dev'], check=True)
    os.chdir(python_dir)


def compile_sass():
    python_dir = os.getcwd()
    os.chdir(THEME_PATH)
    node.run([COMPILE_PATH], check=True)
    os.chdir(python_dir)


def collect_assets():

    print(f"Collecting other assets in {ASSETS_PATH}")

    for source, destination in OTHER_SOURCE_PATHS:
        print(source)
        if os.path.isdir(source):
            shutil.copytree(source, destination, dirs_exist_ok=True)
        else:
            if not os.path.exists(os.path.dirname(destination)):
                os.makedirs(os.path.dirname(destination))
            shutil.copy(source, destination)


def copy_assets_to_static():

    print(f"Copying assets to {JANEWAY_STATIC_PATH}")
    shutil.copytree(ASSETS_PATH, JANEWAY_STATIC_PATH, dirs_exist_ok=True)


def build():

    print('\n')
    print(f"Building theme: {THEME_NAME}")

    if not os.path.exists(ASSETS_PATH):
        os.makedirs(ASSETS_PATH)
    # You can comment out the following line in development
    # if rebuilding assets frequently
    # install_theme_dependencies()
    collect_assets()
    compile_sass()
    copy_assets_to_static()
    print('\n')
    call_command('collectstatic', '--noinput')
