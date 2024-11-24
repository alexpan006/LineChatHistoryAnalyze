from datetime import datetime, timedelta
from collections import defaultdict
import re
from matplotlib import rcParams
import matplotlib.font_manager as fm
import sys
import pandas as pd
import matplotlib.pyplot as plt
import platform
# Helper function to parse dates and times
def parse_date_time(date_str, time_str):
    am_pm = 'PM' if '下午' in time_str else 'AM'
    time_str = time_str.replace('下午', '').replace('上午', '').strip()
    full_datetime_str = f"{date_str} {time_str} {am_pm}"
    return datetime.strptime(full_datetime_str, "%Y/%m/%d %I:%M %p")

# Function to calculate average reply time by day with a threshold
def calculate_avg_reply_time_by_day(chat_data, threshold_hours=5):
    daily_response_times = defaultdict(lambda: defaultdict(list))
    last_message_by = None
    last_message_time = None
    current_date = None

    for timestamp, sender, message in chat_data:
        if current_date != timestamp.date():  # New day
            current_date = timestamp.date()
            last_message_by = None  # Reset for the new day
        
        if last_message_by and sender != last_message_by:
            response_time = timestamp - last_message_time
            if response_time <= timedelta(hours=threshold_hours):
                daily_response_times[current_date][last_message_by].append(response_time.total_seconds() / 60)
        
        last_message_by = sender
        last_message_time = timestamp

    # Calculate averages
    daily_avg_response_time = {}
    for date, responses in daily_response_times.items():
        daily_avg_response_time[date] = {
            sender: sum(times) / len(times) for sender, times in responses.items()
        }
    return daily_avg_response_time


# ---------------------- Config Part-------------------------
file_path = sys.argv[1]  # Replace with the path to your file
threshold_hours=int(sys.argv[2])
if len(sys.argv) > 3:
    picture_width = sys.argv[3]
else:
    picture_width = 20
 
#Font setting
# Detect operating system
if platform.system() == "Darwin":  # macOS
    rcParams['font.family'] = ['PingFang TC', 'Apple Color Emoji']
elif platform.system() == "Windows":
    rcParams['font.family'] = ['Microsoft JhengHei', 'Segoe UI Emoji']
else:
    rcParams['font.family'] = ['DejaVu Sans']
   

# ---------------------- Config Part-------------------------



# Read the content of the file
with open(file_path, "r", encoding="utf-8") as file:
    file_content = file.read()

# The rest of the script remains unchanged
# Extract chat data
chat_data = []
current_date = None

lines = file_content.strip().split('\n')
for line in lines:
    if re.match(r'\d{4}/\d{2}/\d{2}', line):  # Date header
        current_date = line.split('（')[0].strip()
    elif re.match(r'(下午|上午)\d{1,2}:\d{2}', line):  # Chat line
        time, sender, message = line.split('\t', 2)
        timestamp = parse_date_time(current_date, time)
        chat_data.append((timestamp, sender, message.strip()))
        
daily_avg_response_time = calculate_avg_reply_time_by_day(chat_data, threshold_hours)



# Display results in a table for clarity
df = pd.DataFrame.from_dict(daily_avg_response_time, orient='index').stack().reset_index()
df.columns = ['Date', 'Sender', 'Average Reply Time (minutes)']
df.sort_values(by='Date', inplace=True)


# Calculate total chat sentences per day
daily_chat_counts = defaultdict(int)

for timestamp, sender, message in chat_data:
    daily_chat_counts[timestamp.date()] += 1

# Add total chat counts to the dataframe
df['Total Chat Sentences'] = df['Date'].map(lambda date: daily_chat_counts[date])




output_file= ' avg_reply_time_over_days.png'
# Pivot data for plotting
plot_data = df.pivot(index='Date', columns='Sender', values='Average Reply Time (minutes)')

# Plot the line chart
plt.figure(figsize=(int(picture_width), 6))
for sender in plot_data.columns:
    plt.plot(plot_data.index, plot_data[sender], marker='.', label=sender)

# Configure chart details
plt.title("Average Reply Time Over Days", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Average Reply Time (minutes)", fontsize=12)
plt.xticks(rotation=45)
plt.legend(title="Sender")
plt.grid(alpha=0.3)

# Show the plot
plt.tight_layout()
plt.savefig(output_file, format='png', dpi=300)  # Save as PNG with 300 DPI
plt.show()


# Prepare data for plotting
output_file = "total_chat_sentences_over_time.png"
total_chat_data = pd.DataFrame(list(daily_chat_counts.items()), columns=['Date', 'Total Chat Sentences'])
total_chat_data.sort_values(by='Date', inplace=True)
# print(picture_width)
# Plot the total chat sentences over time
plt.figure(figsize=(int(picture_width), 6))
plt.plot(total_chat_data['Date'], total_chat_data['Total Chat Sentences'], marker='.', label="Total Chat Sentences")

# Configure chart details
plt.title("Total Chat Sentences Over Time", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Total Chat Sentences", fontsize=12)
plt.xticks(rotation=45)
plt.grid(alpha=0.3)
plt.legend()

# Show the plot
plt.tight_layout()
plt.savefig(output_file, format='png', dpi=300)  # Save as PNG with 300 DPI
plt.show()
# print("done")