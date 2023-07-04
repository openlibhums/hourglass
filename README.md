# Hourglass Theme for Janeway

## Installing

1. Navigate to the root of your
   [Janeway](https://github.com/BirkbeckCTP/janeway) installation, and
   clone this subtheme into `src/themes`:

   ```shell
   git clone git@github.com:BirkbeckCTP/hourglass.git src/themes
   ```

2. Still in the Janeway root, install Node in your Janeway virtual
   environment using pip:

   ```shell
   pip install -r src/themes/hourglass/requirements.txt
   ```

3. Install the JavaScript dependencies
   in `src/themes/hourglass/package.json` using NPM:

   ```shell
   npm install --prefix ./src/themes/hourglass
   ```

## Deploying to production

From the Janeway root, build assets for all themes:

```shell
python src/manage.py build_assets
```

You can also rebuild just the CSS with NPM:

```shell
cd src/themes/hourglass
npm run build
```

## Updating in production

```shell
cd src/themes/hourglass
git pull
pip install -r requirements.txt
npm install
python ../../manage.py build_assets
```

## Developing

### CSS

Use Tailwind classes in the HTML templates to apply styling.

In the rare case you need to apply a style to the base layer or define
a custom component, make changes to `src/input.css` using `@layer` and
`@apply` commands.

When making lots of small CSS changes that you want to see in the browser
during development, you can use the hot-module replacement (HMR) feature
provided by Tailwind. To watch for changes, use this NPM command:

```shell
npm run dev
```

### JavaScript

Modify the files in `js` and rerun `build_assets`.

New files need to be added to `OTHER_SOURCE_FILES` in `build_assets.py`.

## Engineering

As an alternative, we could use
[django-tailwind](https://github.com/timonweb/django-tailwind).

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
