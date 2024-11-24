
# Analyze Reply Time

This Python program analyzes the average reply time from a chat history file. It allows you to exclude replies that exceed a specified threshold interval.

## Prerequisites

1. Ensure you have Python installed (version 3.7 or higher is recommended).
2. Install the necessary libraries using the `requirements.txt` file.

## Installation

1. Clone or download this repository.
2. Navigate to the folder containing the project files.
3. Install the required libraries by running:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To execute the program, run the following command:

```bash
python analyze_reply_time.py file_name_of_chat_history threshold_interval_to_exclude [picture_width]
```


### Parameters:
- **file_name_of_chat_history**: The name of the chat history file in `.txt` format. Ensure the file is in the same folder as the script.
- **threshold_interval_to_exclude**: The threshold interval (in hours) for excluding replies. For example, set `5` to exclude replies longer than 5 hours.
- **picture_width (optional)**: The width of the output picture (in inches). Defaults to `20`. Adjust this parameter if the chat history is very long, and the output looks squeezed.

### Example:

```bash
python analyze_reply_time.py chat_history.txt 5 25
```

This will analyze the `chat_history.txt` file, exclude any replies with an interval exceeding 5 hours, and produce a plot with a width of 25 inches.

## Input Format

The chat history file should follow this structure:
- Each day begins with a date header in the format: `YYYY/MM/DD（Day）`
- Messages are in the format: `time<tab>name<space>message`
- Example:
  ```
  2024/06/11（二）
  下午12:42	John	Hello there!
  下午01:00	Alice	Hi, John!
  ```

## Output

The program outputs:
1. **Average Reply Times**: Displays the average reply time for each participant.
2. **Visualizations**:
   - A plot showing average reply times over days.
   - A plot showing total chat sentences over time.


