import sys

import pygame
import random

pygame.init()

# stałe ekranu
WIDTH = 800
HEIGHT = 600
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Topnienie śniegu")
clock = pygame.time.Clock()

# colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)
DARK_BLUE = (20, 30, 50)
ICE_BLUE = (200, 230, 255)
SNOW_DRIFT_COLOR = (220, 235, 255)

class Snowflake:
    def __init__(self):
        self.x = random.randint(20, WIDTH - 20)
        self.y = -10
        self.radius = random.randint(8, 16)
        self.speed = random.uniform(1.5, 3.5 - self.radius / 8)
        self.active = True
        self.melting = False
        self.melt_timer = 0

    def update(self, drifts):
        if self.melting:
            self.melt_timer += 1
            self.radius -= 0.5

            if self.radius <= 0:
                self.active = False
            return

        self.y += self.speed

        # check collision
        column_index = int(self.x // 10)
        if 0 <= column_index < len(drifts):
            ground_y = HEIGHT - drifts[column_index]
            if self.y + self.radius >= ground_y:
                # osiągnął dół lub zaspę - zamienia się w część zaspy
                self.active = False
                # dodanie wysokości do zaspy w tej i sąsiednich kolumnach
                for c in range(max(0, column_index - 5), min(len(drifts), column_index + 6)):
                    drifts[c] += 1.5
                return False # dotarł na dół

        return None

    def draw(self, surface):
        # rysowanie płatka (okrąg/gwiazdka)
        pygame.draw.circle(surface, ICE_BLUE, (int(self.x), int(self.y)), int(max(1, self.radius)))
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), int(max(1, self.radius - 3)))

    def is_clicked(self, position):
        distance_sq = (self.x - position[0])**2 + (self.y - position[1])**2
        return distance_sq <= (self.radius + 5)**2

def main():
    col_width = 10
    num_cols = WIDTH // col_width
    drifts = [0.0] * num_cols

    snowflakes = []
    score = 0
    spawn_timer = 0
    game_over = False

    font = pygame.font.SysFont("Arial", 36)
    big_font = pygame.font.SysFont("Arial", 64)

    while True:
        screen.fill(DARK_BLUE)

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouse_position = pygame.mouse.get_pos()
                # sprawdzanie klikniętych płatków (od góry do dołu, żeby klikać w wierzchnie)
                for flake in reversed(snowflakes):
                    if flake.active and not flake.melting and flake.is_clicked(mouse_position):
                        flake.melting = True
                        score += 1
                        break

            elif event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_r:
                    # Restart gry
                    drifts = [0.0] * num_cols
                    snowflakes = []
                    score = 0
                    spawn_timer = 0
                    game_over = False

        if not game_over:
            # Generowanie nowych płatków
            spawn_timer += 1
            if spawn_timer > 30: # co około 0.5 sekundy
                snowflakes.append(Snowflake())
                spawn_timer = 0

            # aktualizowanie płatków
            for flake in snowflakes[:]:
                if flake.active:
                    updated = flake.update(drifts)
                    # jeśli zaspa doszła do góry
                    if updated is False:
                        max_drift = max(drifts)
                        if max_drift >= HEIGHT - 100:
                            game_over = True

                else:
                    snowflakes.remove(flake)


        # rysowanie zasp śnieżnych
        for i, h in enumerate(drifts):
            if h > 0:
                rect_x = i * col_width
                rect_y = HEIGHT - h
                pygame.draw.rect(screen, SNOW_DRIFT_COLOR, (rect_x, rect_y, col_width, h))


        # rysowanie płatków śniegu
        for flake in snowflakes:
            if flake.active:
                flake.draw(screen)

        # wyświetlanie wyniku
        score_surface = font.render(f"Topione: ({score})", True, WHITE)
        screen.blit(score_surface, (20, 20))

        # ekran końca gry
        if game_over:
            overlay = pygame.Surface(size, pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            screen.blit(overlay, (0, 0))

            over_surf = big_font.render(f"KONIEC GRY! Zaspa cię zasypała w całości", True, WHITE)
            restart_surf = font.render(f"Naciśnij R, aby zagrać ponownie", True, WHITE)

            screen.blit(over_surf, (WIDTH//2 - over_surf.get_width() // 2, HEIGHT//2 - 50))
            screen.blit(restart_surf, (WIDTH//2 - restart_surf.get_width() // 2, HEIGHT//2 + 20))

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()