# We start with a single string representing raw data, now updated with the new names.
raw_data = "Mario:85 Piattos:92 Gemini:78 Chadgipiti:95"

# 1. Splitting strings into lists
# When you do not specify a delimiter, multiple spaces are treated like one delimiter.
student_records = raw_data.split()

# 2. Building a List from Scratch
# We create an empty list to store our final extracted numbers.
grades = list() 

# 3. Lists and Definite Loops
# We construct a loop to go through each record in our collection.
for record in student_records:
    
    # 4. The Double Split Pattern
    # We grab one piece of the line and split that piece again using a specific delimiter.
    pieces = record.split(':')
    
    # The grade is the second item (index 1) after splitting by ':'
    score = float(pieces[1])
    
    # 5. Using the append method
    # The list stays in order and new elements are added at the end of the list.
    grades.append(score)

print("Initial extracted grades:", grades)

# 6. Lists are Mutable
# We can change an element of a list using the index operator.
# Let's say the first student (Mario) gets a 5-point bonus.
grades[0] = grades[0] + 5.0
print("Grades after mutability change:", grades)

# 7. Concatenating Lists Using +
# We can create a new list by adding two existing lists together.
late_submissions = [100.0, 88.5]
all_grades = grades + late_submissions
print("Combined list of all grades:", all_grades)

# 8. Lists Can Be Sliced Using :
# Just like in strings, the second number is "up to but not including".
first_two_grades = all_grades[0:2]
print("Sliced list (first two grades):", first_two_grades)

# 9. Is Something in a List?
# We use a logical operator that returns True or False.
has_perfect_score = 100.0 in all_grades
print("Is there a 100.0 in the list?", has_perfect_score)

# 10. Lists are in Order (Sorting)
# A list can be sorted, and the sort method means "sort yourself".
all_grades.sort()
print("Sorted grades from lowest to highest:", all_grades)

# 11. Built-in Functions and Lists
# Python provides functions that take lists as parameters to perform simple calculations.
total_sum = sum(all_grades)
count = len(all_grades)
average = total_sum / count

print("--- Final Statistics ---")
print("Highest grade:", max(all_grades))
print("Lowest grade:", min(all_grades))
print("Average grade:", average)