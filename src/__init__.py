import src.constant as CONST
from src.game import Game


if not (CONST and Game):
    raise Exception("src not imported")
else:
    if __name__ == '__main__':
        game = Game()
    else:
        print("src imported")
