# importing math,pandas, and reading the csv file
import math
import pandas as pd
dataset = pd.read_csv(r'C:\Users\arcad\Desktop\cs455_homework2_harker_dataset.csv')

# separating the attributes into their own arrays
names = dataset['name'].to_numpy()
track_num = dataset['track_num'].to_numpy()
duration = dataset['duration_ms'].to_numpy()
popularity = dataset['popularity'].to_numpy()

# compute distance categorical function
def compute_distance_categorical(data):
    distance_matrix = []
    for i in range(len(data)):
        temp = []
        for j in range(len(data)):
            if (data[i] != data[j]):
                difference = 1
            else:
                difference = 0
            temp.append(difference)
        distance_matrix.append(temp)
    return distance_matrix

# normalizing numerical array
def normalize_numerical(data):
    maxValue = max(data)
    minValue = min(data)
    new_data = []
    for i in range(len(data)):
        new_value = round((data[i] - minValue)/ (maxValue - minValue ), 2)
        new_data.append(new_value)
    return new_data

# compute distance numerical function
def compute_distance_numerical(data):
    distance_matrix = []
    for i in range(len(data)):
        temp = []
        for j in range(len(data)):
            difference = round(math.fabs(data[i] - data[j]), 2)
            temp.append(difference)
        distance_matrix.append(temp)
    return distance_matrix

#compute distance ordinal function
def compute_distance_ordinal(data):
    distance_matrix = []
    rank_order = ['Very Low', 'Low', 'Average', 'High', 'Very High']
    for i in range(len(data)):
        temp = []
        for j in range(len(data)):
            rank_i = 0
            rank_j = 0
            for k in range(len(rank_order)):
                if (data[i] == rank_order[k]):
                    rank_i = k+1
                if (data[j] == rank_order[k]):
                    rank_j = k+1
                difference = round((math.fabs(rank_i-rank_j))/(len(rank_order)-1), 2)           
            temp.append(difference)
        distance_matrix.append(temp)
    return distance_matrix

# combine distance arrays function
def compute_distance_final(distance_num1, distance_num2, distance_cat, distance_or):
    distance_matrix = []
    for i in range(len(distance_num1)):
        temp = []
        for j in range(len(distance_num1)):
            sum = round((distance_num1[i][j] +  distance_num2[i][j] + distance_cat[i][j] + distance_or[i][j])*(1/4),2)          
            temp.append(sum)
        distance_matrix.append(temp)
    return distance_matrix

# normalize and calculate distance for different attributes
normal_tracks = normalize_numerical(track_num)
normal_duration = normalize_numerical(duration)
track_distance = compute_distance_numerical(normal_tracks)
duration_distance = compute_distance_numerical(normal_duration)
name_distance = compute_distance_categorical(names)
popularity_distance = compute_distance_ordinal(popularity)

# compute final distance
distance_matrix_final = compute_distance_final(track_distance, duration_distance, name_distance, popularity_distance)

#ask for input
desired_i = int(input("Input the first object index (0-99):  "))
desired_j = int(input("Input the second object index (0-99):  "))

#give output
distance = distance_matrix_final[desired_i][desired_j]
print(distance)
