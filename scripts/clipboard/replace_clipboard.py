import pyperclip


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(prog="Replace text in clipboard")
    parser.add_argument('-f', '--find', default=" ")
    parser.add_argument('-r', '--replace', default=",")
    args = parser.parse_args()
    text = pyperclip.paste().replace(args.find, args.replace)
    pyperclip.copy(text)