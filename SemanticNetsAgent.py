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
        count = 0
        start = (initial_sheep, initial_wolves, 0)
        end = (0,0,1)

        queue = [(start, [])]
        visited = set()
        ans = []
        #bfs
        while queue:
            cur, path = queue.pop(0)
            #print(f'current path: {path}')
            if cur == end:
                return path
            
            visited.add(cur)
            sheep_left, wolves_left, boat = cur

            moves = [(0,1), (0,2), (1,1), (1,0), (2, 0)]
            for move in moves:
                new_state = self.generate_state(sheep_left, wolves_left, boat, move)
                if new_state not in visited and self.isValid(new_state, initial_sheep, initial_wolves):
                    #print(f'New state: {new_state}')
                    visited.add(new_state)
                    queue.append((new_state, path + [move]))
        return []

    def generate_state(self, sheep, wolf, boat, move):
            sheep_moving, wolves_moving = move
            if boat == 0:
                sheep -= sheep_moving 
                wolf -= wolves_moving
                boat = 1
                return (sheep, wolf, boat)
            else: 
                sheep += sheep_moving
                wolf += wolves_moving
                boat = 0
                return (sheep, wolf, boat)


            #return a state 

    def isValid(self, state, initial_sheep,initial_wolves):
            #return type boolean 
            sheep_left, wolf_left, boat = state
            sheep_right, wolf_right = initial_sheep - sheep_left, initial_wolves - wolf_left
            #print(f'sheep_left: {sheep_left}, boat:{boat}, shee_right: {sheep_right}, \nwolf_left: {wolf_left},           wolf_right: {wolf_right}')
            if sheep_left > initial_sheep or wolf_left > initial_wolves or sheep_left < 0 or wolf_left < 0:
                #print('Invalid')
                return False
            elif sheep_left > 0 and sheep_left < wolf_left  or sheep_right  > 0 and sheep_right < wolf_right:
                #print('Invalid')
                return False
            return True