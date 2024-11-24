/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",   
    "./src/**/*.{js,ts,jsx,tsx}", 
  ],
  theme: {
    extend: {
      colors: {
        primary: '#2D3748',  
        accent: '#F59E0B',   
        'accent-dark': '#F29C11', 
        background: '#f8fafc',
      },
      boxShadow: {
        '2xl': '0 25px 50px rgba(0, 0, 0, 0.1)',
      }
    },
  },
  plugins: [],
};
