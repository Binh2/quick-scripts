import os
import asyncio
import json
from pyppeteer import launch
import traceback

def handle_exception(*args, **kwargs):
    string = 'My exception handling: ' + str(args) + ' ' + str(kwargs) + '\n'
    string += traceback.format_exc()
    string = string.split('Backtrace')[0]
    print(string)

async def get_text(element):
    text = await (await element.getProperty('textContent')).jsonValue()
    return text

# async def get_property(element, property_key):
    # property_value = await (await element.getProperty(property_key)).toString()
    # return property_value

# def change_property(page, selector, property_key, property_value):
    # await page.evaluate('''() => {
        # document.querySelector({selector}).style["{property_key}"] = "{property_value}"
    # }'''.format(selector=selector, property_key=property_key, property_value=property_value))

async def open_chromium(url):
    browser = await launch({ 
        "autoClose": False,
        "headless": args.headless,
    })
    if url:
        page = await browser.newPage()
        page.goto(url)
    return browser

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(prog="Open Chromium")
    parser.add_argument('--headless', action='store_true')
    parser.add_argument('-u', '--url', default='')
    args = parser.parse_args()
    
    asyncio.run(open_chromium(args.url))