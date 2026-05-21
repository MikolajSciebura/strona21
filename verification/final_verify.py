from playwright.sync_api import Page, expect, sync_playwright
import os

def test_final_verification(page: Page):
  # Use absolute path for file:// protocol
  path = os.path.abspath("index.html")
  page.goto(f"file://{path}")

  # Verify H1 contains LAWETA
  h1 = page.locator('h1')
  expect(h1).to_contain_text("LAWETA")
  expect(h1).to_contain_text("POMOC DROGOWA")
  expect(h1).to_contain_text("SKUP AUT")
  expect(h1).to_contain_text("DETAILING")

  # Verify Benefits contains GOTÓWKA DO RĘKI
  benefits = page.locator('.benefits')
  expect(benefits).to_contain_text("GOTÓWKA DO RĘKI")

  # Take a screenshot of the testimonials section where the slider dots are
  testimonials = page.locator('.testimonials')
  testimonials.scroll_into_view_if_needed()
  page.wait_for_timeout(500) # Wait for potential scroll animations
  page.screenshot(path="/home/jules/verification/final_slider_check.png")

  # Check SEO read more
  read_more_btn = page.locator('.btn-read-more').first
  read_more_btn.click()
  page.wait_for_timeout(500)
  page.screenshot(path="/home/jules/verification/final_seo_check.png")

  # Check detailing page link
  page.get_by_role("link", name="AUTO DETAILING").first.click()
  expect(page).to_have_title(re.compile("Detailing"))
  page.screenshot(path="/home/jules/verification/final_detailing_page_check.png")

import re

if __name__ == "__main__":
  if not os.path.exists("/home/jules/verification"):
    os.makedirs("/home/jules/verification")
  with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    try:
      test_final_verification(page)
    except Exception as e:
      print(f"Error during verification: {e}")
      # Still take a screenshot if possible
      page.screenshot(path="/home/jules/verification/error.png")
    finally:
      browser.close()
