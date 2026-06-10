from src import CONST, Game


if not (CONST and Game):
    raise Exception("src not imported")
else:
    game = Game()
