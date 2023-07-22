/** @type {import('tailwindcss').Config} */
module.exports = {
    purge: {
      content: ['./src/**/*.jsx', './src/**/*.js'],
      options: {
        safelist: [],
      }
    },
    darkMode: false,
    theme: {
      extend: {},
    },
    variants: {},
    plugins: [],
  }

