import { Client, Colors, Message } from 'discord.js'
import axios from 'axios'
import { EmbedBuilder } from '@discordjs/builders'

// This is just a part of an typescript discord bot

export default async (client: Client): Promise<void> => {
  client.on('messageCreate', async (msg: Message) => {
    if (msg.mentions.users.has(client.user?.id ?? '')) {
      const userIdRegex = new RegExp(`<@!?${client.user?.id ?? ''}>`)
      const content = msg.content.replace(userIdRegex, '').trim()
      try {
        const response = await axios.post(`http://127.0.0.1:1337/predict?msg=${content}`)
        switch (response.data.category) {
          case "greeting":
            await msg.channel.send({
              embeds: [
                buildResponse(msg, response.data.error, response.data.category, response.data.proba, `Hey <@${msg.member?.id ?? ''}>!`)
              ]
            })
            return
          case "undefined":
            return
        }
      } catch (error) {
        console.error(error)
      }
    }
  })
}

function buildResponse(msg: Message, error: string, category: string, proba: string, response: string): EmbedBuilder {
  let color: any = Colors.Grey
  if (error.length > 0) {
    color = Colors.Orange
  }
  return new EmbedBuilder().setAuthor({ iconURL: msg.author.avatarURL() ?? '', name: msg.author.username })
    .setColor(color)
    .setTimestamp()
    .setDescription(`**Response**: ${response} \n
    **Category**: ${category} \n
    **Proba**: ${proba}
    `)
}
