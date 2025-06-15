from datetime import datetime, timedelta
from collections import defaultdict

# Read input from file
with open("timelog.log", "r") as f:
    input_text = f.read()

# Split into individual days
days = input_text.strip().split("\n\n")

# Initialize output and duration tracking
processed_lines = []
task_durations = defaultdict(timedelta)

# Function to parse one day's schedule
def parse_day(day_text):
    lines = day_text.strip().split("\n")
    events = []
    for line in lines:
        time_str, task = line.split(" ", 1)
        time_obj = datetime.strptime(time_str, "%H:%M")
        events.append((time_obj, task))
    return events

# Process each day's events
for day in days:
    events = parse_day(day)
    for i in range(len(events) - 1):
        start_time, task = events[i]
        end_time, _ = events[i + 1]
        duration = end_time - start_time
        task_durations[task] += duration
        line = f"{start_time.strftime('%H:%M')}-{end_time.strftime('%H:%M')} {task}"
        processed_lines.append(line)
    processed_lines.append("")  # Empty line after each day

# Add one more blank line after day reports
processed_lines.append("")

# Total time for percentage calculation
total_duration = sum(task_durations.values(), timedelta())

# Create the summary
for task, duration in sorted(task_durations.items()):
    minutes = int(duration.total_seconds() // 60)
    percent = int((duration / total_duration) * 100)
    summary_line = f"{task}\t{minutes} minutes\t{percent}%"
    processed_lines.append(summary_line)

# Final output
final_output = "\n".join(processed_lines)

# Save to a file
with open("timelog.txt", "w") as f:
    f.write(final_output)

print("Report successfully generated and saved to 'timelog.txt'.")
