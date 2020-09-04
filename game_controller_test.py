from game_controller import GameController


def test_game_controller():
    # Test the minimal cunstructors argus

    gc = GameController()

    assert len(gc.circles) == 0 and \
        gc.winner == 0 and \
        gc.can_drop and \
        not gc.mouse_drag and \
        not gc.mouse_release and \
        gc.mouse_pressed and \
        gc.txt_update_called and \
        not gc.game_over and \
        not gc.computer_turn and \
        gc.winner_counter == 0

