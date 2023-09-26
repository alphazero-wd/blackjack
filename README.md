# Game rules:
Read the game rules on [Wiki](https://en.wikipedia.org/wiki/Blackjack) 
- At the start of each bet, the player can bet between $1 and the amount of money the player has
- The player and dealer are given 2 cards
- The player knows both of their cards but only knows one of the dealer's cards, the other one is hidden.

# Calculate results:
- If the player can either hit (add more cards) or stay (NOT add more cards) 
- If the player's total is greater than 21, then the player busts and loses the hand regardless
- Otherwise, there are two possible cases that might happen:
  - If the dealer's total is less than 17, the dealer must hit until the total is greater than 17 
  - If the total is greater than 21, the dealer busts and the player wins
  - Otherwise, the one whose total is higher is the winner.

# Calculate rewards:
- If the player wins by:
  - **Blackjack** (their total is equal to 21) then they win a reward of **1.5 * bet**.
  - Getting a higher total than the dealer (but not exceeding 21) then they win a reward for what they've bet.
- If the dealer wins then they take the player's bet, thus the player loses money
- If the dealer and the player have the same total then it's a tie, no one loses money.

### The player can have more bets if they still have enough money.
