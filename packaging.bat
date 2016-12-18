start /wait pyinstaller --paths E:/Python/Python35/Lib/site-packages/PyQt5/Qt/bin;F:\百度云同步盘\工作区\workspace\py\fbcrawler;E:/Python/Python35;E:/Python/Python35/Lib/site-packages/requests; -F -w main.py
start /wait xcopy %cd%\res\*.* %cd%\dist\res\ /s
start /wait xcopy %cd%\datamodel.json %cd%\dist\
start /wait md %cd%\dist\output & pause
exit