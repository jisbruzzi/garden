const extraConfig=(process.env.NODE_ENV==="production"?{
  purge:{
    content: ['_site/**/*.html'],
    options: {
      safelist: [],
    },
  }
}:{})
module.exports = {
  //mode: 'jit',
  ...extraConfig,
  theme: {
    extend: {
      colors: {
        change: 'black',
      },
    },
  },
  variants: {},
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
