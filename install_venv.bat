@echo off
setlocal

REM 定义常量
if "%VENV_NAME%"=="" (
    set VENV_NAME=.venv
    echo 2
)
if "%REQUIREMENTS_FILE%"=="" set REQUIREMENTS_FILE=requirements.txt
if "%PYTHON_CMD%"=="" set PYTHON_CMD=python

REM 检查虚拟环境目录是否存在
if exist %VENV_NAME%\ (
    echo Virtual environment '%VENV_NAME%' already exists.
) else (
    REM 创建虚拟环境
    echo Creating virtual environment '%VENV_NAME%'...
    %PYTHON_CMD% -m venv %VENV_NAME%
)

REM 激活虚拟环境
call %VENV_NAME%\Scripts\activate

REM 安装依赖项
echo Installing dependencies from '%REQUIREMENTS_FILE%'...
pip install -r %REQUIREMENTS_FILE%

REM 输出提示信息
echo Setup complete.

endlocal