# SEARCH

- Solving a problem of how to go from POINT A to POINT B

## TERMINOLOGIES

### AGENT

- Entity that PERCEIVES ITS ENVIRONMENT AND ACTS UPON THAT ENVIRONMENT

### STATE

- Configuration ofthe agent and its environment

#### INITIAL STATE

- State in which the agent begins

### ACTIONS

- Choices that can be made in a state
- ACTIONS(s) returns the set of actions that can be executed in state `s`

### TRANSITION MODEL

- a description of what state results from transforming any applicable action in any state

#### RESULT (s,a)

- returns the state RESULTING from performing action `a` in state `s`

### STATE SPACE

- the state of all states reachable from the initial state by any sequence of actions

### GOAL TEST

- way to determine whether a given state is a/the GOAL STATE

### PATH COST

- numerical cost associated with a given path

### OPTIMAL SOLUTION

- a solution that has the lowest path cost among all solutions.

### NODE

- a data structure that keeps track of
  - a state
  - a parent (node that generated this current node)
  - an action (action applied to parent to get node)
  - a path cost from initial state to current state

### FRONTIER

- represents all of the things that we could explore next that we HAVEN'T explored or visited yet

## CLASSIC APPROACH

1. Start with a frontier that contains the initial state
2. Repeat:
   1. If the frontier is empty, then there's no solution
   2. Otherwise, remove a node from the frontier
   3. If the node contains the goal state, return the solution, else,
   4. EXPAND the node, add resulting nodes to the frontier

## REVISED APPROACH WITH EXPLORED SETS

1. Start with a frontier that contains the initial state
2. Start with empty explored set.
3. Repeat:
   1. If the frontier is empty, then there's no solution
   2. Otherwise, remove a node from the frontier
   3. If the node contains the goal state, return the solution, else,
   4. Add the node to explored set.
   5. EXPAND the node, add resulting nodes to the frontier if not yet in frontier or explored sets
