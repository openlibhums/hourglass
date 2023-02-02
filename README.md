# Path Subtheme for Janeway

## Configuration notes

Janeway subtheme architecture is laid out in [the Janeway documentation](https://janeway.readthedocs.io/en/latest/configuration.html#theming), and involves a `build_assets.py` that is run when the Django `manage.py` command `build_assets` is run.

However, for this subtheme, we have to use Node and npm so that we can use [`sass`](https://www.npmjs.com/package/sass). As of January 2023 there is no Python SASS library (!) that supports the latest SASS syntax, such as `@use`. The Python library [`libsass`](https://pypi.org/project/libsass/) is based on a [now-deprecated C/C++ compiler](https://github.com/sass/libsass). And the three other Python SASS compilers are more oudated than `libsass`.

Using Node does give us some advantages. It allows us to track `sass` as a version-controlled dependency using `package.json` and `package-lock.json`. The same goes for `materialize`, which we would otherwise have to include as a git-submodule because there is no up-to-date Python wrapper for it either, that we know about.

Rather than a `build_assets.py` file, this library currently has a `compile.js` file that synchronously makes the static files needed for the theme. At the moment, only CSS is compiled; Materialize JavaScript, Materialize Icons, and jQuery are loaded via CDNs.

## Installation

1. Install [Node.js v16.x or later](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-20-04) and npm[0]

2. Clone and install this subtheme
    ```shell
    git clone https://github.com/BirkbeckCTP/path
    cd path
    npm install
    node compile.js
    ```

## Customization

If you have the [Custom Styling Plugin](https://github.com/BirkbeckCTP/customstyling) installed in your Janeway instance, you can add CSS code to override the default colors and fonts.

What color values should you use? See the [Materialize color palette](https://materializecss.github.io/materialize/color.html#palette) for ideas.
