import os
import shutil
from nodejs import npm

from django.conf import settings
from django.core.management import call_command

THEME_NAME = 'hourglass'

THEME_PATH = os.path.join(settings.BASE_DIR, 'themes', THEME_NAME)

DIST_PATH = os.path.join(THEME_PATH, 'dist')

JANEWAY_STATIC_PATH = os.path.join(settings.BASE_DIR, 'static', THEME_NAME)

OTHER_SOURCE_PATHS = [
    (
        os.path.join(
            THEME_PATH,
            'node_modules',
            'minisearch',
            'dist',
            'es',
            'index.js',
        ),
        os.path.join(
            DIST_PATH,
            'js',
            'minisearch.js',
        )
    ),
    (
        os.path.join(
            THEME_PATH,
            'node_modules',
            '@glidejs',
            'glide',
            'dist',
            'glide.esm.js',
        ),
        os.path.join(
            DIST_PATH,
            'js',
            'glide.esm.js',
        )
    ),
    (
        os.path.join(
            THEME_PATH,
            'node_modules',
            '@glidejs',
            'glide',
            'dist',
            'css',
            'glide.core.min.css',
        ),
        os.path.join(
            DIST_PATH,
            'css',
            'glide.core.min.css',
        )
    ),
    (
        os.path.join(
            THEME_PATH,
            'node_modules',
            'simple-scrollspy',
            'demo',
            'dist',
            'simple-scrollspy.min.js',
        ),
        os.path.join(
            DIST_PATH,
            'js',
            'simple-scrollspy.min.js',
        )
    ),
    (
        os.path.join(
            THEME_PATH,
            'node_modules',
            'jump.js',
            'dist',
            'jump.module.js',
        ),
        os.path.join(
            DIST_PATH,
            'js',
            'jump.module.js',
        )
    ),
    (
        os.path.join(
            THEME_PATH,
            'node_modules',
            'rallax.js',
            'dist',
            'rallax.js',
        ),
        os.path.join(
            DIST_PATH,
            'js',
            'rallax.js',
        )
    ),
    (
        os.path.join(
            THEME_PATH,
            'node_modules',
            '@tarekraafat',
            'autocomplete.js',
            'dist',
            'autoComplete.min.js',
        ),
        os.path.join(
            DIST_PATH,
            'js',
            'autoComplete.min.js',
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
            DIST_PATH,
            'js',
            'list.min.js',
        )
    ),
    (
        os.path.join(
            THEME_PATH,
            'node_modules',
            'htmx.org',
            'dist',
            'htmx.min.js',
        ),
        os.path.join(
            DIST_PATH,
            'js',
            'htmx.min.js',
        )
    ),
    (
        os.path.join(
            THEME_PATH,
            'src',
            'media',
        ),
        os.path.join(
            DIST_PATH,
            'media',
        )
    ),
    (
        os.path.join(
            THEME_PATH,
            'src',
            'fonts',
        ),
        os.path.join(
            DIST_PATH,
            'fonts',
        )
    ),
]


def compile_css():
    python_dir = os.getcwd()
    os.chdir(THEME_PATH)
    npm.call(['run', 'buildcss'])
    os.chdir(python_dir)


def gather_assets():

    print(f"Collecting other assets in {DIST_PATH}")

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
    shutil.copytree(DIST_PATH, JANEWAY_STATIC_PATH, dirs_exist_ok=True)


def build():

    print('\n')
    print(f"Building theme: {THEME_NAME}")

    if not os.path.exists(DIST_PATH):
        os.makedirs(DIST_PATH)
    # You can comment out the following line in development
    # if rebuilding assets frequently
    # install_theme_dependencies()
    gather_assets()
    compile_css()
    copy_assets_to_static()
    print('\n')
    call_command('collectstatic', '--noinput')
