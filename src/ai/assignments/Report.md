# 1: 

Because in the "problem formulation" phase, the agent devises a description of the states and actions necessary to reach the goal. Besides, everything related to the goal is defined in "goal formulation". 

# 2: 
## 2.1. Phân tích bài toán máy hút bụi: 
- Có n ô. Vậy, có n vị trí máy hút bụi (1).
- Mỗi (1) có 2^n trạng thái bẩn. 
Vậy, kích thước không gian trạng thái: n*2^n.

## 2.2.
### 1.
STATES: 
- A state says which glass boxes are unlocked.
- The unlocked glass boxes must be a sequence starting from the first glass.
- Number of combination: 7.

INITIAL STATE: 
- All glass boxes are locked.

ACTIONS: 
- A glass box is unlocked.

TRANSITION MODEL: 
- Maps a state having n locked glass boxes and an action unlocking one resulting in a state having n-1 locked glass boxes. 

GOAL STATES: 
- All boxes is unlocked. 

ACTION COST: Each action costs 1. 

### 2.
STATES: 
- Any sequence of A,B,C, and E (Infinite state space). 

INITIAL STATE: Any state. 

ACTIONS: 
- Transform a part of the sequence using the following equalities: 
AC = E, AB = BC, BB = E, and Ex = x for any x.

TRANSITION MODEL: 
- Maps a sequence and an equality to resulting a new sequence. 

GOAL STATES: 
- E

ACTION COST: 
- 1.

### 3.
STATES: 
- Position of the agent. 
- Which squares are unpainted & painted. 
- Which squares are bottomless pit. 

INITIAL STATE: 
- Any state in which the agent is on an unpainted square.

ACTIONS: 
- Paint. 
- Move onto an adjacent unpainted square.

TRANSITION MODEL: 
- Paint turn an unpainted square to a painted one. 
- Move change position of the agent. 
- Agent can't move outside the grid.

GOAL STATES: 
- All squares are painted. 

ACTION COST: 
- 1

### 4.
STATES: 
- Position of remaining containers on the ship. 
- For each columns, must unload containers top down.

INITIAL STATE: 
- 13x13x5 containers.

ACTIONS: 
- Unload a specific container. 
- For each columns, must unload containers top down.

TRANSITION MODEL: 
- Map a remaining containers and an unloading to resulting a new remaining containers. 

GOAL STATES: 
- The ship unloaded. 

ACTION COST: 
- 1.

# 3.
## 1. 
### a. 
STATES: 
For a specific size of the maze: 
- Position and facing of the agent. 
- Position of walls. 

INITIAL STATE: 
- Any. 

ACTIONS: 
- Turn. 
- Move forward a certain distance. 
- Can move through a wall. 

TRANSITION MODEL: 
- Map a combination of positions of the agent & walls and one of the actions to resulting a new state. 

GOAL STATES: 
- The agent out of a maze. 

ACTION COST: 
- 1.

### b.
Size of state space: nxm maze, w walls, 1 agent.
(nxm C w) * (nxm - w).

## 2. 
### a. 
STATES: 
For a specific size of the maze: 
- Position and orientation of the agent. 
- Position of corridor intersection.

INITIAL STATE: 
- Any. 

ACTIONS: 
- Turn. 
- Move forward to a corridor intersection. 

TRANSITION MODEL: 
- Map a combination of positions of the agent & corridor intersection and one of the actions to resulting a new state. 

GOAL STATES: 
- The agent out of a maze. 

ACTION COST: 
- 1.

### b.
Assume all corridor intersections are crossroads (4 directions), nxm maze, c corridor intersections, w walls, 1 agent.
(nxm C c) * (nxm - w). 

## 3. 
### a. 
STATES: 
For a specific size of the maze: 
- Position of the agent. 
- Position of turning points. 

INITIAL STATE: 
- Any. 

ACTIONS: 
- Move on one of the 4 directions until reach a turning point. 

TRANSITION MODEL: 
- Map a combination of positions of the agent & turning points and moving to resulting a new combination. 

GOAL STATES: 
- The agent out of a maze. 

ACTION COST: 
- 1.

### b. 
Don't need to track agent's orientation. 

## 4. 
- Robot is out of energy. 
- Robot is stuck. 
- Robot is destroyed by some villain.

# 4.
## 1. 
### a. 
STATES: 
- Any combination of red and blue of the grid.

INITIAL STATE: 
- All blue

ACTIONS: 
- Change color of a square. 

TRANSITION MODEL: 
- Map a combination and a color change to resulting a new combination.

GOAL STATES: 
- Each sub-square to be all one color but neighboring sub-squares to be different colors.

ACTION COST: 
- 1.

### b. 
- 2^81.

## 2. 
### a. 
STATES: 
- Any combination of red and blue of the grid.

INITIAL STATE: 
- All blue

ACTIONS: 
- Change color of a square. 
- Color each square only once

TRANSITION MODEL: 
- Map a combination and a color change to resulting a new combination.

GOAL STATES: 
- Each sub-square to be all one color but neighboring sub-squares to be different colors.

ACTION COST: 
- 1.

### b. 
- 2^81.

### c. 
(?)

### d. 
(?)

## 3. 
### a. 
STATES: 
- Any combination of red and blue of the grid.

INITIAL STATE: 
- Any. 

ACTIONS: 
- Color all squares on uniformly colored sub-squares

TRANSITION MODEL: 
- Map a combination and a color change to resulting a new combination.

GOAL STATES: 
- All sub-squares are uniformly colored. 

ACTION COST: 
- 1.

### b. 
2^9 (Each sub-square can be uniformed colored or not). 

## 4. 
- Only 2 goals.
(?)

## 5. 
(?)

# 5.
## 1. 
> Goal formulatio is "Goal state". 

STATES: 
- Position of 2 agents (friends).

INITIAL STATE: 
- 2 agents are in their ogriginal positions. 

ACTIONS: 
- One of 2 agents move in turn to another position.

TRANSITION MODEL: 
- Map a state and an action to resulting a new state. 

GOAL STATES: 
- 2 agents at the same position. 

ACTION COST: 
- 1.

## 2. 
- (i) & (iii) is admissible. But should select (i). 

## 3. 
- No.

## 4. 
- No. Because visit the same node more than once doesn't change anything. Only a "bad" algorithm leads to that behavior. 

# 6. 
- [References](https://cpentalk.com/502/puzzle-states-divided-disjoint-reachable-while-reachable).

## 1. Procedure: 
Compute N (N denote the sum of the total number of inversions and the row number of the empty square) of the given state S. 
if N is even then S belongs to the set which can't reach the goal state. 
else N belongs to the set can reach the goal state. 

## 2.
(?)






























 



