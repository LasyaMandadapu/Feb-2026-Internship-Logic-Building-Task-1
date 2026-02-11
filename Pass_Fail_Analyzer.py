# Pass / Fail Analyzer
# This program counts how many students passed and failed.

# Given marks list
marks = [45, 78, 90, 33, 60]

# Counters for pass and fail students
pass_count = 0
fail_count = 0

# Check each student's marks
for mark in marks:
    if mark >= 50:
        pass_count += 1   # increase pass count
    else:
        fail_count += 1   # increase fail count

# Print final result
print("Total Students:", len(marks))
print("Number of Pass Students:", pass_count)
print("Number of Fail Students:", fail_count)