import {existsSync, mkdirSync, writeFileSync} from 'node:fs';
import sass from 'sass';

try {
  const staticCssPath = "../../static/path/css/";
  if (!existsSync(staticCssPath)) {
    mkdirSync(
      staticCssPath,
      { recursive: true }
    );
  }
  console.log('Made sure static path exists: ', staticCssPath);

  const compiledCss = sass.compile('./node_modules/@materializecss/materialize/sass/materialize.scss');
  writeFileSync("../../static/path/css/app.css", compiledCss.css);
  console.log('Compiled path theme SCSS into static CSS');
} catch (error) {
  console.log(error);
}
