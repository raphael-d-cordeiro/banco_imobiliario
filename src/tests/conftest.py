import pytest

from board.factory import create_player, create_board


@pytest.fixture
def board():
    return create_board()


@pytest.fixture
def player_impulsive():
    return create_player('impulsive')


@pytest.fixture
def player_demanding():
    return create_player('demanding')


@pytest.fixture
def player_cautious():
    return create_player('cautious')


@pytest.fixture
def player_randomer():
    return create_player('randomer')
