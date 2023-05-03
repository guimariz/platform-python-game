import pygame

class UI:
  def __init__(self, surface):
    
    # setup
    self.display_surface = surface

    # health
    self.health_bar = pygame.image.load('../assets/graphics/ui/health_bar.png').convert_alpha()

    # coins
    self.coin = pygame.image.load('../assets/graphics/ui/coin.png').convert_alpha()
    self.coin_rect = self.coin.get_rect(topleft = (50, 61))
    self.font = pygame.font.Fonte('../assets/graphics/ui/ARCADEPI.ttf', 30)

  def show_health(self, current, full):
    self.display_surface.blit(self.health_bar, (20, 10))

  def show_coins( self, amount):
    self.display_surface.blit(self.coin, self.coin_rect)
    coin_amount_surface = self.font.render(amount, False, )