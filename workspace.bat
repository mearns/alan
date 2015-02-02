
@ECHO OFF

start console -w "DEMO ALAN" -d "%~dp0"
start console -w "GIT ALAN" -d "%~dp0"

start cmd /c cd "%~dp0" ^&^& start gvim -p -c ":simalt ~x"

if "%PYTHON_HOME%"=="" GOTO NO_HH
    start hh "%PYTHON_HOME%.\Lib\site-packages\PyWin32.chm"
:NO_HH
