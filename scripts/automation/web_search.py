import utilities
import sys
import time

## web_search google/youtube/ggstrans/jisho/wiktionary/mazii/papago

##utilities.search_on_browser('https://google.com/search?q=', '+')
##utilities.search_kanji_on_browser('https://jisho.org/search/', '')
##utilities.search_kanji_on_browser('https://mazii.net/search/word?dict=javi&hl=en-US&query=', '')

web_search = {
    "google": ('https://google.com/search?q=', '+'),
    "youtube": ('https://www.youtube.com/results?search_query=', '+'),
    "ggtrans": ('https://translate.google.com/?sl=ja&tl=vi&op=translate&text=', '')
}

kanji_search = {
    "jisho": ('https://jisho.org/search/', ''),
    "wiktionary": ("https://en.wiktionary.org/wiki/", ""),
    "mazii": ("https://mazii.net/search/kanji?dict=javi&query=", ""),
    "papago": ("https://papago.naver.com/?sk=auto&tk=en&st=", "")
}

website_result = ""
is_web_search = True
key = sys.argv[1]
if key in web_search:
    website_result = key
elif key in kanji_search:
    website_result = key
    is_web_search = False


browser = "edge" ## "edge" or "chrome"
if website_result != "":
    if is_web_search:
        utilities.search_on_browser(*search[website_result], browser)
    else:
        utilities.search_kanji_on_browser(*kanji_search[website_result], browser)

##def my_search(search):
##    for web in search:
##        if web == sys.argv[1]:
##            utilities.search_on_browser(*search[web], browser)
##            return False
##    return True
##
##
##if my_search(web_search):
##    for web in kanji_search:
##        if web == sys.argv[1]:
##            utilities.search_kanji_on_browser(*kanji_search[web], browser)

