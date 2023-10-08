from datetime import datetime
from core.gameElements import Button
from core.game import *
from core.solver import *
from webbrowser import open_new
import datetime
from core.settings import *
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
    game_display.blit(load_file('./Hashi-dotQ/core/img/background2.png'), (0, 0))

# ------------------ GAMELOOP AUX METHODS ------------------------

def gl_check_iter(g: Game, clicked_list: list, counter, timer_event) -> list:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == timer_event:
            counter -= 1
            if counter == 0:
                pygame.time.set_timer(timer_event, 0) 
                ui_play_again(g,loose = True)
        z = g.board.update(event)
        if z is not None:
            clicked_list.append(z)
    game_display.blit(load_file('./Hashi-dotQ/core/img/backgroundBakhao.jpeg'), (0, 0))
    text_display("Time left:", 40, black, (position[0]+275, position[1]+150))
    text_display(str(counter), 100, black, (position[0]+325, position[1]+225))
    return clicked_list, counter


# ------------------ GAMELOOP AUX METHODS ------------------------

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

# Need to open the pdf or whatever is going to be
def how_to_play():
    open_new('Game-Concept-for-Quantum-Hashi.pdf')

def fix_error_clicked(g: Game):
    if g.selected_circle is not None:
        # g.board.list_circle[g.selected_circle].error = 1 - g.board.list_circle[g.selected_circle].error  # Toggle 0 and 1
        g.selected_circle.error = 0
        g.selected_circle = None
    # fix_error_button_active = False  # Deactivate the button

# ----------------- UI METHODS ------------------------

def ui_lvl1_explain(g):
    pygame.display.update()
    clock.tick(15)
    while True:
        check_iter()
        text_display("Level 1: Quantum Hashi Initiation", 40, dark_green, (position[0]+100, position[1]-50))
        text_display("In the mysterious world of Quantum Hashi,", 30, text, (position[0], position[1] + 50))
        text_display("players begin their journey by connecting islands representing qubits.", 30, text, (position[0], position[1]+70))
        text_display("Each bridge symbolizes entanglement, forging quantum connections.", 30, text, (position[0], position[1] + 90))
        text_display("The challenge intensifies as more qubits appear on larger grids,", 30, text, (position[0], position[1] + 110))
        text_display("guiding players toward the secrets of quantum entanglement.", 30, text, (position[0], position[1] +130))

        btn(Button(350, 375, 150, 50, green, "|Let's play!>", 30), ui_gameloop, g)
        pygame.display.update()
        clock.tick(15)

def ui_lvl2_explain(g):
    pygame.display.update()
    clock.tick(15)
    while True:
        check_iter()
        text_display("Level 2: Quantum Parity Puzzles", 40, dark_green, (position[0]+100, position[1]-50))
        text_display("Having mastered quantum entanglement,", 25, text, (position[0], position[1] + 50))
        text_display("players advance to Quantum Parity Puzzles.", 25, text, (position[0], position[1]+70))
        text_display("Bridges, once pathways of entanglement, ", 25, text, (position[0], position[1] + 90))
        text_display("now signify parity measurements.", 25, text, (position[0], position[1] + 110))
        text_display("A flipped bridge means a bit-flip error,", 25, text, (position[0], position[1] +130))
        text_display("and players must decipher the cryptic language of neighboring parity measurements", 25, text, (position[0], position[1] +150))
        text_display("to locate and correct these quantum flaws,", 25, text, (position[0], position[1] +170))
        text_display("all while striving to achieve perfect fidelity.", 25, text, (position[0], position[1] +190))

        btn(Button(350, 400, 150, 50, green, "|Got it>", 30), ui_gameloop, g)
        pygame.display.update()
        clock.tick(15)

def ui_play_again(g,loose = False):
    pygame.display.update()
    clock.tick(15)
    # Calculate the fidelity score
    total_circles = len(g.board.list_circle)
    total_errors = sum(circle.error for circle in g.board.list_circle)
    fidelity_score = ((total_circles - total_errors) / total_circles) * 100

    while True:
        check_iter()

         # Display the appropriate message based on the game result
        if loose:
            text_display("You lose :(", 50, dark_green, (position[0], position[1] - 20))
        else:
            text_display("Winner!", 50, dark_green, (position[0], position[1] - 20))
            # Display the fidelity score
            if g.level==2: text_display(f"Fidelity Score: {fidelity_score:.2f}%", 40, dark_green, (position[0] + 10, position[1] + 20))

        text_display('Want to play again?', 50, dark_green, (position[0] + 10, position[1] + 65))
        
        btn(Button(350, 260, 100, 50, green, "|Yes>", 30), ui_choose_level)
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
    fix_error_button_active = False
    if g.level == 2:
        fix_error_button_active = True  # Indicates if the "Fix Error" button is active
    timer_event = pygame.USEREVENT+1
    pygame.time.set_timer(timer_event, 1000)

    clicked_list = list()
    counter = 10 if g.level == 1 else 30
    # To not include error in 1st level
    for circle in g.board.list_circle:
        if circle.error == 1 and g.level == 1:
            circle.error = 1 - circle.error  # Toggle 0 and 1

    while True:
        clicked_list, counter = gl_check_iter(g, clicked_list, counter, timer_event)
        g.selected_circle = None  # Store the selected circle for fixing errors
        # Check if a circle with custom_variable = 1 is clicked
        for circle in g.board.list_circle:
            if circle.is_clicked and circle.error == 1:
                g.selected_circle = circle
                break

        if fix_error_button_active:
            # Display the "Fix Error" button
            btn(Button(650, 250, 120, 50, green, "Fix Error", 25), fix_error_clicked, g)#, clicked_list[-1])
        # Check for errors and change circle color accordingly
        # for circle in g.board.list_circle:
        #     if circle.error == 1:
        #         circle.change_color(red)  # Change to the color you want for errors

        btn(Button(650, 180, 120, 50, green, "Hint", 25),btn_hint_clicked,g)
        btn(Button(650, 80, 120, 50, green, "Clean", 25),btn_clear_clicked,g)

        g.board.generate_board()
        check(clicked_list, g)
        print_bridge(g.board.user_list_bridge)

        if is_finished(g.board.list_circle):
            pygame.display.update()
            pygame.time.delay(800)
            ui_play_again(g)

        pygame.display.update()

def menu():
    while True:
        check_iter()
        
        text_display("Ĥasħi", 70, dark_green, position)
        btn(Button(325, 250, 150, 50, green, "|Play>", 30), ui_choose_level)
        
        pygame.display.update()
        clock.tick(15)

menu()