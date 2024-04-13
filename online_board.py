import threading
import socket
from tkinter import Canvas, Button, Label, Frame, messagebox

class GameBoard(Frame):
    def __init__(self, master, is_host, size, ip="127.0.0.1", port=4000, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(fill="both", expand=True)
        self.configure(bg="blue")

        self.is_host = is_host
        self.size = size
        self.ip = ip
        self.port = port
        self.cols = size
        self.rows = size
        
        self.pieces = [[None for _ in range(self.cols)] for _ in range(self.rows)]


        if is_host:
            self.player_color = "yellow"  # Host plays as yellow
            self.opponent_color = "red"   # Client plays as red
            self.current_player = "yellow"  # Host starts the game
        else:
            self.player_color = "red"    # Client plays as red
            self.opponent_color = "yellow"  # Host plays as yellow
            self.current_player = "red"    # Host starts the game, so client waits
        
        self.create_widgets()
        self.setup_network()
        self.bind_events()

    def create_widgets(self):
        turn_text = "Your Turn" if self.is_host else "Waiting for Opponent..."
        self.turn_label = Label(self, text=turn_text, font=("Arial", 16), bg="blue", fg="white")
        self.turn_label.pack(side="top", fill="x", pady=10)

        self.canvas = Canvas(self, bg="blue")
        self.canvas.pack(fill="both", expand=True)

        self.exit_button = Button(self, text="Exit Game", command=self.close_connection)
        self.exit_button.pack(side="bottom", pady=10)

    def setup_network(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.is_host:
            self.socket.bind((self.ip, self.port))
            self.socket.listen(1)
            self.client_socket, addr = self.socket.accept()
            self.connection = self.client_socket
            self.turn_label.config(text="Your Turn")
            self.is_my_turn = True  # Host starts the game
        else:
            self.socket.connect((self.ip, self.port))
            self.connection = self.socket
            self.turn_label.config(text="Waiting for Opponent...")
            self.is_my_turn = False  # Client waits for the host to play

        threading.Thread(target=self.receive_move, daemon=True).start()

    def receive_move(self):
        while True:
            data = self.connection.recv(1024).decode()
            if data:
                self.process_received_move(int(data))

    def process_received_move(self, col):
        self.master.after(0, lambda: self.make_move(col, self.opponent_color))

    def bind_events(self):
        self.canvas.bind("<Button-1>", self.process_turn)

    def process_turn(self, event):
        if not self.is_my_turn:
            return  # Ignore clicks if it's not the local player's turn

        col = int(event.x / (self.canvas.winfo_width() / self.cols))
        if self.make_move(col, self.current_player):
            self.connection.sendall(str(col).encode())
            self.is_my_turn = False
            self.turn_label.config(text="Waiting for Opponent...")

    def make_move(self, col, color):
        for row in reversed(range(self.rows)):
            if self.pieces[row][col] is None:
                self.pieces[row][col] = color
                self.draw_piece(row, col)
                if self.check_winner(row, col):
                    winner = "You win!" if color == self.current_player else "Opponent wins!"
                    messagebox.showinfo("Game Over", winner)
                    self.canvas.unbind("<Button-1>")
                    return False
                self.switch_player()
                return True
        return False

    def switch_player(self):
        self.is_my_turn = not self.is_my_turn  # Toggle turn
        turn_text = "Your Turn" if self.is_my_turn else "Waiting for Opponent..."
        self.turn_label.config(text=turn_text)

    def close_connection(self):
        if hasattr(self, 'client_socket'):
            self.client_socket.close()
        self.socket.close()
        self.master.quit()
    def initialize_board(self):
        self.update_idletasks()  # Makes sure the canvas is ready before drawing
        self.redraw_board()

    def redraw_board(self):
        self.canvas.delete("all")  # Clears the canvas for redrawing
        cell_width = self.canvas.winfo_width() / self.cols
        cell_height = self.canvas.winfo_height() / self.rows
        for row in range(self.rows):
            for col in range(self.cols):
                x1 = col * cell_width + cell_width * 0.1
                y1 = row * cell_height + cell_height * 0.1
                x2 = x1 + cell_width * 0.8
                y2 = y1 + cell_height * 0.8
                self.canvas.create_oval(x1, y1, x2, y2, fill="white", tags="slot")
                if self.pieces[row][col] is not None:  # Only draw if there's a piece there
                    self.draw_piece(row, col, self.pieces[row][col])


    def bind_events(self):
        self.canvas.bind("<Button-1>", self.process_turn)
        self.master.bind("<Configure>", self.on_resize)  # Handles dynamic resizing

    def on_resize(self, event):
        self.redraw_board()

    
    def make_move(self, col, color):
        for row in reversed(range(self.rows)):
            if self.pieces[row][col] is None:
                self.pieces[row][col] = color
                self.draw_piece(row, col, color)
                if self.check_winner(row, col):
                    winner = "Player" if color == self.player_color else "Opponent wins!"
                    messagebox.showinfo("Game Over", f"{winner} wins!")
                    self.canvas.unbind("<Button-1>")
                    return False
                self.switch_player()
                return True
        return False

    
    def draw_piece(self, row, col, color):
        cell_width = self.canvas.winfo_width() / self.cols
        cell_height = self.canvas.winfo_height() / self.rows
        x1 = col * cell_width + cell_width * 0.2
        y1 = row * cell_height + cell_height * 0.2
        x2 = x1 + cell_width * 0.6
        y2 = y1 + cell_height * 0.6
        self.canvas.create_oval(x1, y1, x2, y2, fill=color, tags=f"piece{row}{col}")  # Tag each piece uniquely

    def check_winner(self, row, col):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            for n in range(1, 4):
                r = row + dr * n
                c = col + dc * n
                if (
                    r < 0
                    or r >= self.rows
                    or c < 0
                    or c >= self.cols
                    or self.pieces[r][c] != self.current_player
                ):
                    break
                count += 1
            for n in range(1, 4):
                r = row - dr * n
                c = col - dc * n
                if (
                    r < 0
                    or r >= self.rows
                    or c < 0
                    or c >= self.cols
                    or self.pieces[r][c] != self.current_player
                ):
                    break
                count += 1
            if count >= 4:
                return True
        return False


def create_game_board(size, parent_window, isHost, ip, port):
    game_board = GameBoard(parent_window, is_host=isHost, size=size, ip=ip, port=port)
    game_board.pack(fill="both", expand=True)
