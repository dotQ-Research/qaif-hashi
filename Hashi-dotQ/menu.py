from datetime import datetime
from core.gameElements import Button
from core.game import *
from core.solver import *
import os
import datetime

pygame.init()

position = ((width/2),(height/3))
# ----------------- AUX METHODS ----------------------
def btn(btn: Button, act_when_clicked, param = None, is_quit = False) -> Button:
    btn.show()
    btn.backlight()

    if btn.is_clicked(): 
        if param!=None: act_when_clicked(param) 
        else: act_when_clicked()
        if is_quit: quit()
    return btn

def set_game(s: str) -> None:
    g = Game(s)
    g.board.generate_default_board()
    g.board.random_board()
    g.board.set_neighbors()
    g.board.set_close_neighbors()
    g.board.set_bridges()
    if s == "hard": ui_lvl2_explain(g)
    else: ui_lvl1_explain(g)

def check_iter() -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.event.post(event)
    game_display.blit(load_file(), (0, 0))

# ------------------ GAMELOOP AUX METHODS ------------------------

def gl_check_iter(g: Game, clicked_list: list) -> list:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        z = g.board.update(event)
        if z is not None:
            clicked_list.append(z)
    game_display.fill(blur_green)
    return clicked_list

def btn_hint_clicked(g: Game):
    if g.number_of_hints >= 2:
        text_display("Without orientation", 25, dark_green, (710, 240))
        pygame.display.update()

    else:
        g.number_of_hints += 1
        j = 0
        while g.board.list_bridge[j] in g.board.user_list_bridge:
            j += 1
        if j < len(g.board.list_bridge):
            g.board.user_list_bridge.append(g.board.list_bridge[j])
            g.board.list_bridge[j].circle1.add_bridge(
                g.board.list_bridge[j].circle2,
                g.board.list_bridge[j].number)
        else:
            text_display("Without orientation", 25, dark_green, (710, 240))

def btn_clear_clicked(g: Game):
    clear_bridges(g.board.user_list_bridge)
    g.board.user_list_bridge.clear()


def how_to_play():
    pass

# ----------------- UI METHODS ------------------------

def ui_lvl1_explain(g):
    pygame.display.update()
    clock.tick(15)
    while True:
        check_iter()
        # We might get one text_display per line of info
        text_display("Let\'s encode our qubits! bla bla bla ...", 30, dark_green, (position[0], position[1] - 20))

        btn(Button(350, 250, 150, 50, green, "|Let's play!>", 30), ui_gameloop, g)

        pygame.display.update()
        clock.tick(15)

def ui_lvl2_explain(g):
    pygame.display.update()
    clock.tick(15)
    while True:
        check_iter()
        # We might get one text_display per line of info
        text_display("Now let's add reality. Let's add error on the grid", 30, dark_green, (position[0], position[1] - 20))

        btn(Button(350, 250, 150, 50, green, "|Got it>", 30), ui_gameloop, g)

        pygame.display.update()
        clock.tick(15)


def ui_play_again():
    pygame.display.update()
    clock.tick(15)
    while True:
        check_iter()

        text_display('Winner!', 50, dark_green, (position[0], position[1] - 20))
        text_display('Want to play again?', 50, dark_green, (position[0] + 10, position[1] + 30))
        
        btn(Button(350, 250, 100, 50, green, "|Yes>", 30), ui_choose_level)
        btn(Button(350, 350, 100, 50, green, "No", 30), pygame.quit, is_quit= True)

        pygame.display.update()
        clock.tick(15)


def ui_choose_level():
    pygame.display.update()
    clock.tick(15)
    while True:
        check_iter()

        text_display("Select level", 70, dark_green, position)

        btn(Button(350, 320, 100, 50, green, "Level 1", 30), set_game, "midi")
        btn(Button(350, 390, 100, 50, green, "Level 2", 30), set_game, "hard")

        pygame.display.update()
        clock.tick(15)

def ui_gameloop(g: Game):
    pygame.display.update()
    clock.tick(15)

    clicked_list = list()
    while True:
        clicked_list = gl_check_iter(g, clicked_list)
        
        btn(Button(650, 180, 120, 50, green, "Hint", 25),btn_hint_clicked,g)
        btn(Button(650, 80, 120, 50, green, "Clean", 25),btn_clear_clicked,g)
 
        g.board.generate_board()
        check(clicked_list, g)
        print_bridge(g.board.user_list_bridge)

        if is_finished(g.board.list_circle):
            pygame.display.update()
            pygame.time.delay(800)
            ui_play_again()

        pygame.display.update()

def menu():
    while True:
        check_iter()
        
        text_display("Quantum Hashi", 60, dark_green, position)
        btn(Button(325, 250, 150, 50, green, "|Play>", 30), ui_choose_level)
        btn(Button(325, 320, 150, 50, green, "How to play", 30), how_to_play)
        btn(Button(325, 390, 150, 50, green, "Exit", 30), pygame.quit, is_quit=True)

        pygame.display.update()
        clock.tick(15)

menu()