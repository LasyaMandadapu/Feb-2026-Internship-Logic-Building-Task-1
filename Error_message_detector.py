# this program counts how many "ERROR" messages are present in system logs
#Given list of logs
logs = ["INFO", "ERROR", "WARNING", "ERROR"]
error_count = 0
# check each log entry 
for log in logs:
    if log == "ERROR":
        error_count += 1
print("Total ERROR messages:", error_count)
