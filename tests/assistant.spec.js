// assistant.spec.js
import { test, expect } from '@playwright/test';

test('CoilyCurlyOffice login test', async ({ page }) => {
  await page.goto('https://coilycurlyoffice.com');

  // Click on 'Log in' link (you might need to adjust selector if this fails)
  await page.click('text=Log in');

  // Fill in login form
  await page.fill('input[name="email"]', 'aileen.siele@yale.edu'); // use real test account email
  await page.fill('input[name="password"]', 'AileenAgain1'); // use test account password

  await page.click('button[type="submit"]');

  await expect(page.getByRole('link', { name: 'Braiders', exact: true })).toBeVisible();



});
