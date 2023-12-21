from itertools import chain

cards = "AKQJT98765432"
def sort_key(item):
    return [cards.index(char) for char in item]

result = 0
with open('23_7/input.txt', 'r') as f:
    lines = f.readlines()
    bids, fiok, fok, fh, tok, tp, op, hc = {}, [], [], [], [], [], [], []
    all_cards = [fiok, fok, fh, tok, tp, op, hc]
    for line in lines:
        line = line.rstrip()

        hand = line.split()[0]
        bids[hand] = int(line.split()[1])
        cnt = {}
        for card in hand:
            cnt[card] = cnt.get(card, 0) + 1

        if 5 in cnt.values():
            # five of a kind
            fiok.append(hand)
        elif 4 in cnt.values():
            # four of a kind
            fok.append(hand)
        elif 3 in cnt.values() and 2 in cnt.values():
            # full house
            fh.append(hand)
        elif 3 in cnt.values() and len(set(cnt.keys())) == 3:
            # three of a kind
            tok.append(hand)
        elif 2 in cnt.values() and len(set(cnt.keys())) == 3:
            # two pair
            tp.append(hand)
        elif 2 in cnt.values() and len(set(cnt.keys())) == 4:
            # one pair
            op.append(hand)
        else:
            hc.append(hand)

    all_cards = [sorted(cards, key = sort_key) for cards in all_cards]
    for i, card in enumerate(reversed(list(chain(*all_cards))), 1):
        result += i * bids[card]
    
    print(result)