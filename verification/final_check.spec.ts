import { test, expect } from '@playwright/test';

test('verify homepage content and slider', async ({ page }) => {
  await page.goto('file://' + process.cwd() + '/index.html');

  // Verify H1 contains LAWETA
  const h1 = page.locator('h1');
  await expect(h1).toContainText(/LAWETA/i);
  await expect(h1).toContainText(/POMOC DROGOWA/i);
  await expect(h1).toContainText(/SKUP AUT/i);
  await expect(h1).toContainText(/DETAILING/i);

  // Verify Benefits contains GOTÓWKA DO RĘKI
  const benefits = page.locator('.benefits');
  await expect(benefits).toContainText(/GOTÓWKA DO RĘKI/i);

  // Verify slider dots are circles (visually via screenshot)
  await page.locator('.testimonials').scrollIntoViewIfNeeded();
  await page.screenshot({ path: 'verification/final_check.png', fullPage: true });
});
