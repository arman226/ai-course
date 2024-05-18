# LINEAR SEARCH

- Type of Search where there is only one AGENT observing/conducting the search.
- No other agent is opposing the search

## UNINFORMED SEARCH

- Search Strategy that uses NO problem-specific knowledge

### DEPTH-FIRST SEARCH

- Search Algorithm that always expands the <b>deepest</b> node in the frontier

### BREADTH-FIRST SEARCH

- Always expands the <b>shallowest</b> node in the frontier

## INFORMED SEARCH

- Search Strategy that uses problem-specific knowledge to find solutions more efficiently.

### GREEDY BEST-FIRST SEARCH

- search algorithm that expands the node that is closest to the goal, as estimated by HEURISTIC function - `h(n)`
- MANHATTAN DISTANCE

### A\* SEARCH

- expands with lowest value of `g(n) + h(n)`
  - `g(n)` is the cost to reach current node
  - `h(n)` is the estimated cost to reach the goal
- it is optimal if:
  - `h(n)` is admissible (never overestimate the true cost)
  - `h(n)` is consistent (for every node `n` and successor `n` with step cost `c`, `h(n)<=h(n)+c`)
