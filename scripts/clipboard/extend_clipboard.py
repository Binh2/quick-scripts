import threading
from pynput import keyboard
import os
import time
import win32clipboard
import traceback

def monitor_keyboard(stack):
    alt_pressed = False

    def on_press(key):
        nonlocal alt_pressed
        try:
            if key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
                alt_pressed = True
            elif alt_pressed and key.char == '1':
                set_clipboard(**stack[-1])
            elif alt_pressed and key.char == '2':
                set_clipboard(**stack[-2])
            elif alt_pressed and key.char == '3':
                set_clipboard(**stack[-3])
            elif alt_pressed and key.char == '4':
                set_clipboard(**stack[-4])
            elif alt_pressed and key.char == '5':
                set_clipboard(**stack[-5])
            elif alt_pressed and key.char == '6':
                set_clipboard(**stack[-6])
            elif alt_pressed and key.char == '7':
                set_clipboard(**stack[-7])
            elif alt_pressed and key.char == '8':
                set_clipboard(**stack[-8])
            elif alt_pressed and key.char == '9':
                set_clipboard(**stack[-9])
            elif alt_pressed and key == keyboard.Key.esc:
                return False
        except AttributeError:
            pass
        except:
            handle_exception()

    def on_release(key):
        nonlocal alt_pressed
        if key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
            alt_pressed = False

    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    return listener


def handle_exception(*args, **kwargs):
    string = 'My exception handling: ' + str(args) + ' ' + str(kwargs) + '\n'
    string += traceback.format_exc()
    string = string.split('Backtrace')[0]
    print(string)
    
def get_clipboard(format_dict):
    is_open = False
    try:
        win32clipboard.OpenClipboard()
        is_open = True
        data = None
        format_code = None
        for format_code in format_dict.values():
            try:
                data = win32clipboard.GetClipboardData(format_code)
                break
            except:
                pass
    finally:
        if is_open: win32clipboard.CloseClipboard()
    return { "data": data, "format_code": format_code }

def set_clipboard(data, format_code):
    # is_open = False
    # try:
        # win32clipboard.OpenClipboard()
        # is_open = True
        # win32clipboard.SetClipboardData(format_code, data)
    # finally:
        # if is_open: win32clipboard.CloseClipboard()
    set_clipboard_text(data)

def set_clipboard_text(text):
    is_open = False
    try:
        win32clipboard.OpenClipboard()
        is_open = True
        win32clipboard.SetClipboardText(text)
    finally:
        if is_open: win32clipboard.CloseClipboard()

# def set_clipboard(text):
    # win32clipboard.OpenClipboard()
    # win32clipboard.EmptyClipboard()
    # win32clipboard.SetClipboard(text.encode('utf-8'),
                    # win32clipboard.CF_TEXT)
    # win32clipboard.SetClipboard(unicode(text),
                    # win32clipboard.CF_UNICODETEXT)
    # win32clipboard.CloseClipboard()
    
def watch_clipboard(stack=[], stack_size=30):
    prev_data = get_clipboard(format_dict)
    if prev_data: stack.append(prev_data)
    while True:
        data = get_clipboard(format_dict)
        if data and prev_data != data:
            stack.append(data)
            prev_data = data
            os.system('cls')
            for i, d in zip(range(len(stack)), reversed(stack)):
                print(i+1, d["data"])
        time.sleep(0.1)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(prog='Extend clipboard')
    parser.add_argument('-s', '--stack-size', default=30)
    args = parser.parse_args()
    format_dict = {
        "text": win32clipboard.CF_OEMTEXT, # 7
        # "image": win32clipboard.CF_DIB, # 8
        # "files": win32clipboard.CF_HDROP, # 15
    }
    
    keyboard_listener = None
    clipboard_watcher = None
    stack = []
    try:
        keyboard_listener = monitor_keyboard(stack)
        clipboard_watcher = threading.Thread(target=watch_clipboard, args=(stack, args.stack_size,))
        keyboard_listener.start()
        clipboard_watcher.start()
    except:
        handle_exception()
    finally:
        keyboard_listener.join()
        clipboard_watcher.join()