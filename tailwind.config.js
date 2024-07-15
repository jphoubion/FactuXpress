/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./invoicing/templates/invoicing/**/*.{html,js}",
            "./FactuXpress/invoicing/**/*.py"
  ],
  theme: {
    extend: {},
  },
  plugins: [
//    require('daisyui'),
  ],
  daisyui: {
    themes: ["business"],
  },
}
