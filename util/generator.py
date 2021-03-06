from adventure.models import Room

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

        traveling = 'n'

        # rnd(round) is one continous cycle without increasing steps
        rnd = 1

        # create room at center
        room = Room(room_num, f"Room {room_num}", f"A generic description for room {room_num}", start_x, start_y)
        
        # Save the room in the World grid
        self.grid[start_y][start_x] = room
        room.save()

        # update iterators
        num_rooms -= 1
        room_num += 1
        previous_room = None

        x = position[0]
        y = position[1]

        while num_rooms > 0:
            steps = rnd * 2

            while steps:
                if traveling == 'n':
                    y += 1

                    # if wall, turn left
                    if rnd == steps - 1:
                        traveling = 'w'

                    # create a room and pass in (x, y)
                    room = Room(room_num, f"Room {room_num}", f"A generic description for room {room_num}", x, y)

                    # Save the room in the World grid
                    self.grid[y][x] = room
                    room.save()

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
                    if rnd == steps - 1:
                        # 1: turn W
                        traveling = 'e'

                    # create a room and pass in (x, y)
                    room = Room(room_num, f"Room {room_num}", f"A generic description for room {room_num}", x, y)

                    # Save the room in the World grid
                    self.grid[y][x] = room
                    room.save()

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
                    room.save()

                    # connect the new room to the previous room
                    if previous_room is not None:
                        previous_room.connect_rooms(room, traveling)

                    # update iterators
                    num_rooms -= 1
                    room_num += 1
                    previous_room = room

                    # change direction
                    if (steps - 1) == 0:
                        traveling = 'n'

                elif traveling == 'w':
                    x -= 1

                    # create a room and pass in (x, y)
                    room = Room(room_num, f"Room {room_num}", f"A generic description for room {room_num}", x, y)

                    # Save the room in the World grid
                    self.grid[y][x] = room
                    room.save()

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
