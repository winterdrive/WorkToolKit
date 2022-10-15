@echo off
for /f "tokens=*" %%a in ('
  "wmic path Win32_LocalTime get year,month,day /value|findstr ="
  ') do @set %%a

set p=1
echo Do You Want To Backup Files From Google Drive To External Device? (y/n)
set /p Input=Enter y or n:
if /I "%Input%"=="y" goto yes
if /I "%Input%"=="n" goto no


:yes
set /p Input=Default Path is D:\ set as default? (y/n)
if /I "%Input%"=="y" goto default
if /I "%Input%"=="n" goto notdefault

:default
mkdir D:\backup_%year%%month%%day%
XCOPY . D:\backup_%year%%month%%day%
Echo Press any key to leave...
pause >nul
exit


:notdefault
set /p Input=Enter the path:
XCOPY . %Input%


:no
Echo Press any key to leave...
pause >nul
exit