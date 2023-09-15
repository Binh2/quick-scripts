@echo off
cd C:\cua-Binh\MyPython\Script
cls
set website=papago
py web_search.py %website% %*
exit