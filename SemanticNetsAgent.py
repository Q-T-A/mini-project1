class SemanticNetsAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass

    def solve(self, initial_sheep, initial_wolves):
        #Add your code here! Your solve method should receive
        #the initial number of sheep and wolves as integers,
        #and return a list of 2-tuples that represent the moves
        #required to get all sheep and wolves from the left
        #side of the river to the right.
        #
        #If it is impossible to move the animals over according
        #to the rules of the problem, return an empty list of
        #moves.

        start = (initial_sheep, initial_wolves, 0)
        end = (0,0,1)

        queue = [(start, [])]
        visited = set()
        while queue:

            cur, path = queue.pop()
            if cur == end:
                return path
            
            visited.add(cur)
            sheep_left, wolves_left, boat = cur

            moves = [(0,1), (0,2), (1,1), (1,0), (2, 0)]
            for move in moves:
                new_state = generate_state(cur)
                if new_state not in visited:
                    visited.add(new_state)
            
        def generate_state(state):
        pass

