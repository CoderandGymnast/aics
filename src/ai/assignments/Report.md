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

INITIAL STAE: 
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






 



