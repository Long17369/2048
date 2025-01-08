@echo off
setlocal

set VENV_NAME=.venv

REM 检查虚拟环境目录是否存在
if exist %VENV_NAME%\ ( 
    echo Virtual environment '%VENV_NAME%' already exists.
) else (
    install_venv.bat
)

REM 激活虚拟环境
call %VENV_NAME%\Scripts\activate

python main.py

endlocal