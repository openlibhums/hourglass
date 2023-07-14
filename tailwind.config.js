import typography from '@tailwindcss/typography'
import forms from '@tailwindcss/forms'

export default {
  content: [
    './src/**/*.js',
    './templates/**/*.html'
  ],
  theme: {
    colors: {
      blue: '#1579a0',
      'blue-medium': '#5ba1bc',
      'blue-light': '#a1c9d9',
      tan: '#d6cbbc',
      'tan-medium': '#e2dad0',
      'tan-light': '#efeae4',
      red: '#e94c33',
      'red-medium': '#f08170',
      'red-light': '#f6b7ad',
      orange: '#ec8323',
      'orange-medium': '#f2a865',
      'orange-light': '#f7cda7',
      black: '#202124',
      white: '#fdfeff',
      transparent: 'transparent',
      current: 'currentColor'
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
