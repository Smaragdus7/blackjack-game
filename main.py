import random
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(deck):
  """returns a random card in the deck"""
  random_index = random.randint(0,len(deck)-1)
  return deck[random_index]
  
def calculate_score(deck):
  score = sum(deck)
  if 11 in deck:
    if len(deck) == 2 and score == 21:
      return 0
    elif score > 21:
      deck.remove(11)
      deck.append(1)
      score = sum(deck)
      return score
    else:
      return score
  else:
    return score

def compare(u_score,c_score):
  if u_score == c_score:
    print("Its a draw")
  elif c_score == 0:
    print("You lose")
  elif u_score == 0:
    print("You win")
  elif u_score > 21:
    print("You lose")
  elif c_score > 21:
    print("You win")
  else:
    if u_score > c_score:
      print("You win")
    else:
      print("Computer wins")

def play_game():

  print(logo)
  user_cards = []
  computer_cards = []
  num_cards = 0
  
  while num_cards < 2:
    user_cards.append(deal_card(cards))
    computer_cards.append(deal_card(cards))
    num_cards += 1
  print(f"Your cards: {user_cards}")
  print(f"Computer's frist card: {computer_cards[0]}")
  
  print(f"This is your current score: {calculate_score(user_cards)}")

  end_game = False
  while end_game == False:
    if calculate_score(user_cards) > 21 or calculate_score(user_cards) == 0 or calculate_score(computer_cards) == 0:
      end_game = True
      print("Game Over")
    else:
      draw_card = input("Do you want to draw another card? Type 'y' or 'n': ")
    
      if draw_card == "y":
        user_cards.append(deal_card(cards))
        print(user_cards)
        print(f"Your new score is {calculate_score(user_cards)}")
  
        if calculate_score(computer_cards) < 17:
          computer_cards.append(deal_card(cards))
      else:
        end_game = True
        print("Game Over")

  us_score = calculate_score(user_cards)
  co_score = calculate_score(computer_cards)
  print(f"   Your final hand: {user_cards}, final score: {us_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {co_score}")
  print(compare(us_score, co_score))
      
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()