import numpy
import copy
 
class State:
 def __init__(self, x, y):
   self.x = x
   self.y = y
 
grid = [State(1, 1), State(2, 1), State(3, 1), State(4, 1), State(1, 2), State(2, 2), State(3,2), State(4, 2), State(1, 3), State(2, 3), State(3, 3), State(4, 3)]
 
actions = ['U', 'D', 'L', 'R']
 
rewards = [-0.04, -0.04, -0.04, -0.04, -0.04, 0.0, -0.04, -1, -0.04, -0.04, -0.04, 1]
rewards = numpy.array(rewards)
 
terminalIRP = [[grid[0], rewards[0]], [grid[1], rewards[1]], [grid[2], rewards[2]], [grid[3], rewards[3]], [grid[4], rewards[4]], [grid[5], rewards[5]], [grid[6], rewards[6]], [grid[7], rewards[7]], [grid[8], rewards[8]], [grid[9], rewards[9]]]
 
terminalStates = [grid[10], grid[6]]
 
discount = 1
 
#################################################################################
 
# action - a
# state - s
# S - outcomes, s'
# U - utilities, U(s')
# P - transition model P(s'|s, a)
def getExpectedUtility(action, state, S, U, P):
  # Do nothing. I remember you saying we could just have an empty method
  return NotImplemented
 
#################################################################################
 
def valueIteration(grid, actions, P, rewards, discount, terminalIRP):
  U = numpy.full((len(grid), 1), 0.0)
 
  iTerminals = [i[0] for i in terminalIRP]
 
  for t in terminalIRP:
    U[t[0]] = t[1]
 
  uPrime = copy.deepcopy(U[0])
 
  while True:
 
    delta = 0
 
    U = copy.deepcopy(uPrime)
 
    # For each state
    for s, in enumerate(grid):
      if (s != grid[5]):
        valueFunction = 0
        actionProbs = P[s]
 
      # For each action
      for a in enumerate(grid):
        if (a != grid[5]):
          [(actionProbs, grid[s+1], rewards[s], done)] = P[s][a]
          # Bellman equation
          valueFunction += actionProbs[a] * (rewards[a] + discount * U[grid[s+1]])
 
      delta = max(delta, abs(valueFunction - U[s]))
      uPrime[s] = valueFunction
 
    U = uPrime
 
    if(delta < discount):
      break
  return U
 
##########################################################################
 
def getIndexOfState(S, x, y):
  """ Get the index of the state that contains the (x,y) position in S
  
  Parameters:
      S (list): list of State objects
      x (integer): x coordinate of a cell
      y (integer): y coordinate of a cell
      
  Returns:
      int: in range [0,len(S)-1] if the position can be found. -1 otherwise
  """
  for i,s in enumerate(S):
      if s.x == x and s.y == y:
          return i
  return -1
 
######################################################################
 
def getPolicyForGrid(grid, U, actions, P, terminalStates):
  """ Computes the policy as a list of characters indicating which direction to move in at the state
  
  Parameters:
      S (list): States
      U (numpy array): Utilities
      A (list): Actions
      P (numpy array): Transition model matrix
      i_terminal_states (list): Indices of the terminal states
      
  Returns:
      list: 1d list of characters that indicate the action to take at each state
  """
  policy = []
  
  for i_s, s in enumerate(grid):
      i_states = []
      
      # If it's a terminal state, then make the action be 'T'
      if i_s in terminalStates:
          action = 'T'
          
      # Otherwise, find the action that gives the best utility
      else:
          i_states = []
          
          # Get the index of each neighbor for a state
          i_up = getIndexOfState(grid, s.x, s.y+1)
          i_right = getIndexOfState(grid, s.x+1, s.y)
          i_down = getIndexOfState(grid, s.x, s.y-1)
          i_left = getIndexOfState(grid, s.x-1, s.y)                      
          
          # Check to make sure each one is not an obstacle           
          if i_up != -1:
              i_states.append(i_up)
                  
          if i_right != -1:
              i_states.append(i_right)
              
          if i_down != -1:
              i_states.append(i_down)               
              
          if i_left != -1:
              i_states.append(i_left)
                
          # Append the state itself to consider the agent bouncing off the boundary
          i_states.append(i_s)
          
          # Calculate the expected utilities for each action in the state
          i_a_max_eu = 0
          max_eu = -100000 # don't wait to loop for i_a=0...
          for i_a, a in enumerate(actions):
      
              # Get the expected utility for an action
              eu = 0               
              for i_neighbor in i_states:
                  u_s_prime = U[i_neighbor]
                  prob_s_prime = P[i_a, i_s, i_neighbor]
                  eu += (prob_s_prime * u_s_prime)
 
              # Check if max expected utility
              if eu > max_eu:
                  max_eu = eu
                  i_a_max_eu = i_a
          
          # Set the action character
          action = actions[i_a_max_eu]
          
      # Add the action to the policy
      policy.append(action)             
  
  return policy
  
######################################################################
 
def printPolicyForGrid(policy, w, h, i_obs):
  """ Print out a policy in the form:
      ['r', 'r', 'r', 'T']
      ['u', '0', 'u', 'T']
      ['u', 'l', 'l', 'l']
      where the characters indicate the action to take at each state.
      '0' elements are obstacles in the grid.
      
  Parameters:
      policy (list): 1d list of characters indicating which action to take for each state
      w (int): width of the grid
      h (int): height of the grid
      i_obs(list): list of indices where obstacles are located
      
  Returns:
      None
  """
  
  # Insert 0's for obstacle tiles
  for i_ob in i_obs:
      policy.insert(i_ob, '0')  
 
  # Blank line to isolate the policy
  print('\n')
  
  # Start at top of the grid, and print each row
  for y in range(h-1,-1,-1):
      row = [policy[ ((w*y)+i) ] for i in range(0,w)]
      print(row)
      
      
      
# P is the transition model matrix for the 4x3 grid world problem
# P gets converted to a numpy array after it is hard-coded here
# actions are in order: up, right, down, left
# rows -> s
# cols -> s'
# [action, state, outcome], [a, s, s']
P = [[[0.1, 0.1, 0.,  0.,  0.8, 0.,  0.,  0.,  0.,  0.,  0.],
    [0.1, 0.8, 0.1, 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0. ],
    [0.,  0.1, 0.,  0.1, 0.,  0.8, 0.,  0.,  0.,  0.,  0. ],
    [0.,  0.,  0.1, 0.1, 0.,  0.,  0.8, 0.,  0.,  0.,  0. ],
    [0.,  0.,  0.,  0.,  0.2, 0.,  0.,  0.8, 0.,  0.,  0. ],
    [0.,  0.,  0.,  0.,  0.,  0.1, 0.1, 0.,  0.,  0.8, 0. ],
    [0.,  0.,  0.,  0.,  0.,  0.1, 0.1, 0.,  0.,  0.,  0.8],
    [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.9, 0.1, 0.,  0. ],
    [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.1, 0.8, 0.1, 0. ],
    [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.1, 0.8, 0.1],
    [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.1, 0.9]],
 
[[0.1, 0.8, 0.,  0.,  0.1, 0.,  0.,  0.,  0.,  0.,  0. ],
[0.,  0.2, 0.8, 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0. ],
[0.,  0.,  0.1, 0.8, 0.,  0.1, 0.,  0.,  0.,  0.,  0. ],
[0.,  0.,  0.,  0.9, 0.,  0.,  0.1, 0.,  0.,  0.,  0. ],
[0.1, 0.,  0.,  0.,  0.8, 0.,  0.,  0.1, 0.,  0.,  0. ],
[0.,  0.,  0.1, 0.,  0.,  0.,  0.8, 0.,  0.,  0.1, 0. ],
[0.,  0.,  0.,  0.1, 0.,  0.,  0.8, 0.,  0.,  0.,  0.1],
[0.,  0.,  0.,  0.,  0.1, 0.,  0.,  0.1, 0.8, 0.,  0. ],
[0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.2, 0.8, 0. ],
[0.,  0.,  0.,  0.,  0.,  0.1, 0.,  0.,  0.,  0.1, 0.8],
[0.,  0.,  0.,  0.,  0.,  0.,  0.1, 0.,  0.,  0.,  0.9]],
 
[[0.9, 0.1, 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0. ],
[0.1, 0.8, 0.1, 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0. ],
[0.,  0.1, 0.8, 0.1, 0.,  0.,  0.,  0.,  0.,  0.,  0. ],
[0.,  0.,  0.1, 0.9, 0.,  0.,  0.,  0.,  0.,  0.,  0. ],
[0.8, 0.,  0.,  0.,  0.2, 0.,  0.,  0.,  0.,  0.,  0. ],
[0.,  0.,  0.8, 0.,  0.,  0.1, 0.1, 0.,  0.,  0.,  0. ],
[0.,  0.,  0.,  0.8, 0.,  0.1, 0.1, 0.,  0.,  0.,  0. ],
[0.,  0.,  0.,  0.,  0.8, 0.,  0.,  0.1, 0.1, 0.,  0. ],
[0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.1, 0.8, 0.1, 0. ],
[0.,  0.,  0.,  0.,  0.,  0.8, 0.,  0.,  0.1, 0.,  0.1],
[0.,  0.,  0.,  0.,  0.,  0.,  0.8, 0.,  0.,  0.1, 0.1]],
 
[[0.9, 0.,  0.,  0.,  0.1, 0.,  0.,  0.,  0.,  0.,  0. ],
[0.8, 0.2, 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0. ],
[0.,  0.8, 0.1, 0.,  0.,  0.1, 0.,  0.,  0.,  0.,  0. ],
[0.,  0.,  0.8, 0.1, 0.,  0.,  0.1, 0.,  0.,  0.,  0. ],
[0.1, 0.,  0.,  0.,  0.8, 0.,  0.,  0.1, 0.,  0.,  0. ],
[0.,  0.,  0.1, 0.,  0.,  0.8, 0.,  0.,  0.,  0.1, 0. ],
[0.,  0.,  0.,  0.1, 0.,  0.8, 0.,  0.,  0.,  0.,  0.1],
[0.,  0.,  0.,  0.,  0.1, 0.,  0.,  0.9, 0.,  0.,  0. ],
[0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.8, 0.2, 0.,  0. ],
[0.,  0.,  0.,  0.,  0.,  0.1, 0.,  0.,  0.8, 0.1, 0. ],
[0.,  0.,  0.,  0.,  0.,  0.,  0.1, 0.,  0.,  0.8, 0.1]]]
P = numpy.array(P)
 
################################################################
terminalStates=[6,10]

optimalUtilityValues = valueIteration(grid, actions, P, rewards, discount, terminalIRP)
policy = getPolicyForGrid(grid, optimalUtilityValues,P, actions,[6,10])
w=4
h =3

printPolicyForGrid(policy, w, h, grid[5])

