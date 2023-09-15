import sys
import webbrowser
import pyperclip
import win32api, win32con, win32gui
import time
import ctypes

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    time.sleep(0.03)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    

def minimize_window():
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )

ranges = [
    {"from": ord(u"\u3300"), "to": ord(u"\u33ff")},         # compatibility ideographs
    {"from": ord(u"\ufe30"), "to": ord(u"\ufe4f")},         # compatibility ideographs
    {"from": ord(u"\uf900"), "to": ord(u"\ufaff")},         # compatibility ideographs
    {"from": ord(u"\U0002F800"), "to": ord(u"\U0002fa1f")}, # compatibility ideographs
    {'from': ord(u'\u3040'), 'to': ord(u'\u309f')},         # Japanese Hiragana
    {"from": ord(u"\u30a0"), "to": ord(u"\u30ff")},         # Japanese Katakana
    {"from": ord(u"\u2e80"), "to": ord(u"\u2eff")},         # cjk radicals supplement
    {"from": ord(u"\u4e00"), "to": ord(u"\u9fff")},
    {"from": ord(u"\u3400"), "to": ord(u"\u4dbf")},
    {"from": ord(u"\U00020000"), "to": ord(u"\U0002a6df")},
    {"from": ord(u"\U0002a700"), "to": ord(u"\U0002b73f")},
    {"from": ord(u"\U0002b740"), "to": ord(u"\U0002b81f")},
    {"from": ord(u"\U0002b820"), "to": ord(u"\U0002ceaf")}  # included as of Unicode 8.0
]

def is_cjk(char):
    return any([range["from"] <= ord(char) <= range["to"] for range in ranges])
    
    
def is_kana(char):
    return any([range["from"] <= ord(char) <= range["to"] for range in ranges[4:6]])


def remove_kana(string):
    if string == "": 
        return ""
    if is_kana(string[0]): 
        return remove_kana(string[1:])
    return string[0] + remove_kana(string[1:])


def has_cjk(string):
    for char in string:
        if is_cjk(char):
            return True
    return False


def open_chrome(address = ""):
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(r"C:\Program Files\Google\Chrome\Application\chrome.exe"))
    webbrowser.get('chrome').open(address)


def open_ms_edge(address = ""):
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
    webbrowser.get('edge').open(address)


def search_on_browser(search_path, connecting_char, browser = "edge"):
    if len(sys.argv) > 2:
        search_for = connecting_char.join(sys.argv[2:])
    else:
        search_for = pyperclip.paste().replace(" ", connecting_char)
    
    address = search_path + search_for
    if browser == "edge":
        open_ms_edge(address)
    elif browser == "chrome":
        open_chrome(address)
        
    
def search_kanji_on_browser(search_path, connecting_char, browser = "edge"):
    if len(sys.argv) > 2:
        search_for = connecting_char.join(sys.argv[2:])
    else:
        search_for = pyperclip.paste().replace(" ", connecting_char)
        
    if has_cjk(search_for):
        address = search_path + remove_kana(search_for)
        if browser == "edge":
            open_ms_edge(address)
        elif browser == "chrome":
            open_chrome(address)


        
