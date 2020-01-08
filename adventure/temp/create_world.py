from django.contrib.auth.models import User
from adventure.models import Player, Room
from generator import World


def create_world():
  Room.objects.all().delete()

  w = World()
  num_rooms = 100
  width = 50
  height = 50
  w.generate_rooms(width, height, num_rooms)
  
  players=Player.objects.all()
  for p in players:
    p.currentRoom=r_outside.id
    p.save()

  return w, players