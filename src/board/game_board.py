import os
from datetime import datetime
from random import randint

from dotenv import load_dotenv

from .card_patrimony import Patrimony

load_dotenv()


class GameBoard:

    def __init__(self, *args, **kwargs):
        self.winner = None
        self.played = 0
        self.players = []
        self.start_time = datetime.now()
        self.cards = [
            Patrimony(index, None)
            for index in range(
                int(os.getenv('ENV_QUANTITY_OF_PROPERTIES'))
            )
        ]

    @staticmethod
    def play_dice():
        '''
        No começo da sua vez, o jogador joga um
        dado equiprovável de 6 faces que determina
        quantas espaços no tabuleiro o jogador vai
        andar.
        '''
        return randint(1, 6)

    def __getitem__(self, position):
        return self.cards[position]

    def __setitem__(self, position, patrimony):
        self.cards[position] = patrimony

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return f"{self.cards}"

    def __repr__(self):
        return f"{self.cards}"

    def remove(self, player):
        for patrimony in self.cards:
            if patrimony.type_of_strategy == player:
                patrimony.type_of_strategy = None
        self.players.remove(player)

    def walk(self, player, _dice=None):
        go_to_position = player.position + (_dice or self.play_dice())
        if go_to_position >= int(os.getenv('ENV_QUANTITY_OF_PROPERTIES')):
            '''
            Ao completar uma volta no tabuleiro,
            o jogador ganha 100 de saldo.
            '''
            player.money += float(os.getenv('ENV_PLAYER_MONEY_ROUND'))
            go_to_position -= int(os.getenv('ENV_QUANTITY_OF_PROPERTIES'))
        player.position = go_to_position
        return go_to_position

    def check_winner(self, player):
        '''
        Termina quando restar somente um jogador
        com saldo positivo, a qualquer momento da
        partida. Esse jogador é declarado o
        vencedor.
        '''
        if len(self.players) == 1:
            return player
        if int(os.getenv('ENV_TIMEOUT_ROUND')) <= self.played:
            money = 0
            winner = None
            for _player in self.players:
                if _player.money > money:
                    money = _player.money
                    winner = _player
            return winner

        elements = [
            _player.money
            for _player in self.players if _player != player
        ]
        if sum(elements) < 0:
            return player

        return None

    def play(self, player, board):
        '''
        Um jogador que fica com saldo negativo
        perde o jogo, e não joga mais. Perde
        suas propriedades e portanto podem ser
        compradas por qualquer outro jogador.
        '''
        if player.money <= 0:
            player.gameover = True
            return

        patrimony = self.cards[self.walk(player)]
        player.income_or_sale(patrimony, board)

    def finish(self):
        return {
            "time_it": (datetime.now() - self.start_time).total_seconds(),
            "winner": self.winner,
            "money": self.winner.money,
            "played": self.played,
            "strategy": self.winner,
            "time_out": self.played > int(os.getenv('ENV_TIMEOUT_ROUND')),
        }
