module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  mode: 'jit',
  theme: {
    extend: {
      boxShadow: (theme) => ({
        c: `0 -24px 0 0 ${theme('colors.red.400')}`,
      }),
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
