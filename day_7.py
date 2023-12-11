from collections import Counter
'''
    hand including the wildcard joker, need to first check to see if we can add a joker to 
    the current hand to increase the strength of the hand, if we can add a joker, then we
    also need to update the hand to have the correct value from the joker


    key note got messed up and wasted a couple of hours because I didnt read the following

    To balance this, J cards are now the weakest individual cards, weaker even than 2.
    The other cards stay in the same order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J.

    J cards can pretend to be whatever card is best for the purpose of determining hand type; for example, 
    QJJQ2 is now considered four of a kind. 
    However, for the purpose of breaking ties between two hands of the same type, J is always treated as J,
    not the card it's pretending to be: JKKK2 is weaker than QQQQ2 because J is weaker than Q.

    q1; 247823654
    q2; 245461700
'''

class Hand_j:
    values_q2 = {
            # "2": 2,
            # "3": 3,
            # "4": 4,
            # "5": 5,
            # "6": 6,
            # "7": 7,
            # "8": 8,
            # "9": 9,
            "T": "A",
            "J": "1",
            "Q": "C",
            "K": "D",
            "A": "E",
        }

    def __init__(self, hand, bet):
        self.hand = hand
        self.score = self.max_strength(self.hand)
        self.bet = int(bet)

    def curr_score(self, hand):
        cards_counter = Counter([card for card in hand])
        card_types = list(sorted(cards_counter.values(), reverse=True))

        if card_types == [5]:
            return 6
        elif card_types == [4,1]:
            return 5
        elif card_types == [3,2]:
            return 4
        elif card_types == [3,1,1]:
            return 3
        elif card_types == [2,2,1]:
            return 2
        elif card_types == [2,1,1,1]:
            return 1
        else:
            return 0

    # find all permutations of jokers
    def check_joker(self, hand):
        def backtrack(current_hand, index, result):
            if index == len(current_hand):
                result.append(current_hand)
                return

            if current_hand[index] == "J":
                for card in "23456789TQKA":
                    backtrack(current_hand[:index] + card + current_hand[index + 1:], index + 1, result)
            else:
                backtrack(current_hand, index + 1, result)

        result = []
        backtrack(hand, 0, result)
        return result

    def get_strength(self, hand):
        return max(map(self.curr_score, self.check_joker(hand)))


    def max_strength(self, hand):
        # make it return a tuple of the get_strength and then the array the original array
        return (self.get_strength(hand), [Hand_j.values_q2.get(card, card) for card in hand])

# sort all the hands by rank. then enumerate over all sorted hands and append rank
# create a class for hand object for each hand, containing the hand score, and bet placed

class Hand:
    values_q1 = {
            # "2": 2,
            # "3": 3,
            # "4": 4,
            # "5": 5,
            # "6": 6,
            # "7": 7,
            # "8": 8,
            # "9": 9,
            "T": "A",
            "J": "B",
            "Q": "C",
            "K": "D",
            "A": "E",
        }

    def __init__(self, hand, bet):
        cards_counter = Counter([card for card in hand])
        card_types = list(sorted(cards_counter.values(), reverse=True))
        self.hand = hand
        self.strength = 0 

        if card_types == [5]:
            self.strength = 6
        elif card_types == [4,1]:
            self.strength = 5
        elif card_types == [3,2]:
            self.strength = 4
        elif card_types == [3,1,1]:
            self.strength = 3
        elif card_types == [2,2,1]:
            self.strength = 2
        elif card_types == [2,1,1,1]:
            self.strength = 1
        else:
            self.strength = 0

        self.bet = int(bet)
        # score should be determined based on the strengh + the sorting of the values in the cards
        self.score = (self.strength, [(Hand.values_q1.get(card, card)) for card in hand])


def question_one():
    with open("day7.txt") as f:
        lines = f.read().split('\n')

    hands = []

    for line in lines:
        curr_hand, curr_bet = line.split()
        hands.append(Hand(curr_hand, curr_bet))

    # sort based on score
    hands.sort(key=lambda x: x.score)


    # print(*[(curr_hand.hand, curr_hand.bet, curr_hand.strength, curr_hand.score) for curr_hand in hands], sep='\n')
    res = 0

    for rank, curr_hand in enumerate(hands, 1):
        res += rank * curr_hand.bet

    print(res)


def question_two():
    with open("day7.txt") as f:
        lines = f.read().split('\n')

    hands = []

    for line in lines:
        curr_hand, curr_bet = line.split()
        # find max hand here before you create hands class?
        hands.append(Hand_j(curr_hand, curr_bet))

    # sort based on score
    hands.sort(key=lambda x: x.score)

    res = 0

    for rank, curr_hand in enumerate(hands, 1):
        res += rank * curr_hand.bet

    print(res)

question_one()
question_two()