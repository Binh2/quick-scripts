@echo off
cd C:\cua-Binh\MyPython\Script
cls
set website=youtube
py web_search.py %website% %*
exit