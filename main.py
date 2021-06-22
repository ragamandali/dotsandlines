from tkinter import *


size_of_board = 600
number_of_dots = 6
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 50
dot_color = '#98D933'
player1_color = '#256CD1'
player1_color_light = '#3E73BD'
player2_color = '#CB0E91'
player2_color_light = '#C6409D'
Green_color = '#98D933'



distance_between_dots = size_of_board/number_of_dots

dot_width = (0.25*distance_between_dots)

edge_width = (0.10*distance_between_dots)

window = Tk()
window.title('Dots and Line Game')
canvas = Canvas(window, width=size_of_board, height=size_of_board)
canvas.pack()
window.mainloop(30)

#Rows
canvas.create_line(50, 50, 550, 50, fill='gray', dash = (2,2))
canvas.create_line(50, 150, 550, 150, fill='gray', dash = (2,2))
canvas.create_line(50, 250, 550, 250, fill='gray', dash = (2,2))
canvas.create_line(50, 350, 550, 350, fill='gray', dash = (2,2))
canvas.create_line(50, 450, 550, 450, fill='gray', dash = (2,2))
canvas.create_line(50, 550, 550, 550, fill='gray', dash = (2,2))

#Columns
canvas.create_line(50, 50, 50, 550, fill='gray', dash=(2,2))
canvas.create_line(150, 50, 150, 550, fill='gray', dash=(2,2))
canvas.create_line(250, 50, 250, 550, fill='gray', dash=(2,2))
canvas.create_line(350, 50, 350, 550, fill='gray', dash=(2,2))
canvas.create_line(450, 50, 450, 550, fill='gray', dash=(2,2))
canvas.create_line(550, 50, 550, 550, fill='gray', dash=(2,2))