# ADVERSARIAL SEARCH

- Search with at least two opposing AGENTS such as Tic-Tac-Toe game

## MINI MAX

- Max (X) aims to <b>maximize</b> the score
- Min (O) aims to <b>minimize </b> the score

### GAME

- S<sub>0</sub> - initial State
- `PLAYER(s)` returns which player to move in state `s`
- `ACTION(s)` returns LEGAL moves in state `s`
- `RESULT(s,a)` returns state after action `a` taken in state `s`
- `TERMINAL(s)` - checks if state `s` is a terminal state <b>GOAL STATE</b>
- `UTILITY(s)` - final numerical value for terminal state `s`

### ALGORITHM

- Given a state `s`:

  - <b>MAX</b> picks action `a` in `ACTION(s)` that produces HIGHEST value of `MIN-VALUE(RESULT(s,a))`
  - <b>MIN</b> picks action `a` in `ACTION(s)` that produces HIGHEST value of `MIN-VALUE(RESULT(s,a))`

- Pseudocode for MAX

  ```py pseudocode
  def MAXVALUE(state)
    if TERMINAL(state):
        return UTILITY(state)
    v = -∞
    for action in ACTIONS(state):
        v=MAX(v,MINVALUE(state,action))
  ```

- Pseudocode for MIN

  ```py pseudocode
  def MINVALUE(state)
    if TERMINAL(state):
        return UTILITY(state)
    v = ∞
    for action in ACTIONS(state):
        v=MIN(v,MAXVALUE(state,action))
  ```

## OTHER TERMINOLOGIES

### ALPHA-BETA PRUNING

- it is an optimization technique that reduces the number of nodes evaluated by the `minimax` algorithm by PRUNING branches in the game tree that CANNOT influence the final decision

### DEPTH-LIMITED MINIMAX

### EVALUATION FUNCTION

- function that ESTIMATES the expected `UTILITY` of the game from a given state
