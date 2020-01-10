from django.contrib.auth.models import User
from adventure.models import Player, Room

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
    # set first room
    room_num = 1

    # initialize with one step 
    steps = 1

    traveling = 'n'

    # rnd(round) is one continous cycle without increasing steps
    rnd = 1

    # create room at center
    room = Room(room_num, f"Room {room_num}", f"A generic description for room {room_num}")
    room.addCoordinates(start_x, start_y)
    
    # Save the room in the World grid
    self.grid[start_y][start_x] = room
    room.save()

    # update iterators
    num_rooms -= 1
    room_num += 1
    previous_room = room

    x = position[0]
    y = position[1]

    while num_rooms > 0:
      steps = rnd * 2

      while steps:
        if traveling == 'n':
          y += 1

          # create a room and pass in (x, y)
          room = Room(room_num, f"Room {room_num}", f"A generic description for room {room_num}")
          room.addCoordinates(x, y)
          room.connectRooms(previous_room, 's')

          # Save the room in the World grid
          self.grid[y][x] = room
          room.save()

          # connect the new room to the previous room
          if previous_room is not None:
            previous_room.connectRooms(room, traveling)
          
          # if wall, turn left
          if rnd == steps - 1:
            traveling = 'w'

          # update iterators
          num_rooms -= 1
          room_num += 1
          previous_room = room

        elif traveling == 's':
          y -= 1

          # create a room and pass in (x, y)
          room = Room(room_num, f"Room {room_num}", f"A generic description for room {room_num}")
          room.addCoordinates(x, y)
          room.connectRooms(previous_room, 'n')

          # Save the room in the World grid
          self.grid[y][x] = room
          room.save()

          # connect the new room to the previous room
          if previous_room is not None:
            previous_room.connectRooms(room, traveling)

          # if wall, turn left
          if rnd == steps - 1:
            # 1: turn W
            traveling = 'e'

          # update iterators
          num_rooms -= 1
          room_num += 1
          previous_room = room

        elif traveling == 'e':
          x += 1

          # create a room and pass in (x, y)
          room = Room(room_num, f"Room {room_num}", f"A generic description for room {room_num}")
          room.addCoordinates(x, y)
          room.connectRooms(previous_room, 'w')

          # Save the room in the World grid
          self.grid[y][x] = room
          room.save()

          # connect the new room to the previous room
          if previous_room is not None:
            previous_room.connectRooms(room, traveling)

          # change direction
          if (steps - 1) == 0:
            traveling = 'n'

          # update iterators
          num_rooms -= 1
          room_num += 1
          previous_room = room

        elif traveling == 'w':
          x -= 1

          # create a room and pass in (x, y)
          room = Room(room_num, f"Room {room_num}", f"A generic description for room {room_num}")
          room.addCoordinates(x, y)
          room.connectRooms(previous_room, 'e')

          # Save the room in the World grid
          self.grid[y][x] = room
          room.save()

          # connect the new room to the previous room
          if previous_room is not None:
            previous_room.connectRooms(room, traveling)

          # change direction
          if (steps - 1) == 0:
            traveling = 's'

          # update iterators
          num_rooms -= 1
          room_num += 1
          previous_room = room

        steps -= 1

      rnd += 1


def create_world():
  Room.objects.all().delete()

  w = World()
  num_rooms = 100
  width = 50
  height = 50
  w.generate_rooms(width, height, num_rooms)

  # deleted the last room to make map symetrical
  last=len(Room.objects.all())
  Room.objects.filter(id=last).delete()

  players=Player.objects.all()
  for p in players:
    p.currentRoom=0
    p.save()
  
create_world()