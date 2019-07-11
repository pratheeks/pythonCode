import pandas 
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]


# Create dictionary my_dict with three key:value pairs: my_dict

my_dict={'country':names,'drivers-right':dr,'cars_per_cap':cpc}

# Build a DataFrame cars from my_dict: cars

cars=pandas.DataFrame(my_dict)

# Print cars
print(cars)