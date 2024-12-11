# Telegram Bot by Girish Sonune

This is a simple Telegram bot built using Python and the `python-telegram-bot` library. The bot provides various commands and functionalities to interact with users, offering helpful information about the creator and how to connect with him.

## Features

- **Start Command**: Greets the user and initiates interaction.
- **Help Menu**: Provides a list of available commands and their descriptions.
- **Content Command**: Shares information about the bot creator, Girish Sonune.
- **Contact Command**: Provides links to the creator's social media and professional profiles.
- **Message Handler**: Echoes any message mentioning the bot.

## Installation

### Prerequisites

- Python 3.6+
- `python-telegram-bot` library
- `.env` file with a valid Telegram Bot API token

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/GirishSonune/telegram-bot.git
   cd telegram-bot
   ```

2. Install dependencies:

   ```bash
   pip install python-telegram-bot python-dotenv
   ```

3. Create a `.env` file and add your bot token:

   ```env
   TOKEN=your_telegram_bot_token
   ```

4. Run the bot:

   ```bash
   python bot.py
   ```

## Commands

| Command    | Description                                        |
|------------|----------------------------------------------------|
| `/start`   | Starts the bot and sends a welcome message.        |
| `/help`    | Displays the help menu with all available commands.|
| `/content` | Shares information about the bot and its creator.  |
| `/contact` | Provides links to connect with the creator.        |

## Creator Info

- **Name**: Girish Sonune
- **Portfolio**: [Portfolio Website](https://girishsonune.github.io/New-Portfolio/)
- **LinkedIn**: [Girish Sonune](https://www.linkedin.com/in/girish-sonune-7a7090255)
- **GitHub**: [GirishSonune](https://github.com/GirishSonune)

For a full list of social media links, use the `/contact` command in the bot.

## Logging

The bot logs its activity using Python's `logging` module. Logs are output to the console and include timestamps, log levels, and messages.

## Contributing

If you'd like to contribute:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

- [python-telegram-bot](https://python-telegram-bot.readthedocs.io/) for providing an excellent library to build Telegram bots.
- [dotenv](https://pypi.org/project/python-dotenv/) for managing environment variables.

## Contact

For any inquiries, please reach out to Girish Sonune via the [contact command](#commands) or directly on his [LinkedIn profile](https://www.linkedin.com/in/girish-sonune-7a7090255).
