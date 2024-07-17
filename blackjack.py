import random

deck_of_cards = [
    'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'
] * 4

for i in range(len(deck_of_cards) - 1, 1, -1):
  j = random.randint(0, i)
  deck_of_cards[i], deck_of_cards[j] = deck_of_cards[j], deck_of_cards[i]

your_hand = []
dealer_hand = []

your_hand.append(deck_of_cards.pop())
dealer_hand.append(deck_of_cards.pop())
your_hand.append(deck_of_cards.pop())
dealer_hand.append(deck_of_cards.pop())


def calculate_hand_value(hand):
  sum = 0
  for card in hand:
    if card.isdigit():
      sum += int(card)
    else:
      if card in ['K', 'Q', 'J']:
        sum += 10
      else:
        sum += 11
  if sum > 21 and 'A' in hand:
    sum -= 10
  return sum


print("PLAYER TURN")
while True:
  player_total = calculate_hand_value(your_hand)
  if player_total > 21:
    print(f"BUST! Your cards: {your_hand}; Your total: {player_total}")
    break

  print(f"Your cards: {your_hand}; Your total: {player_total}")

  action = input("What do you want to do? (h/s): ")

  if (action == 'h'):
    your_hand.append(deck_of_cards.pop())
  else:
    print(f"You hold at {player_total}")
    break

print("DEALER TURN")
while True:
  dealer_total = calculate_hand_value(dealer_hand)
  print(f"Dealer's Hand: {dealer_hand}; Dealer total: {dealer_total}")
  if dealer_total > 21:
    print("Dealer Bust!")
    break
  if dealer_total < 17:
    dealer_hand.append(deck_of_cards.pop())
  else:
    player_total = calculate_hand_value(your_hand)
    if dealer_total >= player_total:
      print("dealer stands")
      break
    else:
      dealer_hand.append(deck_of_cards.pop())

player_total = calculate_hand_value(your_hand)
dealer_total = calculate_hand_value(dealer_hand)

if (player_total > 21 and (dealer_total >= 17 and dealer_total <= 21)) or (player_total == dealer_total):
  print("Dealer Wins")
elif player_total > 21 and dealer_total > 21:
  print ("Nobody Wins")
elif dealer_total > player_total:
  print("Dealer Wins")
else:
  print("Player Wins")