// This little file has to exist independently of build_assets.py
// so that we can avoid installing
// Dart Sass globally on servers, while also avoiding committing
// compiled CSS to Git.
// See https://sass-lang.com/documentation/js-api

import sass from 'sass';
import path from 'node:path';
import {writeFileSync} from 'node:fs';

const sassPath = path.join('sass', 'path.scss');

const assetsPath = path.join('assets');

const cssFileName = 'path.min.css';
const cssMapFileName = 'path.min.css.map';

const cssPath = path.join(assetsPath, cssFileName);
const cssMapPath = path.join(assetsPath, cssMapFileName);

console.log('Compiling SASS to CSS in theme folder:')
console.log(`From ${sassPath} to ${cssPath} and ${cssMapPath}`)

const options = {
  style: 'compressed',
  sourceMap: true,
}
const result = sass.compile(sassPath, options);
const cssSourceMapUrl = `/*# sourceMappingURL=${cssMapFileName} */`;
const cssString = result.css + cssSourceMapUrl;
writeFileSync(cssPath, cssString);
writeFileSync(cssMapPath, JSON.stringify(result.sourceMap));
