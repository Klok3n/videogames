n = 33000
p = Entities.Pumpkin
d = Entities.Dead_Pumpkin
c = Entities.Carrot
g = Entities.Grass
b = Entities.Bush
t = Entities.Tree
h = Items.Hay
w = Items.Wood
wat = Items.Water
car = Items.Carrot
pum = Items.Pumpkin
soil = Grounds.soil
grassland = Grounds.Grassland

#Defined functions list.
#############################################################################################
#Reset drone
def zero():
	for i in range(get_pos_x()): #Resets to position 0,0.
		move(West)
	for i in range(get_pos_y()):
		move(South)
#############################################################################################
#plant grass
def plantgrass():
	if num_items(h) <= n: #Checks for hay
		for i in range(get_world_size()):
			for i in range(get_world_size()):
				if can_harvest():
					harvest()
				if get_entity_type() == None or g:#Checks for anything still present.
					if get_ground_type() == soil:#Changes to grasslands before planting
						till()
					plant(g)
				move(North)
			move(East)
	zero() #Recenters drone on origin
##########################################################################################
#Plant wood.
def plantwood():
	if num_items(w) <= n: #Checks for wood
		for i in range(get_world_size()):
			for i in range(get_world_size()):
				if can_harvest():
					harvest()
				if get_pos_x() % 2 == 0: #Alternates planting pattern
					if get_pos_y() % 2 == 1:
						plant(b)
					elif get_pos_y() % 2 == 0:
						plant(t)
				if get_pos_x() % 2 == 1:
					if get_pos_y() % 2 == 1:
						plant(t)
					elif get_pos_y() % 2 == 0:
						plant(b)
				move(North)
			move(East)
	zero() #Recenters drone on origin
#########################################################################################	
#Plant Carrots
def plantcarrots():
	if num_items(car) <= n: #Checks for carrots.
			for i in range(get_world_size()):
				for i in range(get_world_size()):
					if can_harvest():
						harvest()
					if get_entity_type() == None or g:#Checks for anything still present.
						if get_ground_type() == grassland:#Changes ground before planting
							till()
							plant(c)
						else:
							plant(c)
					move(North)
				move(East)
	zero() #Recenters drone on origin
	
########################################################################################
#Plant Pumpkins
def plantpumkins():
	if num_items(pum) <= n: #Checks for pumpkin qty.
		if num_items(car) >= n:
			for i in range(get_world_size()): #Harvests eaverything starting from origin, and plants pumpkins.
				for i in range(get_world_size()):
					if can_harvest() == True:
						harvest()
					if get_ground_type() == grassland:
						till()
					plant(p)
					move(North)
				move(East)
			for i in range(get_pos_x()): #Resets to position 0,0.
				move(West)
			for i in range(get_pos_y()):
				move(South)
				
			isdead = True

			while(isdead) == True: #Checks for dead pumpkins.
				isdead = False
				for i in range(get_world_size()):
					for i in range(get_world_size()):
						if get_entity_type() == d:
							isdead = True
							plant(p)
						move(North)
					move(East)
	zero() #Recenters drone on origin
	
#################################################################################################	
while(True):
	if num_items(h) < n:
		plantgrass()
	if num_items(w) <= n:
		plantwood()
	if num_items(car) <= n:
		plantcarrots()
	if num_items(pum) <= n:
		plantpumkins()
	if num_items(car) <= n:
		plantcarrots()