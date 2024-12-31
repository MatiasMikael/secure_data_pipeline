# Finnhub API Response Explanation

The Finnhub API returns stock data in JSON format. Below is an explanation of the response fields and their meanings:

- **`c`**: **Current price** – The current stock price.
  - Example: `252.2`

- **`d`**: **Change** – The change in price compared to the previous day's closing price.
  - Example: `-3.39`

- **`dp`**: **Percent change** – The percentage change compared to the previous day's closing price.
  - Example: `-1.3263` (approximately -1.33%).

- **`h`**: **High** – The highest price of the stock during the current trading day.
  - Example: `253.5`

- **`l`**: **Low** – The lowest price of the stock during the current trading day.
  - Example: `250.75`

- **`o`**: **Open** – The stock's opening price for the current trading day.
  - Example: `252.23`

- **`pc`**: **Previous close** – The stock's closing price from the previous trading day.
  - Example: `255.59`

- **`t`**: **Timestamp** – A Unix timestamp indicating when the data was last updated.
  - Example: `1735592400` (converted to UTC, this corresponds to `2024-12-31 14:00:00`).