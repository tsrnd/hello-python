from player import Player
player = Player("phu", 24)
# player.add = "a2"
print("add", player.name)
# player.showInfo()
# print ("getattr(player1,'name') = ", getattr(player, "name", "age"), "age", getattr(player, "age")  )


# print("test att",hasattr(player,"add"))
# print("test att",setattr(player, "name", "aaasdfad"))

player1 = Player("Tom", 20)
 
 
player2 = Player("Jerry", 20)
 
# Truy cập thông qua tên lớp.
print ("Player.minAge = ", Player.minAge)
 
# Truy cập thông qua đối tượng.
print ("player1.minAge = ", player1.minAge) 
print ("player2.minAge = ", player2.minAge)
 

print("phu", dir(Player))
