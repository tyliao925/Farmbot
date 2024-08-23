from datetime import datetime, timedelta

# Get the current UTC time
current_time = datetime.utcnow()

# Format the current time in ISO 8601 format with "Z" for UTC
start_time = current_time.isoformat() + "Z"

# Calculate the end time by adding 1 hour to the start time
end_time = (current_time + timedelta(hours=1)).isoformat() + "Z"

print("Start Time:", start_time)
print("End Time:", end_time)
