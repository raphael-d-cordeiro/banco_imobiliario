from .base import BasePlayer


class PlayerImpulsive(BasePlayer):
    '''
    O jogador impulsivo compra qualquer
    propriedade sobre a qual ele parar.
    '''

    def _rules_to_payment(self, patrimony):
        self.paid(patrimony.property_price, patrimony.type_of_strategy)
        return True
