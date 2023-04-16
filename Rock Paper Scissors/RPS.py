import random
#for Quincy if you just use "Paper" it would be enough to win more than 60%
#make a whole new for every opponent
#not sure what it has to do with machine learning this proyect
def player(prev_play, opponent_history=[],my_history=[]):
  opponent_history.append(prev_play)
  ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
  ideal_response_to_response = {'P': 'R', 'R': 'S', 'S': 'P'}
  guess = 'P'
  #Abbey
  if len(opponent_history) < 1000 and len(opponent_history) > 2:
    guess = ideal_response_to_response[my_history[-2]]
  #Kris
  if len(opponent_history) < 2000 and len(opponent_history) > 1000:
    guess = ideal_response_to_response[my_history[-1]]
  #Mrugesh
  if len(opponent_history) < 3000 and len(opponent_history) > 2000:
    guess = ideal_response_to_response[my_history[-2]]
  #Quincy
  if len(opponent_history) > 3000:
    guess = 'P'
  my_history.append(guess)
  return guess