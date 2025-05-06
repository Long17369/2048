import pygame
import snd.constant as CONST


class Draw:
    def __init__(
        self, screen: pygame.Surface, width_count: int, height_count: int, size: tuple[int, int]
    ) -> None:
        cell_size = (size[0]/width_count,size[1]/height_count)
        self.screen = screen
        self.surface = pygame.Surface(size)
        self.set = [
            [Cell((i*cell_size[0], j*cell_size[1], cell_size[0], cell_size[1])) for i in range(width_count)]
            for j in range(height_count)
        ]
        pass

    def flash(self) -> pygame.Surface:
        for i in self.set:
            for j in i:
                self.surface.blit(j.image, j.rect)
        return self.surface

    def set_update(self, set: list[list[int]]) -> None:
        for y in range(len(self.set)):
            for x in range(len(self.set[y])):
                self.set[y][x].update(set[y][x])
        return

class Cell(pygame.sprite.Sprite):
    LEFT = float
    TOP = float
    WIDTH = float
    HEIGHT = float
    def __init__(self, rect: tuple[LEFT, TOP, WIDTH, HEIGHT]) -> None:
        super().__init__()
        self.rect = pygame.Rect(rect)
        self.center = (int(rect[2] / 2), int(rect[3] / 2))
        self.size = self.rect.size
        self.image = pygame.Surface(self.size)
        self.font = pygame.font.Font(None, 36)
        self.value = -1
        self.update(0)
        pass

    def update(self, value: int) -> None:
        self.value = value
        self.image.fill(CONST.CELL_COLOR[self.value])
        if self.value != 0:
            self.text = self.font.render(str(1 << self.value), True, (0, 0, 0))
            self.text_rect = self.text.get_rect()
            self.text_rect.center = self.center
            self.image.blit(self.text, self.text_rect)
        return
