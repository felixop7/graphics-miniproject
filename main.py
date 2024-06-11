import pygame
from render import Renderer
from game import TicTacToe
from OpenGL.GL import *
from OpenGL.GLUT import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600), pygame.OPENGL | pygame.DOUBLEBUF)
    pygame.display.set_caption("Tic-Tac-Toe")

    renderer = Renderer()
    game = TicTacToe()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                game.handle_click(x, y)
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        renderer.render(game)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
