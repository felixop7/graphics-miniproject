from OpenGL.GL import *
from OpenGL.GLUT import *
import pygame

class Renderer:
    def __init__(self):
        glClearColor(1.0, 1.0, 1.0, 1.0)
        glColor3f(0.0, 0.0, 0.0)
        glLineWidth(5)
        self.font = pygame.font.Font(None, 144)

    def render(self, game):
        self.draw_grid()
        self.draw_board(game.board, game)
        if game.winner:
            self.draw_winner(game.winner)
        elif self.check_draw(game.board):
            self.draw_draw_message()

    def draw_grid(self):
        glBegin(GL_LINES)
        for i in range(1, 3):
            glVertex2f(i * 200 / 300 - 1, -1)
            glVertex2f(i * 200 / 300 - 1, 1)
            glVertex2f(-1, i * 200 / 300 - 1)
            glVertex2f(1, i * 200 / 300 - 1)
        glEnd()

    def draw_board(self, board, game):
        game_over = True
        for row in range(3):
            for col in range(3):
                if board[row][col] != '':
                    self.draw_text(board[row][col], col * 200 + 70, row * 200 + 150)
                else:
                    game_over = False

    def draw_text(self, text, x, y):
        surface = self.font.render(text, True, (0, 0, 0), (255, 255, 255))
        data = pygame.image.tostring(surface, "RGBA", True)
        glRasterPos2f((x - 300) / 300, (300 - y) / 300)
        glDrawPixels(surface.get_width(), surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, data)

    def draw_winner(self, winner):
        if winner == 'Draw':
            surface = self.font.render("It's a Draw!", True, (255, 0, 0), (255, 255, 255))
        else:
            surface = self.font.render(f"{winner} Wins!", True, (0, 255, 0), (255, 255, 255))
        data = pygame.image.tostring(surface, "RGBA", True)
        glRasterPos2f(-0.6, -0.2)
        glDrawPixels(surface.get_width(), surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, data)
    
    def draw_draw_message(self):
        surface = self.font.render("It's a Draw!", True, (255, 0, 0), (255, 255, 255))
        data = pygame.image.tostring(surface, "RGBA", True)
        glRasterPos2f(-0.9, -0.2)
        glDrawPixels(surface.get_width(), surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, data)

    def check_draw(self, board):
        for row in board:
            for cell in row:
                if cell == '':
                    return False
        return True


class TicTacToe:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None

    def handle_click(self, x, y):
        if self.winner:
            return

        row, col = y // 200, x // 200
        if self.board[row][col] == '':
            self.board[row][col] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
            elif all(self.board[r][c] != '' for r in range(3) for c in range(3)):
                self.winner = 'Draw'
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] == self.current_player:
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == self.current_player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current_player:
            return True
        return False
