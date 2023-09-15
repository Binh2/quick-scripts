import os
import asyncio
import json
from pyppeteer import launch
import traceback

WORD_TYPES = ['noun', 'verb', 'adjective', 'adverb', 'exclamation']
PRONUNCIATION_SELECTOR = '.BNeawe.tAd8D.AP7Wnd'
INFO_SELECTOR = '.Ap5OSd .BNeawe.s3v9rd.AP7Wnd'
CORRECTION_SELECTOR = '#scc i'

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

async def get_words_meanings(urls, args):
    # os.environ["LANG"] = 'en-US'
    browser = await launch({ 
        "autoClose": False,
        "headless": args.no_headless,
        "args": [
            # '--accept-lang="en-US"',
            # '--use-fake-ui-for-media-stream',
        ],
    })
    page = await browser.newPage()
    results = []
    for url in urls:
        meanings = []
        pronunciation = None
        correction = None
        examples = []
        synonyms = []
        types = []
        audio_url = None
        try:
            await page.goto(url)
            if args.pause: await asyncio.sleep(10000)
            try:
                correction_element = await page.querySelector(CORRECTION_SELECTOR)
                if correction_element: correction = await get_text(correction_element)
            except:
                handle_exception()
                
            try:
                pronunciation = await get_text(await page.querySelector(PRONUNCIATION_SELECTOR))
            except:
                handle_exception()
            
            try:
                audio_url = await page.evaluate('() => document.querySelector("audio").src')
            except:
                handle_exception()
            
            try:
                await page.waitForSelector(INFO_SELECTOR)
                info_elements = await page.querySelectorAll(INFO_SELECTOR)
                for info_element in info_elements:
                    try:
                        info = await get_text(info_element)
                        if info.strip().lower() in WORD_TYPES:
                            types.append(info.strip())
                        elif info.strip().startswith('"') and info.strip().endswith('"'):
                            examples.append(info.strip()[1:-1])
                        elif info.strip().startswith('từ đồng nghĩa: '):
                            synonyms.append(info.strip().replace('từ đồng nghĩa: ', '').split(', '))
                        else:
                            meanings.append(info.strip())
                    except:
                        handle_exception()
            except:
                handle_exception()
            meanings = list(filter(lambda x: len(x) > 0, meanings))
            
        finally:
            result = {
                "pronunciation": pronunciation,
                "correction": correction,
                "audio_url": audio_url,
                "meanings": meanings,
                "examples": examples,
                "synonyms": synonyms,
                "types": types,
            }
            print(result)
            results.append(result)
    await browser.close()
    return results

def print_list(label, info):
    if len(info) <= 0: return
    print('{:<15} {:<50}'.format(label, str(info[0])))
    for inf in info[1:]:
        print('{:<15} {:<50}'.format('', str(inf)))
    if len(info[1:]) > 0: print()

def print_result(index, word, correction, meanings, pronunciation, audio_url, examples, synonyms, types):
    print('{:<15} {:<50}'.format(str(index), str(word)))
    if correction:      print('{:<15} {:<50}'.format("Correction", str(correction)))
    print_list("Meanings", meanings)
    print('{:<15} {:<50}'.format("Word types", str(types)))
    print_list("Examples", examples)
    if synonyms:        print_list("Synonyms", synonyms)
    if pronunciation:   print('{:<15} {:<50}'.format("Pronunciation", str(pronunciation)))
    if audio_url:       print('{:<15} {:<50}'.format("Audio url", str(audio_url)))
    print()
    print()
    
def print_results(words, results):
    for index, word, result in zip(range(10000), words, results):
        print_result(index, word, **result)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(prog="Get words' meanings")
    parser.add_argument("-b", "--base-url", default="https://www.google.com/search?q=define+")
    parser.add_argument("-w", '--words', nargs='+', default=[])
    parser.add_argument('-f', '--file-with-words', default='words.txt')
    parser.add_argument('-r', '--reuse-result', action='store_true')
    parser.add_argument('-p', '--pause', action='store_true')
    parser.add_argument('-n', '--number-of-words', type=int, default=100000)
    parser.add_argument('--no-headless', action='store_false')
    parser.add_argument('-i', '--index', help='Start from the ith item in the word list', type=int, default=0)
    parser.add_argument('-m', '--mark', help='Mark the saved filename with a different name to reuse it later', default='')
    args = parser.parse_args()
    
    results_filename = 'words-meanings' +  ('-' if args.mark else '') + args.mark + '.json'
    if args.reuse_result and os.path.exists(results_filename):
        with open(results_filename, 'r') as f:
            text = json.load(f)
            words = text["words"]
            results = text["results"]
            print(words)
            print_results(words, results)
    else:
        words = args.words
        if not words:
            with open(args.file_with_words, 'r') as f:
                words = f.read().split('\n')
        words = words[args.index: args.index+args.number_of_words]
        print(words)
        urls = [ args.base_url + word.replace(' ', '+') for word in words ]
        
        results = asyncio.run(get_words_meanings(urls, args))
        print_results(words, results)
        with open(results_filename, 'w') as f:
            json.dump(
                {
                    "words": words,
                    "results": results
                }, 
                f, indent=4)