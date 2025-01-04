import snd.constant as CONST
from snd.game import Game


if not (CONST and Game):
    raise Exception("snd not imported")
else:
    if __name__ == '__main__':
        game = Game()
    else:
        print("snd imported")
