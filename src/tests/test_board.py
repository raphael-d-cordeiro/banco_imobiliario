from os import getenv
from typing import Counter

from dotenv import load_dotenv

load_dotenv()


def test_quantity_of_properties_board(board):
    assert len(board) == int(getenv('ENV_QUANTITY_OF_PROPERTIES'))


def test_board_quantity_of_players(board):
    assert sum(Counter(board.players).values()) == 4


def test_board_play_dice(board):
    assert board.play_dice() in list(range(1, 7))
    assert type(board.play_dice()) == int


def test_board_walk(board, player_cautious):
    player_cautious.position = 19
    assert board.walk(player_cautious, 1) == 0


def test_board_check_winner(board, player_cautious):
    for player in board.players:
        if player_cautious != player:
            player.money = -1
    _player = board.check_winner(player_cautious)
    board.winner = _player
    assert board.winner == player_cautious
