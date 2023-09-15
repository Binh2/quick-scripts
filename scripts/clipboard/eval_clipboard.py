import pyperclip

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(prog='Eval clipboard')
    parser.add_argument('-e', '--eval')
    args = parser.parse_args()
    text = args.eval
    if not text: text = pyperclip.paste()
    
    result = eval(text)
    print(result)
    pyperclip.copy(result)
    