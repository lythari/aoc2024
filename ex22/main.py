from pathlib import Path
from functools import cache
from collections import defaultdict
from datetime import datetime

now = datetime.now
@cache
def mix(number, secret):
    return number ^ secret

@cache
def prune(number):
    return number % 16777216

@cache
def evolve(secret):
    secret = prune(mix(secret,secret*64))
    secret = prune(mix(secret//32,secret))
    secret = prune(mix(secret,secret*2048))
    return secret

def walk_secrets(secret):
    for _ in range(2000):
        secret = evolve(secret)
        yield secret

print(f"Initialisation - {now()}")
sum_secret,cumulative_offers  = 0,defaultdict(int)

for monkey_number, initial_secret in enumerate(list(map(int,Path('input.txt').read_text().splitlines()))):
    sequence, previous_offer, offer, offers_made = [], None, 0, {}
    for secret_number in walk_secrets(initial_secret):
        if previous_offer is None:
            previous_offer, offer = offer, int(str(secret_number)[-1:])
            continue
        previous_offer, offer = offer, int(str(secret_number)[-1:])
        sequence.append(offer-previous_offer)
        if len(sequence) >=4:
            sequence = sequence[-4:]
            a, b, c, d = sequence
            if (a,b,c,d) not in offers_made:
                offers_made[(a,b,c,d)] = 1
                cumulative_offers[(a,b,c,d)]+=offer
    sum_secret += secret_number
print(f"Walked - {now()}")
print(sum_secret)
print(max(cumulative_offers.values()))
print(f"Result - {now()}")