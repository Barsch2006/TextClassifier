import { Client, Message } from 'discord.js'
import { ILogger } from '../logger/logger'
import axios from 'axios'

// This is just a part of an typescript discord bot

export default async (client: Client, logger: ILogger): Promise<void> => {
  client.on('messageCreate', async (msg: Message) => {
    if (msg.mentions.users.has(client.user?.id ?? '')) {
      const userIdRegex = new RegExp(`<@!?${client.user?.id ?? ''}>`)
      const content = msg.content.replace(userIdRegex, '').trim()
      try {
        const response = await axios.post(`http://127.0.0.1:1337/predict?msg=${content}`)
        console.log(response.data)
        switch (response.data.category) {
          case "greeting":
            await msg.channel.send(`Hey <@${msg.member?.id ?? ''}>!`)
            return
          case "question":
            await msg.channel.send(`Question`)
            return
          case "search":
            await msg.channel.send(`Search`)
            return
          case "undefined":
            await msg.channel.send(`undefined`)
            return
        }
      } catch (error) {
        console.error(error)
      }
    }
  })
}
