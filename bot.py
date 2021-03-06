import nonebot
import config
import logging
from os import path

if __name__ == '__main__':
    nonebot.init(config)
    nonebot.get_bot().logger.setLevel(logging.WARNING)
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'EXplorer', 'plugins'),
        'EXplorer.plugins'
    )
    nonebot.run()
