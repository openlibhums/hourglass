# Hourglass Subtheme for Janeway

This is a testing repository for a press subtheme based on Materialize using
the Material theme as a backup. Everything about it is provisional. I
imagine rebuilding the repo once we have agreed on an architecture.

## Installation

1. Clone this subtheme in `src/themes` with
`git clone git@github.com:BirkbeckCTP/path-subtheme.git src/themes`

2. Build assets with `python src/manage.py build_assets`.

## Development

Install dev dependencies for linting:

```sh
npm install
```

When making lots of small CSS changes that you want to see in the browser
during development, you can use sass at the command line to bypass the
build_assets script.

Install sass globally first:

```shell
npm install -g sass
```

Then run this command to tell sass to watch for changes in the SCSS and
put the compiled CSS directly into Janeway’s static assets folder:

```shell
sass --watch src/themes/path/sass/path.scss:src/static/path/path.min.css --style compressed
```

### CSS

Make changes to `.scss` files in the `sass` subfolder.
Any variables or rules declared in these files will overwrite matching
rules in Materialize CSS, on which the theme is based.

New files and folders should mirror the names of the
file structure in `node_modules/@materializecss/materialize/sass/` with
partial files for compoments.

Rerun `python src/manage.py build_assets` from the janeway repo
root to build and copy the SCSS, and the changes should appear.

### JS

Modify the files in `js` and rerun `build_assets`.

New files need to be added to `OTHER_SOURCE_FILES` in `build_assets.py`.

## Engineering

Janeway subtheme architecture is laid out in [the Janeway
documentation](https://janeway.readthedocs.io/en/latest/configuration.html#theming),
and involves a `build_assets.py` file that is run when the Django
`manage.py` command `build_assets` is run. This subtheme conforms to that
expectation, but only by introducing
[`nodejs-bin`](https://pypi.org/project/nodejs-bin/) as a Python
dependency.

We have to use Node and npm so that we can compile SCSS with
[`sass`](https://www.npmjs.com/package/sass), a.k.a. “Dart Sass”. As of
January 2023 there is no Python SASS library (!) that supports the latest
SASS syntax, such as `@use`. The Python library
[`libsass`](https://pypi.org/project/libsass/) is based on
a [now-deprecated C/C++ compiler](https://github.com/sass/libsass). And
the three other Python SASS compilers are more oudated than `libsass`.

Using Node also allows following a few other best practices.
It allows us to track the maintained version of
[`materialize`](https://www.npmjs.com/package/@materializecss/materialize)
with npm, which we would otherwise have to include as a git-submodule
because there is no up-to-date Python wrapper for it either, that we know
about.

With these functional requirements, the `build_assets.py` script does these things:

1. Installs the subtheme as a Node package, checking
`package.json` to update dependencies in `node_modules`.
2. Uses [`nodejs-bin`](https://pypi.org/project/nodejs-bin/) to run `compile.js`,
which uses `sass` to build the subtheme CSS and CSS source map files and put
them in `assets`.
3. Copies custom JavaScript from `js` to `assets`.
4. Copies everything to `assets` into a theme folder in `static`.
5. Calls `collect_static`.

While this configuration is the best option of the ones I've considered,
I don't like that build_assets results in an installation script being
run. I considered altering the `build_assets` Django command but could not
pass options or args to this subtheme without breaking other
implementations of `build_assets.build()`. Maybe we could separate the
installation part with a separate Django command.

### Alternatives considered

1. Make [`nodejs-bin`](https://pypi.org/project/nodejs-bin/) a dependency
of this repository, with its own requirements.txt. Decided against this
because it would mean you'd have to install requirements separately for
the subtheme. Also, if we do use more JavaScript for frontend development,
we will likely want a way to run it with Python, so adding Node as
a dependency seems like a solid choice.
2. Use the Dart Sass command line utility, which must be globally installed,
to compile CSS into assets, but commit the compiled code so that servers don't
have to run `sass` or Node. Decided against this because we do not want to
commit code from dependencies.
3. Use [`nodeenv`](https://pypi.org/project/nodeenv/), which would allow
the "global" installation of Dart Sass and potentially avoid the `nodejs-bin`
dependency, but add more virtual environment spaghetti.

## Licensing

The code in this repository is licensed under AGPL 3.0.

Unless otherwise stated, the original textual content and visual designs
in this repository are the copyright of Birkbeck, University of London,
and they are licenced under a [Creative Commons Attribution 4.0
International License](https://creativecommons.org/licenses/by/4.0/) (CC
BY 4.0). The Open Library of Humanities and its logos are registered
trademarks.

The attribution-required and trademarked content is restricted to the
following folders:

- `templates/custom/*`

- `src/media/*`

The CC BY license lets you share and adapt these materials so long as you
properly credit the source. Proper attribution of the OLH must be given in
the following manner:

- Attribute the materials wherever they appear, including published
  end-product websites.

- Spell out the full name of the Open Library of Humanities and provide
a link to our website, as in one of these examples:

  - “The Open Access Movement” was first published by the Open Library of
Humanities, openlibhums.org

  - Diamond open access diagram by the
    [Open Library of Humanities](https://www.openlibhums.org/)

- Display the attribution so that it is clearly visible and easily
  legible, not obscured or hidden, with text that is the same size as the
  main text in your work, or a minimum of 12pt (print) or 18px (web),
  whichever is larger

- Under no circumstances may your use or attribution of our materials
  misconstrue the Open Library of Humanities as a publisher of your works
