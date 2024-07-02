# Bitcoin-Solana Swap Telegram Bot ( Front-End ONLY)

This Telegram bot facilitates swapping Bitcoin for Solana. Users can register with a Bitcoin address, receive a Solana wallet, and initiate swaps through a simple interface.

## Project Structure

project_root/
│
├── bot/
│ ├── init.py
│ ├── handlers/
│ │ ├── init.py
│ │ ├── start.py
│ │ ├── btc_address.py
│ │ ├── menu.py
│ │ └── button_handlers.py
│ ├── utils/
│ │ ├── init.py
│ │ ├── validators.py
│ │ └── api_client.py
│ └── config.py
│
├── database/
│ ├── init.py
│ └── mongo_client.py
│
├── main.py
├── requirements.txt
└── README.md

### Bot Directory

- `config.py`: Contains configuration variables and loads environment variables.
- `handlers/`:
  - `start.py`: Handles the /start command and initiates user registration.
  - `btc_address.py`: Processes and validates the Bitcoin address provided by the user.
  - `menu.py`: Manages the main menu interface of the bot.
  - `button_handlers.py`: Contains handlers for various button actions in the bot.
- `utils/`:
  - `validators.py`: Provides utility functions for input validation (e.g., Bitcoin address format).
  - `api_client.py`: Handles communication with the Rust backend API.

### Database Directory

- `mongo_client.py`: Manages the connection to MongoDB and provides functions for database operations.

### Root Directory

- `main.py`: The entry point of the application. Sets up the Telegram bot and connects handlers.
- `requirements.txt`: Lists all Python dependencies required for the project.

## How It Works

1. User Interaction:

   - Users start by sending the `/start` command to the bot.
   - If not registered, they are prompted to provide a Bitcoin address.
   - Once registered, users can access various functions through the main menu.

2. Registration Process:

   - The bot validates the provided Bitcoin address.
   - It communicates with a Rust backend to create a Solana wallet for the user. Also iside of the rust back end uses Kraken for swaping btc-sol
   - User details are stored in MongoDB for future interactions.

3. Main Functionality:

   - Users can initiate a Bitcoin to Solana swap.
   - They can export their Solana private key.

4. Backend Communication:

   - The bot interacts with a Rust backend for critical operations like wallet creation and key management.
   - API calls are made asynchronously to ensure responsive bot behavior.

5. Database Operations:
   - User data is stored and retrieved from MongoDB.
   - Asynchronous database operations are used to maintain performance.

## Setup and Running

1. Install dependencies:

```python
pip install -r requirements.txt
```

2. Set up environment variables:

- Create a `.env` file in the project root with the following variables:

  ```python
  TELEGRAM_BOT_TOKEN=your_bot_token
  RUST_BACKEND_URL=url_of_your_rust_backend
  MONGO_URI=your_mongodb_connection_string
  ```

3. Run the bot:

```python
python main.py
```

## Future Improvements

- Implement comprehensive error handling and user feedback.

### TODO: Implement Notification System

- Add a webhook-based notification system using Helius for Solana transactions dont know for bitcoin or maybe custom webhook:
  - Set up webhook to receive updates from Helius.
  - Create a handler to process incoming notifications.
  - Develop a system to send user-friendly notifications via the bot.
  - (maybe)Add user commands to manage notification preferences.
  - Implement security measures for the webhook endpoint.
  - Test the notification system thoroughly.
