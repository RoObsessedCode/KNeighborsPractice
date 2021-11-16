star_wars = [125, 1977, 11000000]
raiders = [115, 1981, 18000000]
mean_girls = [97, 2004, 17000000]

def distance(movie1, movie2):
  sumTotal = 0
  for dim in range(len(movie1)):
    sumTotal += (movie1[dim] - movie2[dim]) ** 2

  distance = sumTotal ** 0.5
  return distance
