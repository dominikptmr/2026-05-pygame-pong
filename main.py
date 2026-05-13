import pygame

from settings import *
from game import Game


def main():
    
    pygame.init()
    
    game = Game()

    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False

        game.window.fill(BACKGROUND_COLOR)
    
        score_text = game.score_font.render(f"{game.score}", True, SCORE_FONT_COLOR)
        score_text.set_alpha(SCORE_FONT_OPACITY)
        score_box = score_text.get_rect(center=(WINDOW_SIZE / 2, WINDOW_SIZE / 2))
        game.window.blit(score_text, score_box)
    
        game.paddle.update()
        game.paddle.draw(game.window)

    
        for ball in game.balls[:]:
            ball.update()
            ball.draw(game.window)
        
            ball.check_window_collision()
        
            if ball.check_paddle_collision(game.paddle.hitbox):
                game.increase_score()
                if game.get_score() % 3 == 0:
                    game.add_ball()
        
            if ball.lost():
                game.balls.remove(ball)
            
            if len(game.balls) <= 0:
                game.reset()
        
        pygame.display.flip()
        
        game.clock.tick(FPS)

    pygame.quit()
    
main()