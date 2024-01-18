## 🤖 Welcome to the Discord.py Template!

This repo provides a starting point for creating your own Discord bot using Discord.py. Get your bot up and running quickly with predefined templates in the `templates` folder and customizable commands that you can add to the main file.

## 📂 Templates

Explore the `templates` folder to find Discord.py templates that serve as a foundation for your bot's functionality.

- [Template 1](https://github.com/DanG115/discord-bots/tree/main/Default%20Template(s))
  
## 🚀 Commands

Enhance your bot by adding custom commands to the main file. The template is designed to be extensible, allowing you to tailor the bot to your specific needs.

### Example Command:

```python
@bot.command(name='hello', help='Responds with a hello message.')
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}!')
```

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Description

The Discord Nuke Bot is a powerful utility bot designed for administrators of Discord servers. It provides a set of commands to perform administrative actions, including banning members, deleting channels, and creating a designated "nuke" channel.

## Features

- **Server Nuking**: Use the `!fn` command to fully nuke a server, banning all members and deleting all channels except for the nuke channel.
- **Command Help**: Use the `!help` command to display a list of available commands and their descriptions.

## 🛠️ Installation

To get started with the Discord Nuke Bot, follow these simple steps:

1. **Clone the Repository** ⬇️

   ```bash
   git clone https://github.com/DanG4115/nukebot_discord.git
   cd nukebot_discord
2. **Create a Discord Application** 🤖

   - Visit the Discord Developer Portal.
   - Click the "New Application" button.
   - Give your application a name (e.g., "Nuke Bot").
   - Navigate to the "Bot" tab and click "Add Bot."

3. **Get Your Bot Token** 🔑

   - Under the "Token" section, click "Copy" to copy your bot token.

4. **Invite the Bot to Your Server** 💌

   - Construct an invite link for your bot using this URL format:

     ```
     https://discordapp.com/oauth2/authorize?client_id=YOUR_BOT_ID&scope=bot&permissions=ADMINISTRATOR
     ```

   - Replace `YOUR_BOT_ID` with your bot's client ID.

5. **Configure Your Bot** ⚙️

   - Create a `.env` file in the project directory.
   - Paste your bot token into the `.env` file with this format:

     ```
     DISCORD_TOKEN=your-bot-token
     ```

6. **Run the Bot** 🚀

   ```bash
   python bot.py


## Usage

1. Ensure the Discord Nuke Bot is a member of your server with the necessary permissions (e.g., `ADMINISTRATOR`).

2. In any text channel, use the following command to fully nuke the server:


## Commands

- `!fn` - Fully nuke the server (Ban all members and delete all channels except for the nuke channel).
- `!help` - Display a list of available commands and their descriptions.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on [GitHub](https://github.com/YourGitHubUsername/discord-nuke-bot).

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or feedback, you can reach out to me at your@email.com.

---
[GitHub Repository](https://github.com/YourGitHubUsername/discord-nuke-bot)
