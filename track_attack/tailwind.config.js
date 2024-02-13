/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./*.html'],
  theme: {
    screens: {
      sm: '480px',
      md: '768px',
      lg: '976px',
      xl: '1440px',
    },
    extend: {
      colors: {
        brightRed: 'hsl(12,88%, 59%)',
        platinum: 'rgb(251, 251, 251)',
      },
      fontFamily: {
        poppins: ['Poppins', 'sans-serif'],
        silkscreen: ['Silkscreen'],
        neonderthaw: ['Neonderthaw'],
      },
    },
  },

  plugins: [],
}