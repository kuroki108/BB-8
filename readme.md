# BB-8: Your Friendly Discord Movie Droid 🤖🎬

Beep-boop! BB-8 reporting for duty!

BB-8 is a lightweight, slightly sarcastic Discord bot who LOVES movies and guessing games. Originally designed to impress one (1) human female — mission status: CONFIDENTIAL — he now serves all who dare summon him.

----

## 🤖 Features

🎥 **Random Movie Recommender**  
BB-8 will suggest a random film from his personal favorites list. Great for date nights, boredom, or proving you have *impeccable* taste in cinema.

🎲 **Number Guessing Game**  
Bored? BB-8 will think of a number, and you’ll try to guess it. If you win, he'll probably pretend not to be impressed. If you lose… well, he’s a droid, he never forgets.

---

## 💬 Commands

`!movie` – BB-8 drops a hot movie pick, no popcorn required.

`!play` – Start the number guessing game. You versus a machine with no feelings. Good luck.

---

## 🔧 Installation

1. Clone the bot.
2. Add your Discord token.
3. Run BB-8.
4. Try not to fall in love.

---

## 🐳 Docker

### Prepare

1. Create an `.env` file in the project root with:

```
DISCORD_TOKEN=your-token-here
```

2. Build and run with Docker Compose:

```
docker compose up -d --build
```

3. View logs:

```
docker compose logs -f
```

4. Stop the bot:

```
docker compose down
```