import sys

import pygame
import random

pygame.init()

# stałe ekranu
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)

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

    def update(self, drift_manager):
        if self.melting:
            self.radius -= 0.5

            if self.radius <= 0:
                self.active = False
            return None

        self.y += self.speed

        # check collision
        column_index = int(self.x // drift_manager.col_width)
        if 0 <= column_index < drift_manager.num_cols:
            ground_y = HEIGHT - drift_manager.drifts[column_index]
            if self.y + self.radius >= ground_y:
                # osiągnął dół lub zaspę - zamienia się w część zaspy
                self.active = False
                # dodajemy śnieg do zaspy
                drift_manager.add_snow(column_index)
                return False # dotarł na dół

        return None

    def draw(self, surface):
        # rysowanie płatka (okrąg/gwiazdka)
        pygame.draw.circle(surface, ICE_BLUE, (int(self.x), int(self.y)), int(max(1, self.radius)))
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), int(max(1, self.radius - 3)))

    def is_clicked(self, position):
        distance_sq = (self.x - position[0])**2 + (self.y - position[1])**2
        return distance_sq <= (self.radius + 5)**2

class SnowDrift:
    def __init__(self, width, height, col_width=10):
        self.width = width
        self.height = height
        self.col_width = col_width
        self.num_cols = width // col_width
        self.reset()

    def reset(self):
        self.drifts = [0.0] * self.num_cols

    # dodac snieg do zaspy, podwyzszyc w danym miejscu do maximum wysokosc zaspy
    def add_snow(self, center_col):
        # promień uderzenia w którym ma się śnieg rozejść
        radius = 6

        # dodanie śniegu w kształcie paraboli/stożka w miejscu uderzenia
        for c in range(max(0, center_col - radius), min(self.num_cols, center_col + radius + 1)):
            # odległość od środka
            distance = abs(c - center_col)
            # im bliżej środka tym więcej śniegu dodajemy
            increment = max(0.0, 5.0 * (1.0 - distance / (radius + 1)))
            self.drifts[c] += increment

        # wygładzanie (efekt osuwania się śniegu), żeby góry zasp nie były zbyt strome
        # Przechodzimy przez zaspy i wyrównujemy zbyt duże różnice wysokości między sąsiadami
        for i in range(1, self.num_cols - 1):
            diff_left = self.drifts[i] - self.drifts[i - 1]
            diff_right = self.drifts[i] - self.drifts[i + 1]

            # Jeśli różnica wysokości z lewej jest za duża, zsuwamy śnieg na bok
            if diff_left > 4.0:
                excess = (diff_left - 4.0) * 0.5
                self.drifts[i] -= excess
                self.drifts[i - 1] += excess

            # Jeśli różnica wysokości z prawej jest za duża
            if diff_right > 4.0:
                excess = (diff_right - 4.0) * 0.5
                self.drifts[i] -= excess
                self.drifts[i + 1] += excess

    def get_max_height(self):
        return max(self.drifts) if self.drifts else 0

    def draw(self, surface):
        # rysowanie zasp śnieżnych
        for i, h in enumerate(self.drifts):
            if h > 0:
                rect_x = i * self.col_width
                rect_y = HEIGHT - h
                pygame.draw.rect(surface, SNOW_DRIFT_COLOR, (rect_x, rect_y, self.col_width, h))


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SIZE)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Topnienie śniegu - Zamieć")

        self.font = pygame.font.SysFont("Arial", 36)
        self.big_font = pygame.font.SysFont("Arial", 42)

        self.drift_manager = SnowDrift(WIDTH, HEIGHT, col_width=10)
        self.snowflakes = []
        self.score = 0
        self.spawn_timer = 0
        self.game_over = False

    def reset_game(self):
        self.drift_manager.reset()
        self.snowflakes.clear()
        self.score = 0
        self.spawn_timer = 0
        self.game_over = False

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                mouse_position = pygame.mouse.get_pos()
                # sprawdzanie klikniętych płatków (od góry do dołu, żeby klikać w wierzchnie)
                for flake in reversed(self.snowflakes):
                    if flake.active and not flake.melting and flake.is_clicked(mouse_position):
                        flake.melting = True
                        self.score += 1
                        break

            elif event.type == pygame.KEYDOWN and self.game_over:
                if event.key == pygame.K_r:
                    self.reset_game()

    def update(self):
        if not self.game_over:
            # Generowanie nowych płatków
            self.spawn_timer += 1
            if self.spawn_timer > 2: # co około 0.25 sekundy
                self.snowflakes.append(Snowflake())
                self.spawn_timer = 0

            # aktualizowanie płatków
            for flake in self.snowflakes[:]:
                if flake.active:
                    updated = flake.update(self.drift_manager)
                    # jeśli zaspa doszła do góry
                    if updated is False:
                        if self.drift_manager.get_max_height() >= HEIGHT - 80:
                            self.game_over = True

                else:
                    self.snowflakes.remove(flake)

    def draw(self):
        self.screen.fill(DARK_BLUE)

        # Rysowanie płatków śniegu
        self.drift_manager.draw(self.screen)
        for flake in self.snowflakes:
            if flake.active:
                flake.draw(self.screen)

        # Wynik
        score_surface = self.font.render(f"Wynik: ({self.score})", True, WHITE)
        self.screen.blit(score_surface, (20, 20))

        # Ekran końca gry
        if self.game_over:
            overlay = pygame.Surface(SIZE, pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            self.screen.blit(overlay, (0, 0))

            over_surf = self.big_font.render(f"KONIEC GRY! Zaspa cię zasypała w całości", True, WHITE)
            restart_surf = self.font.render(f"Naciśnij R, aby zagrać ponownie", True, WHITE)

            self.screen.blit(over_surf, (WIDTH//2 - over_surf.get_width() // 2, HEIGHT//2 - 50))
            self.screen.blit(restart_surf, (WIDTH//2 - restart_surf.get_width() // 2, HEIGHT//2 + 20))

        pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.run()