# Hourglass Theme for Janeway

## Installing

1. Clone this repository into the theme folder of your
   [Janeway](https://github.com/BirkbeckCTP/janeway) installation:

   ```shell
   cd src/themes
   git clone git@github.com:BirkbeckCTP/hourglass.git
   ```

2. With your Python virtual environment activated, install the Python
   dependencies using pip.

   ```shell
   pip install -r requirements.txt
   ```

3. Install the JavaScript dependencies using NPM:

   ```shell
   npm install
   ```

   You should see a new `node_modules` file in the `hourglass` folder.

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

#### Styling notes

Each section of content is given a container and relative positioning, so
that it can be used as an anchor for background colors and images.

Z-index is used as follows:

- `-z-10` for the solid light tan background

- `z-0`, `z-10`, and `z-20` for the constructivist collages of geometric shapes and cut-out photos

- `z-30` for pseudo-elements used to extend alternate color backgrounds
outside the container to the edge left and/or right

- `z-40` for the content layer, along with its immediate, in-container
background color

- `z-50` for the sticky desktop nav so it is persistent on top of
everything else

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
