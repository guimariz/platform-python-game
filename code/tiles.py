import pygame
from support import import_folder

class Tile(pygame.sprite.Sprite):
  def __init__(self, x, y, size):
    super().__init__()
    self.image = pygame.Surface((size, size))
    self.rect = self.image.get_rect(topleft = (x, y))
  
  def update(self, x_shift):
    self.rect.x += x_shift

class StaticTile(Tile):
  def __init__(self, x, y, size, surface):
    super().__init__(x, y, size)
    self.image = surface

class Crate(StaticTile):
  def __init__(self, x, y, size):    
    super().__init__(x, y, size, pygame.image.load('../assets/graphics/terrain/crate.png').convert_alpha())
    offset_y = y + size
    self.rect = self.image.get_rect(bottomleft = (x, offset_y))

class AnimatedTile(Tile):
	def __init__(self, x, y, size, path):
		super().__init__(x, y, size)
		self.frames = import_folder(path)
		self.frame_index = 0
		self.image = self.frames[self.frame_index]

	def animate(self):
		self.frame_index += 0.15
		if self.frame_index >= len(self.frames):
			self.frame_index = 0
		self.image = self.frames[int(self.frame_index)]

	def update(self,shift):
		self.animate()
		self.rect.x += shift