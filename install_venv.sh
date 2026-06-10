#!/bin/bash

# 定义常量（使用默认值）
if [ -z "$VENV_NAME" ]; then
    VENV_NAME=".venv"
    echo "2"   # 保持与原脚本一致的行为（输出数字2）
fi

if [ -z "$REQUIREMENTS_FILE" ]; then
    REQUIREMENTS_FILE="requirements.txt"
fi

if [ -z "$PYTHON_CMD" ]; then
    PYTHON_CMD="python3"
fi

# 检查虚拟环境目录是否存在
if [ -d "$VENV_NAME" ]; then
    echo "Virtual environment '$VENV_NAME' already exists."
else
    # 创建虚拟环境
    echo "Creating virtual environment '$VENV_NAME'..."
    $PYTHON_CMD -m venv "$VENV_NAME"
fi

# 激活虚拟环境（Linux 下使用 source）
source "$VENV_NAME/bin/activate"

# 安装依赖项
echo "Installing dependencies from '$REQUIREMENTS_FILE'..."
pip install -r "$REQUIREMENTS_FILE"

# 输出提示信息
echo "Setup complete."
