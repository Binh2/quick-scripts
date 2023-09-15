@echo off
cd C:\cua-Binh\MyPython\Script
cls
set website=jisho
py web_search.py %website% %*
exit