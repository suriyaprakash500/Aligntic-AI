import re
import pytest
from playwright.async_api import Page, expect

import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_tc_001_landing_page_loads_and_main_heading_is_visible(page: Page):
    await page.goto('https://aligntic.vercel.app/')
    await expect(page.get_by_role('heading', name='Intelligence,\nbeautifully aligned.').first).to_be_visible()


import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_tc_002_navigate_to_products_via_view_products_cta(page: Page):
    await page.goto('https://aligntic.vercel.app/')
    await page.get_by_role('link', name='View Products').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/products')
    await expect(page.get_by_role('heading', name='Our AI Products').first).to_be_visible()


import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_tc_003_navigate_to_services_via_our_services_cta(page: Page):
    await page.goto('https://aligntic.vercel.app/')
    await page.get_by_role('link', name='Our Services').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/services')
    await expect(page.get_by_role('heading', name='AI Consulting & Services').first).to_be_visible()


import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_tc_004_header_navigation_from_landing_page(page: Page):
    await page.goto('https://aligntic.vercel.app/')
    await page.get_by_role('link', name='Products').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/products')
    await expect(page.get_by_role('heading', name='Our AI Products').first).to_be_visible()
    await page.goto('https://aligntic.vercel.app/')
    await page.get_by_role('link', name='Services').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/services')
    await expect(page.get_by_role('heading', name='AI Consulting & Services').first).to_be_visible()
    await page.goto('https://aligntic.vercel.app/')
    await page.get_by_role('link', name='About').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/about')
    await expect(page.get_by_role('heading', name='Aligning Intelligence with Humanity.').first).to_be_visible()
    await page.goto('https://aligntic.vercel.app/')
    await page.get_by_role('link', name='Contact Us').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/contact')
    await expect(page.get_by_role('heading', name='Get in touch').first).to_be_visible()


import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_tc_005_header_navigation_from_products_page(page: Page):
    await page.goto('https://aligntic.vercel.app/products')
    await page.get_by_role('link', name='Services').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/services')
    await expect(page.get_by_role('heading', name='AI Consulting & Services').first).to_be_visible()
    await page.goto('https://aligntic.vercel.app/products')
    await page.get_by_role('link', name='About').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/about')
    await expect(page.get_by_role('heading', name='Aligning Intelligence with Humanity.').first).to_be_visible()
    await page.goto('https://aligntic.vercel.app/products')
    await page.get_by_role('link', name='Contact Us').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/contact')
    await expect(page.get_by_role('heading', name='Get in touch').first).to_be_visible()
    await page.goto('https://aligntic.vercel.app/products')
    await page.get_by_role('link', name='Aligntic').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/')
    await expect(page.get_by_role('heading', name='Intelligence,\nbeautifully aligned.').first).to_be_visible()


import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_tc_006_header_navigation_from_services_page(page: Page):
    await page.goto('https://aligntic.vercel.app/services')
    await page.get_by_role('link', name='Products').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/products')
    await expect(page.get_by_role('heading', name='Our AI Products').first).to_be_visible()
    await page.goto('https://aligntic.vercel.app/services')
    await page.get_by_role('link', name='About').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/about')
    await expect(page.get_by_role('heading', name='Aligning Intelligence with Humanity.').first).to_be_visible()
    await page.goto('https://aligntic.vercel.app/services')
    await page.get_by_role('link', name='Contact Us').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/contact')
    await expect(page.get_by_role('heading', name='Get in touch').first).to_be_visible()
    await page.goto('https://aligntic.vercel.app/services')
    await page.get_by_role('link', name='Aligntic').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/')
    await expect(page.get_by_role('heading', name='Intelligence,\nbeautifully aligned.').first).to_be_visible()


import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_tc_007_header_navigation_from_about_page(page: Page):
    await page.goto('https://aligntic.vercel.app/about')
    await page.get_by_role('link', name='Products').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/products')
    await expect(page.get_by_role('heading', name='Our AI Products').first).to_be_visible()
    await page.goto('https://aligntic.vercel.app/about')
    await page.get_by_role('link', name='Services').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/services')
    await expect(page.get_by_role('heading', name='AI Consulting & Services').first).to_be_visible()
    await page.goto('https://aligntic.vercel.app/about')
    await page.get_by_role('link', name='Contact Us').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/contact')
    await expect(page.get_by_role('heading', name='Get in touch').first).to_be_visible()
    await page.goto('https://aligntic.vercel.app/about')
    await page.get_by_role('link', name='Aligntic').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/')
    await expect(page.get_by_role('heading', name='Intelligence,\nbeautifully aligned.').first).to_be_visible()


import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_tc_008_header_navigation_from_contact_page(page: Page):
    await page.goto('https://aligntic.vercel.app/contact')
    await page.get_by_role('link', name='Products').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/products')
    await expect(page.get_by_role('heading', name='Our AI Products').first).to_be_visible()
    await page.goto('https://aligntic.vercel.app/contact')
    await page.get_by_role('link', name='Services').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/services')
    await expect(page.get_by_role('heading', name='AI Consulting & Services').first).to_be_visible()
    await page.goto('https://aligntic.vercel.app/contact')
    await page.get_by_role('link', name='About').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/about')
    await expect(page.get_by_role('heading', name='Aligning Intelligence with Humanity.').first).to_be_visible()
    await page.goto('https://aligntic.vercel.app/contact')
    await page.get_by_role('link', name='Aligntic').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/')
    await expect(page.get_by_role('heading', name='Intelligence,\nbeautifully aligned.').first).to_be_visible()


import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_tc_009_header_navigation_from_pulse_finance_product_detail_page(page: Page):
    await page.goto('https://aligntic.vercel.app/products/pulse-finance')
    await page.get_by_role('link', name='Products').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/products')
    await expect(page.get_by_role('heading', name='Our AI Products').first).to_be_visible()
    await page.goto('https://aligntic.vercel.app/products/pulse-finance')
    await page.get_by_role('link', name='Services').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/services')
    await expect(page.get_by_role('heading', name='AI Consulting & Services').first).to_be_visible()
    await page.goto('https://aligntic.vercel.app/products/pulse-finance')
    await page.get_by_role('link', name='About').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/about')
    await expect(page.get_by_role('heading', name='Aligning Intelligence with Humanity.').first).to_be_visible()
    await page.goto('https://aligntic.vercel.app/products/pulse-finance')
    await page.get_by_role('link', name='Contact Us').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/contact')
    await expect(page.get_by_role('heading', name='Get in touch').first).to_be_visible()
    await page.goto('https://aligntic.vercel.app/products/pulse-finance')
    await page.get_by_role('link', name='Aligntic').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/')
    await expect(page.get_by_role('heading', name='Intelligence,\nbeautifully aligned.').first).to_be_visible()


import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_tc_010_products_page_loads_and_main_heading_is_visible(page: Page):
    await page.goto('https://aligntic.vercel.app/products')
    await expect(page.get_by_role('heading', name='Our AI Products').first).to_be_visible()


import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_tc_011_product_headings_are_visible(page: Page):
    await page.goto('https://aligntic.vercel.app/products')
    await expect(page.get_by_role('heading', name='Pulse Finance').first).to_be_visible()
    await expect(page.get_by_role('heading', name='Newsume AI').first).to_be_visible()


import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_tc_012_view_case_study_links_are_visible(page: Page):
    await page.goto('https://aligntic.vercel.app/products')
    await expect(page.get_by_role('link', name='View Case Study').first).to_be_visible()


import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_tc_013_open_pulse_finance_case_study_from_product_listing(page: Page):
    await page.goto('https://aligntic.vercel.app/products')
    await page.get_by_role('link', name='View Case Study').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/products/pulse-finance')
    await expect(page.get_by_role('heading', name='Pulse Finance').first).to_be_visible()


import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_tc_014_product_detail_page_loads_and_main_heading_is_visible(page: Page):
    await page.goto('https://aligntic.vercel.app/products/pulse-finance')
    await expect(page.get_by_role('heading', name='Pulse Finance').first).to_be_visible()


import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_tc_015_core_features_section_heading_is_visible(page: Page):
    await page.goto('https://aligntic.vercel.app/products/pulse-finance')
    await expect(page.get_by_role('heading', name='Core Features').first).to_be_visible()


import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_tc_016_ai_spending_coach_section_heading_is_visible(page: Page):
    await page.goto('https://aligntic.vercel.app/products/pulse-finance')
    await expect(page.get_by_role('heading', name='AI Spending Coach').first).to_be_visible()


import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_tc_017_navigate_back_to_products_listing(page: Page):
    await page.goto('https://aligntic.vercel.app/products/pulse-finance')
    await page.get_by_role('link', name='← Back to Products').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/products')
    await expect(page.get_by_role('heading', name='Our AI Products').first).to_be_visible()


import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_tc_018_services_page_loads_and_main_heading_is_visible(page: Page):
    await page.goto('https://aligntic.vercel.app/services')
    await expect(page.get_by_role('heading', name='AI Consulting & Services').first).to_be_visible()


import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_tc_019_all_service_offering_headings_are_visible(page: Page):
    await page.goto('https://aligntic.vercel.app/services')
    await expect(page.get_by_role('heading', name='Custom LLM Fine-tuning').first).to_be_visible()
    await expect(page.get_by_role('heading', name='AI Integration Architecture').first).to_be_visible()
    await expect(page.get_by_role('heading', name='Edge Deployment Optimization').first).to_be_visible()
    await expect(page.get_by_role('heading', name='AI Automation Workflows').first).to_be_visible()
    await expect(page.get_by_role('heading', name='AI-Powered Analytics & Forecasting').first).to_be_visible()
    await expect(page.get_by_role('heading', name='Multimodal AI Solutions').first).to_be_visible()
    await expect(page.get_by_role('heading', name='Conversational AI Platforms').first).to_be_visible()


import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_tc_020_contact_page_loads_and_main_heading_is_visible(page: Page):
    await page.goto('https://aligntic.vercel.app/contact')
    await expect(page.get_by_role('heading', name='Get in touch').first).to_be_visible()


import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_tc_021_contact_form_fields_and_button_are_visible(page: Page):
    await page.goto('https://aligntic.vercel.app/contact')
    await expect(page.get_by_placeholder('John Doe')).to_be_visible()
    await expect(page.get_by_placeholder('john@example.com')).to_be_visible()
    await expect(page.get_by_placeholder('How can we help you?')).to_be_visible()
    await expect(page.get_by_role('button', name='Send Message').first).to_be_visible()


import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_tc_022_fill_contact_form_with_valid_data(page: Page):
    await page.goto('https://aligntic.vercel.app/contact')
    await page.get_by_placeholder('John Doe').fill('Jane Doe')
    await page.get_by_placeholder('john@example.com').fill('jane@example.com')
    await page.get_by_placeholder('How can we help you?').fill('I would like to learn more about your services.')
    await expect(page.get_by_placeholder('John Doe')).to_have_value('Jane Doe')
    await expect(page.get_by_placeholder('john@example.com')).to_have_value('jane@example.com')
    await expect(page.get_by_placeholder('How can we help you?')).to_have_value('I would like to learn more about your services.')
    await expect(page.get_by_role('heading', name='Get in touch').first).to_be_visible()


import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_tc_023_submit_contact_form_with_valid_data(page: Page):
    await page.goto('https://aligntic.vercel.app/contact')
    await page.get_by_placeholder('John Doe').fill('Jane Doe')
    await page.get_by_placeholder('john@example.com').fill('jane@example.com')
    await page.get_by_placeholder('How can we help you?').fill('I would like to learn more about your services.')
    await expect(page.get_by_placeholder('John Doe')).to_have_value('Jane Doe')
    await expect(page.get_by_placeholder('john@example.com')).to_have_value('jane@example.com')
    await expect(page.get_by_placeholder('How can we help you?')).to_have_value('I would like to learn more about your services.')
    await expect(page.get_by_role('button', name='Send Message').first).to_be_visible()
    await page.get_by_role('button', name='Send Message').first.click()
    await expect(page.get_by_role('heading', name='Get in touch').first).to_be_visible()


import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_tc_024_about_page_loads_and_main_heading_is_visible(page: Page):
    await page.goto('https://aligntic.vercel.app/about')
    await expect(page.get_by_role('heading', name='Aligning Intelligence with Humanity.').first).to_be_visible()

