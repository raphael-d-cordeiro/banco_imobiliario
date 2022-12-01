import os
import json
from dotenv import load_dotenv

from .game_board import GameBoard
from players.player_cautious import PlayerCautious
from players.player_demanding import PlayerDemanding
from players.player_impulsive import PlayerImpulsive
from players.player_random import PlayerRandom

load_dotenv()

strategies = {
    "cautious": PlayerCautious,
    "demanding": PlayerDemanding,
    "impulsive": PlayerImpulsive,
    "randomer": PlayerRandom,
}


def create_player(strategy: str, *args, **kwargs):
    try:
        return strategies[strategy](strategy=strategy, *args, **kwargs)

    except KeyError:
        available_strategies = ", ".join(strategies.keys())
        raise NotImplementedError(
            f"The player strategy '{strategy}' is not implemented."
            f"Please use the available strategies: {available_strategies}"
        )


def create_board():
    board = GameBoard()
    env_strategies = json.loads(os.getenv('ENV_STRATEGY'))
    players = [
        create_player(strategy)
        for strategy in env_strategies
    ]
    board.players = players
    return board
