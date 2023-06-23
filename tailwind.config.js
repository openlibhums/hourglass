import typography from '@tailwindcss/typography'
import forms from '@tailwindcss/forms'

export default {
  content: [
    './src/**/*.js',
    './templates/**/*.html'
  ],
  theme: {
    colors: {
      'hourglass-blue': '#1579A0',
      'hourglass-orange': '#EC8323',
      'hourglass-red': '#E94C33',
      'hourglass-tan': '#D6CBBC',
      'hourglass-tan-light': '#EAE5DD',
      transparent: 'transparent',
      current: 'currentColor',
      white: '#ffffff',
      black: '#000000'
    },
    container: {
      padding: {
        DEFAULT: '1.5rem',
        sm: '4rem',
        lg: '6rem',
        xl: '8rem',
        '2xl': '10rem'
      }
    },
    extend: {
      fontFamily: {
        poppins: ['Poppins Regular', 'sans-serif'],
        'poppins-medium': ['Poppins Medium', 'sans-serif'],
        'poppins-bold': ['Poppins Bold', 'sans-serif'],
        'source-sans': ['Source Sans', 'sans-serif'],
        'source-sans-italic': ['Source Sans Italic', 'sans-serif']
      }
    }
  },
  plugins: [
    typography,
    forms
  ]
}
