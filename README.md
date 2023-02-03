# Path Subtheme for Janeway

## How this repository is structured

Janeway subtheme architecture is laid out in [the Janeway documentation](https://janeway.readthedocs.io/en/latest/configuration.html#theming), and involves a `build_assets.py` that is run when the Django `manage.py` command `build_assets` is run. This subtheme conforms to that expectation, but not for the compiling of the SASS code into CSS.

For compiling, we have to use Node and npm so that we can use [`sass`](https://www.npmjs.com/package/sass). As of January 2023 there is no Python SASS library (!) that supports the latest SASS syntax, such as `@use`. The Python library [`libsass`](https://pypi.org/project/libsass/) is based on a [now-deprecated C/C++ compiler](https://github.com/sass/libsass). And the three other Python SASS compilers are more oudated than `libsass`.

Using Node does give us some advantages. It allows us to track `materialize`, which we would otherwise have to include as a git-submodule because there is no up-to-date Python wrapper for it either, that we know about.

At the moment, only CSS is compiled; Materialize JavaScript, Materialize Icons, and jQuery are loaded via CDNs.


## Installation

1. Install [Node.js v16.x or later](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-20-04) and npm[0]

2. Install `sass` globally so that you can access `sass` from the command line.
```
sudo npm i -g sass
```
3. Clone and install this subtheme
    ```shell
    git clone https://github.com/BirkbeckCTP/path
    cd path
    npm install
    ```

## Making changes

Make changes to `.scss` files in the `sass` subfolder. Any variables or rules declared in these files will overwtie matching rules in Materialize CSS, on which the theme is based.

New files and folders should mirror the names of the file structure in `node_modules/@materializecss/materialize/sass/` with partial files for compoments.

Run this command to auto-compile the minified CSS as you make and save changes.
```
sass --watch sass/path.scss:assets/path.min.css --style compressed
```

Rerun `python src/manage.py build_assets` from the janeway repo root to copy the minified CSS to Janeway static files.

See the changes live.

We commit both source SASS and the compiled minified CSS in this repository, so that from the Janeway architecture perspective, all you have to do is run `python src/manage.py build_assets`. You should not have to install `sass` or `Node` or `npm` on production servers.

## Customization

If you have the [Custom Styling Plugin](https://github.com/BirkbeckCTP/customstyling) installed in your Janeway instance, you can add CSS code to override the default colors and fonts.

What color values should you use? See the [Materialize color palette](https://materializecss.github.io/materialize/color.html#palette) for ideas.
