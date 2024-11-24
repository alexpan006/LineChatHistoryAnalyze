(English version see below)

# 分析回覆時間

好奇朋友的回訊息速度嗎? 總是覺得只有我在付出嗎?
此 Python 程式可從聊天記錄檔案中分析平均回覆時間，使用科學的方式來檢視每日的平均回訊息速度，並允許排除超過特定閾值的回覆間隔(睡覺時)。

## 必要條件

1. 確保已安裝 Python（建議使用版本 3.7 或更高）。
2. 使用 `requirements.txt` 檔案安裝所需的函式庫。

## 安裝

1. 下載或克隆此存儲庫。
2. 將終端移至包含專案文件的資料夾。
3. 執行以下命令安裝所需的函式庫：
   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

執行以下命令運行程式：

```bash
python analyze_reply_time.py 聊天記錄檔案名 排除閾值 [圖片寬度]
```

### 參數說明：
- **聊天記錄檔案名**: 聊天記錄檔案的名稱（必須為 `.txt` 格式）。確保該檔案與程式位於同一資料夾中。
- **排除閾值**: 回覆時間超過該閾值（以小時為單位）的記錄將被排除。例如，設置為 `5` 將排除超過 5 小時的回覆。
- **圖片寬度（選填）**: 輸出圖片的寬度（單位：英寸），預設值為 `20`。若聊天記錄過長，輸出圖片可能過於擁擠，請根據需要調整此參數。

### 範例：

```bash
python analyze_reply_time.py chat_history.txt 5 25
```

此命令將分析 `chat_history.txt` 文件，排除超過 5 小時的回覆，並生成寬度為 25 英寸的圖表。

## 輸入格式

聊天記錄檔案應符合以下結構：
- 每天的開始以日期標頭表示，格式為：`YYYY/MM/DD（Day）`
- 每條消息的格式為：`時間<tab>姓名<空格>消息內容`
- 範例：
  ```
  2024/06/11（二）
  下午12:42	John	Hello there!
  下午01:00	Alice	Hi, John!
  ```

## 輸出

程式將輸出：
1. **平均回覆時間**：顯示每位參與者的平均回覆時間。
2. **視覺化圖表**：
   - 顯示每日平均回覆時間的折線圖。
   - 顯示聊天活躍程度的總數折線圖。

## 注意事項
 - 若名稱內含有Emoji或特殊字元可能會出bug，可以先把對方改名，再匯出聊天紀錄。
 - 匯出聊天紀錄可從手機->點選聊天室->右上角->設定->傳送聊天紀錄，再把txt檔傳送到電腦上。




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


