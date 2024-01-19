## 🤖 Welcome to the Discord.py Template!

This repo provides a starting point for creating your own Discord bot using Discord.py. Get your bot up and running quickly with predefined templates in the `templates` folder and customizable commands that you can add to the main file.

## Table of Contents

- [Templates](#templates)
- [Commands](#commands)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
  
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

## Packages

The default packages have been added to text file in the templates folder and should be installed by exectuting: 
     ```
     pip install -r requirements.txt
     ```
Any new packages required will be added to seperate .txt file inside of the command folder

## 🛠️ Installation

To get started with the Discord Bot, follow these simple steps:

1. **Clone the Repository** ⬇️

   ```bash
   git clone https://github.com/DanG115/discord.py-template.git
   cd default_templates
2. **Create a Discord Application** 🤖

   - Visit the Discord Developer Portal.
   - Click the "New Application" button.
   - Give your application a name (e.g., "Bot").
   - Navigate to the "Bot" tab and click "Add Bot."

3. **Get Your Bot Token** 🔑

   - Under the "Token" section, click "Copy" to copy your bot token
     

4. **Invite the Bot to Your Server** 💌

   - Construct an invite link for your bot using this URL format:

     ```
     https://discordapp.com/oauth2/authorize?client_id=YOUR_BOT_ID&scope=bot&permissions=ADMINISTRATOR
     ```

   - Replace `YOUR_BOT_ID` with your bot's client ID.

5. **Configure Your Bot** ⚙️

   - Paste your bot token into the `.env` file with this format:

     ```
     DISCORD_BOT_TOKEN=your-bot-token
     ```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on [GitHub](https://github.com/dang115/discord.py-template).

## License

This project is licensed under the [Apache License](https://github.com/DanG115/discord.py-template?tab=Apache-2.0-1-ov-file#readme).

## Contact

If you have any questions or feedback, you can reach out to me here: [https://dan-gleeson.co.uk/contact](https://dan-gleeson.co.uk/contact)

---
[GitHub Repository](https://github.com/dang115/discord.py-template)

