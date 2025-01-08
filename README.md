# 2048 游戏

这是一个使用 Python 和 Pygame 实现的 2048 游戏。

## Linux 使用方法

### 安装(需要python 3.6 及以上版本)

1. 克隆此仓库：

    ```sh
    git clone https://github.com/Long17369/2048.git
    cd 2048
    ```

2. 创建并激活虚拟环境，并安装依赖项：

    ```sh
    python -m venv venv
    .venv/Scripts/activate
    python -m pip install requirements.txt
    ```

### 运行游戏

在虚拟环境中运行以下命令启动游戏：

```sh
python main.py
```

## Windows 使用方法

下载源码后直接运行目录下 `run.bat` 即可(需要安装python 3.6及以上版本)

## 游戏玩法

- 使用箭头键或者鼠标拖动移动方块。

## 文件结构

- `main.py`：游戏的主入口。
- `snd/`：包含游戏的核心逻辑和常量。
  - `constant.py`：定义游戏中的常量。
  - `core.py`：包含 2048 游戏的核心逻辑。
  - `game.py`：包含游戏类，处理用户输入和游戏更新。
- `install_venv.bat`：用于创建和激活虚拟环境并安装依赖项的脚本。
- `run.bat`：用于运行游戏的脚本。
- `requirements.txt`：列出项目所需的 Python 包。

## 许可证

此项目基于 MIT 许可证，详情请参阅 [LICENSE](LICENSE) 文件。
