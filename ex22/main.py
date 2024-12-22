from pathlib import Path
from collections import defaultdict


def mix(number, secret):
    return number ^ secret

def prune(number):
    return number % 16777216

def evolve(secret):
    secret = prune(mix(secret,secret*64))
    secret = prune(mix(secret//32,secret))
    secret = prune(mix(secret,secret*2048))
    return secret

def walk_secrets(secret):
    for _ in range(2000):
        secret = evolve(secret)
        yield secret


sum_secret,cumulative_offers  = 0,defaultdict(int)

for monkey_number, initial_secret in enumerate(list(map(int,Path('input.txt').read_text().splitlines()))):
    sequence, previous_offer, offer, offers_made = [], None, int(str(initial_secret)[-1:]), defaultdict(int)
    for secret_number in walk_secrets(initial_secret):
        previous_offer, offer = offer, int(str(secret_number)[-1:])
        sequence.append(offer-previous_offer)
        if len(sequence) >=4:
            sequence = sequence[-4:]
            a, b, c, d = sequence
            if (a,b,c,d) not in offers_made:
                cumulative_offers[(a,b,c,d)]+=offer + offers_made[(a,b,c,d)]
    sum_secret += secret_number
    
print(sum_secret)
m = max(cumulative_offers.values())
print(m, [k for k,v in cumulative_offers.items() if v == m])