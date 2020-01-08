class Room:
    def __init__(self, id, name, description, x, y):
        self.id = id
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.x = x
        self.y = y
    def __repr__(self):
        if self.e_to is not None:
            return f"({self.x}, {self.y}) -> ({self.e_to.x}, {self.e_to.y})"
        return f"({self.x}, {self.y})"
    def connect_rooms(self, connecting_room, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''
        reverse_dirs = {"n": "s", "s": "n", "e": "w", "w": "e"}
        reverse_dir = reverse_dirs[direction]
        setattr(self, f"{direction}_to", connecting_room)
        setattr(connecting_room, f"{reverse_dir}_to", self)
    def get_room_in_direction(self, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''
        return getattr(self, f"{direction}_to")

class World:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0

    def generate_rooms(self, size_x, size_y, num_rooms):
        """
        Fill up the grid in a spiral pattern
        """

        # 2-D List
        # Initialize the grid
        self.grid = [None] * size_y
        self.width = size_x
        self.height = size_y
        for i in range( len(self.grid) ):
            self.grid[i] = [None] * size_x

        start_x = (size_x) // 2
        start_y = (size_x) // 2

        position = (start_x, start_y)
        room_num = 0

        # initialize with one step 
        steps = 1
        # 1=N, 2=W, 3=S, 4=E
        traveling = 'n'

        # rnd(round) is one continous cycle without increasing steps
        rnd = 1

        # create room at center
        room = Room(room_num, f"Room {room_num}", f"A generic description for room {room_num}", start_x, start_y)
        
        # Save the room in the World grid
        self.grid[start_y][start_x] = room

        # update iterators
        num_rooms -= 1
        room_num += 1
        previous_room = None

        # x = position[0]
        # y = position[1]

        while num_rooms > 0:
            print(num_rooms)
            steps = rnd * 2

            while steps:
                # this could be causing a bug
                x = position[0]
                y = position[1]

                if traveling == 'n':
                    y += 1

                    # if wall, turn left
                    if steps == (rnd / 2):
                        traveling = 'w'

                    # create a room and pass in (x, y)
                    room = Room(room_num, f"Room {room_num}", f"A generic description for room {room_num}", x, y)

                    # Save the room in the World grid
                    self.grid[y][x] = room

                    # connect the new room to the previous room
                    if previous_room is not None:
                        previous_room.connect_rooms(room, traveling)

                    # update iterators
                    num_rooms -= 1
                    room_num += 1
                    previous_room = room

                elif traveling == 's':
                    y -= 1

                    # if wall, turn left
                    if steps == (rnd / 2):
                        # 1: turn W
                        traveling = 'e'

                    # create a room and pass in (x, y)
                    room = Room(room_num, f"Room {room_num}", f"A generic description for room {room_num}", x, y)

                    # Save the room in the World grid
                    self.grid[y][x] = room

                    # connect the new room to the previous room
                    if previous_room is not None:
                        previous_room.connect_rooms(room, traveling)

                    # update iterators
                    num_rooms -= 1
                    room_num += 1
                    previous_room = room

                elif traveling == 'e':
                    x += 1

                    # create a room and pass in (x, y)
                    room = Room(room_num, f"Room {room_num}", f"A generic description for room {room_num}", x, y)

                    # Save the room in the World grid
                    self.grid[y][x] = room

                    # update iterators
                    num_rooms -= 1
                    room_num += 1
                    previous_room = room

                    # connect the new room to the previous room
                    if previous_room is not None:
                        previous_room.connect_rooms(room, traveling)

                    # change direction
                    if (steps - 1) == 0:
                        traveling = 'n'

                elif traveling == 'w':
                    x += 1

                    # create a room and pass in (x, y)
                    room = Room(room_num, f"Room {room_num}", f"A generic description for room {room_num}", x, y)

                    # Save the room in the World grid
                    self.grid[y][x] = room

                    # connect the new room to the previous room
                    if previous_room is not None:
                        previous_room.connect_rooms(room, traveling)

                    # update iterators
                    num_rooms -= 1
                    room_num += 1
                    previous_room = room

                    # change direction
                    if (steps - 1) == 0:
                        traveling = 's'

                steps -= 1


            rnd += 1
            
w = World()
num_rooms = 21
width = 12
height = 12
w.generate_rooms(width, height, num_rooms)
print(w.grid)
