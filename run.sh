#!/bin/bash

VENV_NAME=".venv"

if [ -d "$VENV_NAME" ]; then
    echo "Virtual environment '$VENV_NAME' already exists."
else
    ./install_venv.sh   # 将原 install_venv.bat 改为对应的 Linux 脚本
fi

source "$VENV_NAME/bin/activate"

# 运行 Python 脚本
python main.py

