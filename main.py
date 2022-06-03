# game rules:
# the player can bet between $1 and the amount of money the player has
# the player and dealer are given 2 cards
# the player knows both cards while the dealer only knows one, the other card is flipped down

# calculate results:
# if the player can either hit (add more cards) or stay (are not allowed to add more cards) 
# if player's total > 21, then the player busts and loses the hand regardless
# else
#     if the dealer's total < 17, the dealer must hit until total >= 17 
#     if total > 21, the dealer busts and the player wins
# check to see whose total is higher and that is the winner 

# calculate rewards:
# if the player wins by:
  # blackjack -> bet * 1.5
  # total higher than the dealer -> bet
# if the dealer wins then takes the player's bet
# if tie then do nothing

# allow restart if the player's money left > 0

from random import random
class Game:
  def __init__(self) -> None:
    self.cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    self.suits = [u"\u2666", u"\u2665", u"\u2663", u"\u2660"]
    self.player_money_left = 500
    self.combinations = []
    self.player_cards = []
    self.dealer_cards = []
    self.bet = 0
    self.winner = None
    self.ith_game = 0

  def convert(self, card, whose_cards):
    if card in [str(i) for i in range(2, 11)]: return int(card)
    elif card in ['J', 'Q', 'K']: return 10
    else:
      sum_without_ace = 0
      for c in whose_cards:
        if c[1] != 'A':
          sum_without_ace += self.convert(c[1], whose_cards)
      
      return 11 if abs(sum_without_ace - 21) >= 11 else 1
  def generate_combinations(self):
    for suit in self.suits:
      for card in self.cards:
        self.combinations.append(suit + str(card))
    self.combinations.sort(key=lambda _: 0.5 - random())

  def reset(self):
    self.player_cards = []
    self.dealer_cards = []
    self.combinations = []
    self.player_total = 0 
    self.dealer_total = 0 

  def start(self):
    while self.player_money_left > 0:
      self.ith_game += 1
      self.select_bet()
    print('You have run out of money :(')

  def select_bet(self):
    choice = input(f'\nGame {self.ith_game}:\nYou are having ${self.player_money_left} in your bank account. Do you want to play? (Type in y for yes, n for no) ')
    if choice == 'y': 
      self.bet = float(input('Place your bet: '))
      while self.bet <= 0: 
        self.bet = float(input('Invalid bet. The minimum bet is $1'))
      while self.bet > self.player_money_left:
        self.bet = float(input('Your bet is greater than the amount of money in your back account. Choose a lower bet: '))
      
      self.reset()
      self.generate_combinations()
      self.play_hand()
    else: exit()

  def play_hand(self):
    self.player_cards = [self.combinations.pop(), self.combinations.pop()]
    self.dealer_cards = [self.combinations.pop(), self.combinations.pop()]
    self.dealer_total = sum([self.convert(card[1], self.dealer_cards) for card in self.dealer_cards]) 
    self.player_total = sum([self.convert(card[1], self.player_cards) for card in self.player_cards])
    print('You have ' + ', '.join(self.player_cards))
    print(f'The dealer has {self.dealer_cards[0]}, Unknown')
    self.handle_player_stay_or_hit()
    self.reward()
    self.display_results()

  def handle_player_stay_or_hit(self):
    while True:
      stay_or_hit = input('Would you like to stay or hit (Type in s for stay or h for hit)? ')
      while stay_or_hit.lower() not in ('s', 'h', 'stay', 'hit'):
        stay_or_hit = input('Invalid choice. Would you like to stay or hit (Type in s for stay or h for hit)? ')
      if stay_or_hit.lower() == 's' or stay_or_hit.lower() == 'stay':
        while True:
          if self.dealer_total >= 17: break
          print('The dealer has ' + ', '.join(self.dealer_cards))
          top = self.combinations.pop()
          print('The dealer gets ' + top)
          self.dealer_cards.append(top)
          self.dealer_total += self.convert(top[1], self.dealer_cards)
        # if the dealer's total > 21 then they lose
        print('The dealer now has ' + ', '.join(self.dealer_cards))
        if self.dealer_total > 21: 
          self.winner = 'player'
        else:
          # otherwise, the one whose total is higher wins 
          if self.player_total > self.dealer_total: 
            self.winner = 'player'
          elif self.player_total < self.dealer_total:
            self.winner = 'dealer'
        break
      elif stay_or_hit.lower() == 'h' or stay_or_hit.lower() == 'hit':
        top = self.combinations.pop()
        self.player_cards.append(top)
        print('You get ' + top)
        print('You now have ' + ', '.join(self.player_cards))
        self.player_total += self.convert(top[1], self.player_cards)
        print(self.player_total)
        if self.player_total > 21:
          self.winner = 'dealer'
          break
  
  def display_results(self):
    if self.winner:
      if self.winner == 'player':
        print(f'The {self.winner} win. ${self.bet} has been transferred into your account :)')
      else:
        print(f'The {self.winner} wins. You lost ${abs(self.bet)} :(')
      self.player_money_left += self.bet
    else:
      print('Tie. You have not lost anything. Keep playing!')
  
  def reward(self):
    if self.winner == 'player' and self.player_total == 21:
      self.bet *= 1.5
    elif self.winner == 'dealer':
      self.bet = -self.bet

Game().start()