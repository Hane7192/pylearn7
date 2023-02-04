import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

def check():
    global X_score
    global O_score
    global draw_score
    x = False
    i = 0

    # check if all cells are filled
    for row in range(0,3): 
        for col in range (0,3):
            if buttons[row][col].text() != "":
                i += 1

    #check the horizomtal and vertical winning conditions
    for row , col in zip(range(0,3), range(0,3)):
        if buttons[row][0].text() == buttons[row][1].text() == buttons[row][2].text() != "" or buttons[0][col].text() == buttons[1][col].text() == buttons[2][col].text() != "":
            if winner == 1:
                X_score += 1
                main_window.x_score_box.setText(str(X_score))
                main_window.x_score_box.setStyleSheet("color : black; background-color: rgb(213, 122, 193); padding: 12px 28px; margin : 12px 8px; border-radius:8px;")
            else:
                O_score += 1
                main_window.o_score_box.setText(str(O_score))
                main_window.o_score_box.setStyleSheet("color : black; background-color: rgb(182, 199, 236); padding: 12px 28px; margin : 12px 8px; border-radius:8px;")
            
            msg_box = QMessageBox(text = "Player " + str(winner) + " Wins!")
            msg_box.exec()
            x = True

    #check the diagonal winning conditions    
    if buttons[0][0].text() == buttons[1][1].text() == buttons[2][2].text() != "" or buttons[2][0].text() == buttons[1][1].text() == buttons[0][2].text() != "":
        if winner == 1:
            X_score += 1
            main_window.x_score_box.setText(str(X_score))
            main_window.x_score_box.setStyleSheet("color : black; background-color: rgb(213, 122, 193); padding: 12px 28px; margin : 12px 8px; border-radius:8px;")
        else:
            O_score += 1
            main_window.o_score_box.setText(str(O_score))
            main_window.o_score_box.setStyleSheet("color : black; background-color: rgb(182, 199, 236); padding: 12px 28px; margin : 12px 8px; border-radius:8px;")
        
        msg_box = QMessageBox(text = "Player " + str(winner) + " Wins!")
        msg_box.exec()
        
    #check the draw condition    
    elif x == False and i == 9:
        draw_score += 1
        main_window.draw_score_box.setText(str(draw_score))
        main_window.draw_score_box.setStyleSheet("color : black; background-color: rgb(255, 243, 198); padding: 12px 28px; margin : 12px 8px; border-radius:8px;")
        msg_box = QMessageBox(text = "Draw")
        msg_box.exec()
    
def player2_type(type):
    global state

    if type == "player":
        state = "player 2"
    else:
        state = "computer"
    
def new_game():
    global player
    for i in range(3):
        for j in range (3):    
            buttons[i][j].setText(None)
            buttons[i][j].setStyleSheet("background-color: rgb(67, 0, 100); border-radius : 8px; margin: 6px 6px;")
    player = 1
    main_window.turn_box.setText("X turn")
    main_window.turn_box.setStyleSheet("color : rgb(213, 122, 193); background-color: rgb(67, 0, 100); border-radius : 8px; padding: 10px 10px; margin: 6px 6px;")
    
def info():
    info_window.show()
    
def play(row, col):
    global player
    global buttons
    global winner

    if player == 1:
        if buttons[row][col].text() == "":
            buttons[row][col].setText("X")
            buttons[row][col].setStyleSheet("color : rgb(213, 122, 193); background-color: rgb(67, 0, 100); border-radius : 8px; margin: 6px 6px;")
            main_window.turn_box.setText("O turn")
            main_window.turn_box.setStyleSheet("color : rgb(182, 199, 236); background-color: rgb(67, 0, 100); border-radius : 8px; padding: 10px 10px; margin: 6px 6px;")
            player = 2
            winner = 1
            
    elif player == 2:
        if state == "player 2":
            if buttons[row][col].text() == "":
                buttons[row][col].setText("O")
                buttons[row][col].setStyleSheet("color : rgb(182, 199, 236); background-color: rgb(67, 0, 100); border-radius : 8px; margin: 6px 6px;")
                main_window.turn_box.setText("X turn")
                main_window.turn_box.setStyleSheet("color : rgb(213, 122, 193); background-color: rgb(67, 0, 100); border-radius : 8px; padding: 10px 10px; margin: 6px 6px;")
                player = 1
                winner = 2

        elif state == "computer":
            while True:
                rand_row = random.randint(0,2)
                rand_col = random.randint(0,2)
                if buttons[rand_row][rand_col].text() == "":
                    buttons[rand_row][rand_col].setText("O")
                    buttons[rand_row][rand_col].setStyleSheet("color : rgb(182, 199, 236);")
                    main_window.turn_box.setText("X turn")
                    main_window.turn_box.setStyleSheet("color : rgb(213, 122, 193);")
                    player = 1
                    winner = 2
                    break
    check()

app = QApplication([])



loader = QUiLoader()
main_window = loader.load("main.ui")
info_window = loader.load("info.ui")
main_window.show()


player = 1 
X_score = 0
O_score = 0
draw_score = 0


main_window.turn_box.setText("X turn")
main_window.turn_box.setStyleSheet("color : rgb(213, 122, 193); background-color: rgb(67, 0, 100); border-radius : 8px; padding: 10px 10px; margin: 6px 6px;")

buttons = [[main_window.btn_1, main_window.btn_2, main_window.btn_3],
           [main_window.btn_4, main_window.btn_5, main_window.btn_6],
           [main_window.btn_7, main_window.btn_8, main_window.btn_9]] 


for i in range(3):
    for j in range (3):
        buttons[i][j].clicked.connect(partial(play, i , j))

main_window.r_btn_1.clicked.connect(partial(player2_type , "player"))
main_window.r_btn_2.clicked.connect(partial(player2_type , "computer"))
main_window.btn_rst.clicked.connect(new_game)
main_window.btn_info.clicked.connect(info)
app.exec()