import typography from '@tailwindcss/typography'
import forms from '@tailwindcss/forms'

export default {
  content: [
    './src/**/*.js',
    './templates/**/*.html'
  ],
  theme: {
    container: {
      padding: {
        DEFAULT: '3rem',
        sm: '6rem',
        lg: '8rem',
        xl: '10rem',
        '2xl': '12rem'
      }
    },
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
