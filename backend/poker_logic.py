import random

class PokerLogic:
    RANKS = '23456789TJQKA'
    SUITS = 'shdc'

    RANGES = {
        'UTG': {'pairs': 7, 'suited': ['AQ', 'AK'], 'offsuit': ['AK']},
        'MP':  {'pairs': 7, 'suited': ['AQ', 'AK'], 'offsuit': ['AK']},
        'HJ':  {'pairs': 5, 'suited': ['AT', 'KJ', 'QJ'], 'offsuit': ['AJ', 'KQ']},
        'CO':  {'pairs': 5, 'suited': ['AT', 'KJ', 'QJ'], 'offsuit': ['AJ', 'KQ']},
        'BTN': {'pairs': 2, 'suited': ['A2', 'KT', 'QT', 'JT'], 'offsuit': ['AT', 'KT']}
    }

    @staticmethod
    def generate_random_hand():
        deck = [f"{r}{s}" for r in PokerLogic.RANKS for s in PokerLogic.SUITS]
        return random.sample(deck, 2)

    @staticmethod
    def is_in_range(hand: list, position: str, strategy: str) -> str:
        if strategy != 'TAAG': return "GTO_FALLBACK"

        r1, r2 = sorted([hand[0][0], hand[1][0]], key=lambda x: PokerLogic.RANKS.index(x), reverse=True)
        is_suited = hand[0][1] == hand[1][1]
        pos_range = PokerLogic.RANGES.get(position, PokerLogic.RANGES['UTG'])

        if r1 == r2:
            val = PokerLogic.RANKS.index(r1)
            return "RAISE" if val >= (pos_range['pairs'] - 2 if r1.isdigit() else 10) else "FOLD"

        hand_str = f"{r1}{r2}"
        target_list = pos_range['suited'] if is_suited else pos_range['offsuit']

        for r in target_list:
            if PokerLogic.RANKS.index(r1) >= PokerLogic.RANKS.index(r[0]) and \
                PokerLogic.RANKS.index(r2) >= PokerLogic.RANKS.index(r[1]):
                    return "RAISE"

        return "FOLD"
