cars = 100
spaceInACar = 4.0
drivers = 30
passengers = 90
carsNotDriven = cars-drivers
carsDriven = drivers
carPoolCapacity = carsDriven*spaceInACar
averagePassengerPerCar = passengers/carsDriven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.") 
print("There will be", carsNotDriven, "empty cars today.") 
print("We can transport", carPoolCapacity, "people today.") 
print("We have", passengers, "to carpool today.") 
print("We need to put about", averagePassengerPerCar, "in each car.")
