# Let's play! You have to return which player won! In case of a draw return Draw!.

# Examples(Input1, Input2 --> Output):

# "scissors", "paper" --> "Player 1 won!"
# "scissors", "rock" --> "Player 2 won!"
# "paper", "paper" --> "Draw!"

# rock beats scissors, scissors beats paper, paper beats rock


# my solution: 

def rps(p1, p2):
    
    winning_pairs = {'rock':'scissors', 'scissors':'paper', 'paper':'rock'}
    
    if p1 == p2:
        return "Draw!"
    elif p2 == winning_pairs[p1]:
        return "Player 1 won!"
    else:
        return "Player 2 won!"
    

# very clever solution found on the solutions page: 
    
def rps(p1, p2):
    hand = {'rock':0, 'paper':1, 'scissors':2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]    