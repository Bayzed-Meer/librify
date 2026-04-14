import { test, expect } from '@playwright/test';

test('has correct page title', async ({ page }) => {
  await page.goto('/');
  await expect(page).toHaveTitle(/Librify/);
});

test('main page loads successfully', async ({ page }) => {
  await page.goto('/');
  await expect(page.locator('body')).toBeVisible();
});
