import re
import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_tc_001(page: Page):
    await page.goto('https://aligntic.vercel.app/')
    await expect(page.get_by_role('link', name='Aligntic').first).to_be_visible()
    await expect(page.get_by_role('link', name='Products').first).to_be_visible()
    await expect(page.get_by_role('link', name='Services').first).to_be_visible()
    await expect(page.get_by_role('link', name='About').first).to_be_visible()
    await expect(page.get_by_role('link', name='Contact Us').first).to_be_visible()


@pytest.mark.asyncio
async def test_tc_002(page: Page):
    await page.goto('https://aligntic.vercel.app/')
    await page.get_by_role('link', name='Products').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/products')
    await expect(page.get_by_role('heading', name='Our AI Products').first).to_be_visible()


@pytest.mark.asyncio
async def test_tc_003(page: Page):
    await page.goto('https://aligntic.vercel.app/')
    await page.get_by_role('link', name='Services').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/services')
    await expect(page.get_by_role('heading', name='AI Consulting & Services').first).to_be_visible()


@pytest.mark.asyncio
async def test_tc_004(page: Page):
    await page.goto('https://aligntic.vercel.app/')
    await page.get_by_role('link', name='About').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/about')
    await expect(page.get_by_role('heading', name='Aligning Intelligence with Humanity.').first).to_be_visible()


@pytest.mark.asyncio
async def test_tc_005(page: Page):
    await page.goto('https://aligntic.vercel.app/')
    await page.get_by_role('link', name='Contact Us').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/contact')
    await expect(page.get_by_role('heading', name='Get in touch').first).to_be_visible()


@pytest.mark.asyncio
async def test_tc_006(page: Page):
    await page.goto('https://aligntic.vercel.app/products')
    await page.get_by_role('link', name='Aligntic').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/')
    await expect(page.get_by_role('heading', name='Intelligence, beautifully aligned.').first).to_be_visible()


@pytest.mark.asyncio
async def test_tc_007(page: Page):
    await page.goto('https://aligntic.vercel.app/products')
    await page.get_by_role('link', name='Services').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/services')
    await expect(page.get_by_role('heading', name='AI Consulting & Services').first).to_be_visible()


@pytest.mark.asyncio
async def test_tc_008(page: Page):
    await page.goto('https://aligntic.vercel.app/about')
    await page.get_by_role('link', name='Contact Us').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/contact')
    await expect(page.get_by_role('heading', name='Get in touch').first).to_be_visible()


@pytest.mark.asyncio
async def test_tc_009(page: Page):
    await page.goto('https://aligntic.vercel.app/')
    await expect(page.get_by_role('heading', name='Intelligence, beautifully aligned.').first).to_be_visible()


@pytest.mark.asyncio
async def test_tc_010(page: Page):
    await page.goto('https://aligntic.vercel.app/')
    await page.get_by_role('link', name='View Products').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/products')
    await expect(page.get_by_role('heading', name='Our AI Products').first).to_be_visible()


@pytest.mark.asyncio
async def test_tc_011(page: Page):
    await page.goto('https://aligntic.vercel.app/')
    await page.get_by_role('link', name='Our Services').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/services')
    await expect(page.get_by_role('heading', name='AI Consulting & Services').first).to_be_visible()


@pytest.mark.asyncio
async def test_tc_012(page: Page):
    await page.goto('https://aligntic.vercel.app/products')
    await expect(page.get_by_role('heading', name='Our AI Products').first).to_be_visible()
    await expect(page.get_by_role('heading', name='Pulse Finance').first).to_be_visible()
    await expect(page.get_by_role('heading', name='Newsume AI').first).to_be_visible()


@pytest.mark.asyncio
async def test_tc_013(page: Page):
    await page.goto('https://aligntic.vercel.app/products')
    await page.get_by_role('link', name='View Case Study').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/products/pulse-finance')
    await expect(page.get_by_role('heading', name='Pulse Finance').first).to_be_visible()
    await expect(page.get_by_role('heading', name='Core Features').first).to_be_visible()


@pytest.mark.asyncio
async def test_tc_014(page: Page):
    await page.goto('https://aligntic.vercel.app/products')
    await expect(page.get_by_role('link', name='View Case Study')).to_have_count(2)
    await expect(page.get_by_role('heading', name='Pulse Finance').first).to_be_visible()
    await expect(page.get_by_role('heading', name='Newsume AI').first).to_be_visible()


@pytest.mark.asyncio
async def test_tc_015(page: Page):
    await page.goto('https://aligntic.vercel.app/products/pulse-finance')
    await expect(page.get_by_role('heading', name='Pulse Finance').first).to_be_visible()
    await expect(page.get_by_role('heading', name='Core Features').first).to_be_visible()
    await expect(page.get_by_role('heading', name='AI Spending Coach').first).to_be_visible()


@pytest.mark.asyncio
async def test_tc_016(page: Page):
    await page.goto('https://aligntic.vercel.app/products/pulse-finance')
    await page.get_by_role('link', name='← Back to Products').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/products')
    await expect(page.get_by_role('heading', name='Our AI Products').first).to_be_visible()


@pytest.mark.asyncio
async def test_tc_017(page: Page):
    await page.goto('https://aligntic.vercel.app/services')
    await expect(page.get_by_role('heading', name='AI Consulting & Services').first).to_be_visible()


@pytest.mark.asyncio
async def test_tc_018(page: Page):
    await page.goto('https://aligntic.vercel.app/services')
    await expect(page.get_by_role('heading', name='Custom LLM Fine-tuning').first).to_be_visible()
    await expect(page.get_by_role('heading', name='AI Integration Architecture').first).to_be_visible()
    await expect(page.get_by_role('heading', name='Edge Deployment Optimization').first).to_be_visible()
    await expect(page.get_by_role('heading', name='AI Automation Workflows').first).to_be_visible()
    await expect(page.get_by_role('heading', name='AI-Powered Analytics & Forecasting').first).to_be_visible()
    await expect(page.get_by_role('heading', name='Multimodal AI Solutions').first).to_be_visible()
    await expect(page.get_by_role('heading', name='Conversational AI Platforms').first).to_be_visible()


@pytest.mark.asyncio
async def test_tc_019(page: Page):
    await page.goto('https://aligntic.vercel.app/about')
    await expect(page.get_by_role('heading', name='Aligning Intelligence with Humanity.').first).to_be_visible()


@pytest.mark.asyncio
async def test_tc_020(page: Page):
    await page.goto('https://aligntic.vercel.app/about')
    await page.get_by_role('link', name='Contact Us').first.click()
    await expect(page).to_have_url('https://aligntic.vercel.app/contact')
    await expect(page.get_by_role('heading', name='Get in touch').first).to_be_visible()


@pytest.mark.asyncio
async def test_tc_021(page: Page):
    await page.goto('https://aligntic.vercel.app/contact')
    await expect(page.get_by_role('heading', name='Get in touch').first).to_be_visible()
    await expect(page.get_by_placeholder('John Doe')).to_be_visible()
    await expect(page.get_by_placeholder('john@example.com')).to_be_visible()
    await expect(page.get_by_placeholder('How can we help you?')).to_be_visible()
    await expect(page.get_by_role('button', name='Send Message')).to_be_visible()


@pytest.mark.asyncio
async def test_tc_022(page: Page):
    await page.goto('https://aligntic.vercel.app/contact')
    await page.get_by_placeholder('John Doe').fill('Jane Doe')
    await page.get_by_placeholder('john@example.com').fill('jane@example.com')
    await page.get_by_placeholder('How can we help you?').fill('Hello, I need help.')
    await page.get_by_role('button', name='Send Message').click()
    await expect(page.get_by_placeholder('John Doe')).to_have_value('Jane Doe')
    await expect(page.get_by_placeholder('john@example.com')).to_have_value('jane@example.com')
    await expect(page.get_by_placeholder('How can we help you?')).to_have_value('Hello, I need help.')
    await expect(page.get_by_role('button', name='Send Message')).to_be_visible()


@pytest.mark.asyncio
async def test_tc_023(page: Page):
    await page.goto('https://aligntic.vercel.app/contact')
    await page.get_by_role('button', name='Send Message').click()
    await expect(page).to_have_url('https://aligntic.vercel.app/contact')
    await expect(page.get_by_role('button', name='Send Message')).to_be_visible()


@pytest.mark.asyncio
async def test_tc_024(page: Page):
    await page.goto('https://aligntic.vercel.app/contact')
    await page.get_by_placeholder('John Doe').fill('Jane Doe')
    email = page.get_by_placeholder('john@example.com')
    await email.fill('not-an-email')
    await page.get_by_placeholder('How can we help you?').fill('Hello')
    await page.get_by_role('button', name='Send Message').click()
    assert not await email.evaluate('el => el.checkValidity()')
    await expect(page).to_have_url('https://aligntic.vercel.app/contact')
    await expect(page.get_by_role('button', name='Send Message')).to_be_visible()


@pytest.mark.asyncio
async def test_tc_025(page: Page):
    await page.goto('https://aligntic.vercel.app/contact')
    email = page.get_by_placeholder('john@example.com')
    await email.fill('valid@example.com')
    await page.get_by_role('button', name='Send Message').click()
    await expect(page).to_have_url('https://aligntic.vercel.app/contact')
    await expect(email).to_have_value('valid@example.com')
    await expect(page.get_by_role('button', name='Send Message')).to_be_visible()

