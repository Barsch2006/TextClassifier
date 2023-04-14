import dotenv from 'dotenv'
import { Client, IntentsBitField } from 'discord.js'
import aiSpeek from './aiSpeek'
dotenv.config()

const token = process.env.BOT_TOKEN
async function init (): Promise<void> {

    const client = new Client({
        intents: [
          IntentsBitField.Flags.Guilds,
          IntentsBitField.Flags.GuildMessageReactions,
          IntentsBitField.Flags.MessageContent,
          IntentsBitField.Flags.GuildMessages
        ]
      })

      await aiSpeek(client)

      await client.login(token)
}

void init()
