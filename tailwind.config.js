import typography from '@tailwindcss/typography'
import forms from '@tailwindcss/forms'

export default {
  content: [
    './src/**/*.js',
    './templates/**/*.html'
  ],
  theme: {
    extend: {
      fontFamily: {
        poppins: ['Poppins Regular', 'sans-serif']
      }
    }
  },
  plugins: [
    typography,
    forms
  ]
}
