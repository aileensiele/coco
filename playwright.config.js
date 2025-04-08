// playwright.config.js
/** @type {import('@playwright/test').PlaywrightTestConfig} */
const config = {
    timeout: 30000,
    retries: 0,
    testDir: './tests',
    use: {
      headless: true,
      baseURL: 'https://coilycurlyoffice.com',
    },
  };
  export default config;
  