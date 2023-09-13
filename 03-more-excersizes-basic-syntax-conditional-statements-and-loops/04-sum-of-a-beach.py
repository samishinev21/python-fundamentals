mesh_of_words = input().lower()
points = 0

count_of_sand = mesh_of_words.count("sand")
count_of_water = mesh_of_words.count("water")
count_of_fish = mesh_of_words.count("fish")
count_of_sun = mesh_of_words.count("sun")

points += count_of_sand
points += count_of_water
points += count_of_fish
points += count_of_sun

print(points)