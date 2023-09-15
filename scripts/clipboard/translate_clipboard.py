import pyperclip
from translate import Translator
import argostranslate.package
import argostranslate.translate

def download_offline_translator():
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
        )
    )
    argostranslate.package.install_from_path(package_to_install.download())

def offline_translate(text, from_code="ja", to_code="en", download=False):
    if download: download_offline_translator()
    translatedText = argostranslate.translate.translate(text, from_code, to_code)
    return translatedText

def online_translate(text, from_code, to_code):
    translator = Translator(from_lang=from_code, to_lang=to_code)
    translated = translator.translate(text)
    return translated

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(prog='Translate text from clipboard')
    parser.add_argument('-f', '--from-code', default='ja')
    parser.add_argument('-t', '--to-code', default='en')
    # parser.add_argument('-d', '--download', help='Download the offline translator', action='store_true')
    parser.add_argument('-on', '--online', action='store_true')
    args = parser.parse_args()
    text = pyperclip.paste()
    translated = None
    if args.online:
        translated = online_translate(text, args.from_code, args.to_code)
    else:
        try:
            translated = offline_translate(text, args.from_code, args.to_code, True)
        except:
            translated = online_translate(text, args.from_code, args.to_code)
    pyperclip.copy(str(translated))
    print(translated)