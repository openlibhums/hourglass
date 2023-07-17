import typography from '@tailwindcss/typography'
import forms from '@tailwindcss/forms'

// Algorithms from https://github.com/tailwindlabs/tailwindcss-typography/blob/master/src/styles.js
const round = (num) =>
  num
    .toFixed(7)
    .replace(/(\.[0-9]+?)0+$/, '$1')
    .replace(/\.0$/, '')
const rem = (px) => `${round(px / 16)}rem`
const em = (px, base) => `${round(px / base)}em`

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
      },
      // Customisation of Tailwind Typography plugin
      typography: ({ theme }) => ({
        DEFAULT: {
          css: {
            '--tw-prose-links': theme('colors.blue'),
            '--tw-prose-body': theme('colors.black'),
            '--tw-prose-headings': theme('colors.black'),
            '--tw-prose-bold': theme('colors.black'),
            '--tw-prose-lead': theme('colors.black'),
            '--tw-prose-bullets': theme('colors.black'),
            p: {
              fontSize: rem(18),
              lineHeight: round(25 / 16),
              marginTop: em(12, 16),
              marginBottom: em(12, 16)
            },
            '[class~="lead"]': {
              fontFamily: 'Poppins Bold',
              fontSize: em(24, 16),
              lineHeight: round(28 / 20)
            },
            h1: {
              fontFamily: 'Poppins Bold',
              fontWeight: 'normal'
            },
            h2: {
              fontFamily: 'Poppins Bold',
              fontWeight: 'normal'
            },
            h3: {
              fontFamily: 'Poppins Bold',
              fontWeight: 'normal'
            },
            h4: {
              fontFamily: 'Poppins Medium',
              fontWeight: 'normal'
            },
            h5: {
              fontFamily: 'Poppins Medium',
              fontWeight: 'normal'
            },
            h6: {
              fontFamily: 'Poppins Medium',
              fontWeight: 'normal'
            }
          }
        },
        lg: {
          css: {
            p: {
              fontSize: rem(20),
              lineHeight: round(26 / 18),
              marginTop: em(18, 18),
              marginBottom: em(18, 18)
            },
            '[class~="lead"]': {
              fontFamily: 'Poppins Bold',
              fontSize: em(28, 18),
              lineHeight: round(26 / 20)
            }
          }
        }
      })
    }
  },
  plugins: [
    typography,
    forms
  ]
}
