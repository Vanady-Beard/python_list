#Python List Transformation
#Task 1: Given the list of grades:


grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
print(grades)

# Task 2: Calculate the average grade from the list above and display it (reminder: The average is calculated by dividing the 
# sum of all grades by the length of the grades list).

sum = sum(grades)
average = sum/ (len(grades))
print (average)

#2. Advanced Slicing Techniques
#temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

new_temperature = temperatures[7:14:]
print(new_temperature)

#Task 2: Extract all the temperatures above 100 
# (reminder: when slicing to the end of a list you don't need a stop index).

end_temperature = temperatures[23::]
print(end_temperature)


#Task 3: extract temperatures from the 5th to the 10th.

cut_temperature = temperatures [5:11:]
print(cut_temperature)


