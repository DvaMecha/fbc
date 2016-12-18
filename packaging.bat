start /wait pyinstaller --paths E:/Python/Python35/Lib/site-packages/PyQt5/Qt/bin;E:/gitstore/fbc;E:/gitstore/fbc/Crawler;E:/Python/Python35;E:/Python/Python35/Lib/site-packages/requests; -F -w main.py
start /wait xcopy %cd%\res\*.* %cd%\dist\res\ /s
start /wait xcopy %cd%\datamodel.json %cd%\dist\
md %cd%\dist\output & pause
exit