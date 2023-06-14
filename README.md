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

### Code styling and linting

The repository is set up with a few formatters and linters:

- [Standard](https://standardjs.com/) for JavaScript

- [djhtml](https://github.com/rtts/djhtml) for Django template file indentation,
  using 2-space-indents to better handle long Tailwind class lines

Please run these two commands before pushing:

```shell
standard --fix
djhtml --tabwidth 2 templates
```

We haven’t enforced them as a pre-commit hook, because we’d need to
discuss the implications of that first.

## Engineering

As an alternative, we could use
[django-tailwind](https://github.com/timonweb/django-tailwind).
