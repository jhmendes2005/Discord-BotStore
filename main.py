import json
from modules import client as configClient
from extra import validate as Validate
import discord
from datetime import datetime
import time
from random import randint
import re
from discord.ext.commands import Bot
bot = Bot("!")

## python ./main.py

client = configClient.client
validate = Validate.validate
token = str
numeral = []

now = datetime.now()

with open("./config.exemplo.json") as f:
    config = json.load(f)
    token = config['token']


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Developed By BOT´S STORE"))
    print('Pronto para uso!')
    print(f'Nome: {client.user}')
    print("User ID: {}".format(client.user.id))
    print("Ping: {}.".format(round(client.latency * 1000)))
    print("Data:{}/{}/{} || Hora: {}:{}. ".format(now.day,
                                                  now.month, now.year, now.hour, now.minute))
    print(bot.commands)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "discord.gg" in message.content:  # Check if message has "discord.gg"
        await message.delete()

        embed = discord.Embed(
            title="PROIBIDO CONVITES NESTE SERVIDOR!!",
            color=255,
            description="Cuidado, nossos ADM's ficarão de olho em você, a próxima pode se resultar em Banimentos!\n\nInfrator: {}".format(message.author.mention),

        )

        embed2 = discord.Embed(
            title="TENTATIVA DE ENVIO DE CONVITE",
            color=255,
            description="O infrator: {} mandou um convite em nosso servidor!\nConvite: {}\n\nPara bani-lo, digite '>ban @usuario', ou para kicka-lo, basta digitar '>kick @usuario'".format(message.author.mention, message.content),

        )

        channel = client.get_channel(854187604399357952)
        await message.channel.send(embed=embed)
        await channel.send(embed=embed2)
        await channel.send("@here")

    await validate.checkMessage(message)
    await validate.checkCommand(message)


@client.event  # entrada
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="NÃO-VERIFICADO")
    await member.add_roles(role)
    vermelho = 255
    embed = discord.Embed(
        title="**SEJA BEM VINDO(A)**",
        color=vermelho,
        description="- Leia as Regras do Servidor em: #『regras』 \n- Convide seus Amigos \n- Divirta-se!\n Boas Compras! \n \n 🥰🥰🥰🥰\n{} \n\n".format(
            member.mention),

    )

    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text="Developed By BOT'S STORE.py", icon_url=client.user.avatar_url)
    await member.send(embed=embed)
    channel = client.get_channel(854188681421389855)
    await channel.send(embed=embed)


@client.event  # saida
async def on_member_remove(member):
    vermelho = 255
    embed = discord.Embed(
        title="**SAIU DO SERVIDOR**",
        color=vermelho,
        description="😪😪😪😪",

    )
    channel = client.get_channel(854188780230934529)
    await channel.send(member.mention, embed=embed)


@client.event
async def on_raw_reaction_add(payload):
    #DEFINIÇÃO GUILD
    guild = client.get_guild(payload.guild_id)

    #ID'S
    message_id = payload.message_id
    userID = payload.user_id
    channelID = payload.channel_id
    clientID = client.user.id

    #EMOJI ID'S
    cancelamentoEmojiID = 865722854603096064
    confirmacaoEmojiID = 865722659484205118
    entregaPedidoEmojiID = 865794124904661012
    emojiID = payload.emoji.id

    #NOMES
    user = payload.member
    nomeEmoji = payload.emoji.name
    nome_da_sala = payload.member.name

    #AWAIT ACTIONS
    member = guild.get_member(payload.user_id)
    channel = client.get_channel(payload.channel_id)
    mencaoReactMembro = payload.member.mention

    #ID'S CANAIS E MENSAGENS
    messageTicketID = 864617981999710270
    verificacaoMessageID = 864620099994648576
    pedidosChannelID = 864683201045463040

    #REACTION CHANNEL
    messageReaction = await channel.fetch_message(message_id)

    #EMOJIS NAMES
    emojiMessageTicket = "📩"
    emojiMessageCloseTicket = "🔒"

    #CARGOS VERIFICACAO
    naoVerificadoRole = "NÃO-VERIFICADO"
    verificadoRole = "MEMBROS |👤|"

    #URL'S
    clientAvatarURL = client.user.avatar_url


    if userID != clientID:

        if nomeEmoji == emojiMessageTicket:
            if message_id == messageTicketID:
                #VARIAVEIS DE EMBEDS
                tituloEmbedTicketCriado = "FAÇA SEU PEDIDO"
                descricaoEmbedTicketCriado = "Digite '>pedido' para fazer um pedido!! \nCaso algum vendedor não estiver disponível, aguarde, assim que estiverem disponíveis, irão lhe atender!\n\n\n Caso tenha sido um erro, ou tennha terminado o atendimento, clique no '🔒'"
                embedTicketCriado = discord.Embed(title=tituloEmbedTicketCriado, color=255, description=descricaoEmbedTicketCriado)

                #DEFINIÇÃO NOME E NUMERAÇÃO CANAL
                numeracao: int = randint(0, 99999999)
                numeral.append(numeracao)
                numero: str = len(numeral) #numeração final
                nome: str = "{}-{}".format(nome_da_sala, numero) #nome final

                #CRIAÇÃO DO TICKET PRIVADO!
                overwritesTicketPrivado = {guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False), user: discord.PermissionOverwrite(read_messages=True, send_messages=True)}
                channelPrivado = await guild.create_text_channel(nome, overwrites=overwritesTicketPrivado)

                #TEMPORIZADOR PARA EXECUÇÃO DO RESTO DO CÓDIGO
                time.sleep(2)

                #ENVIO DE MENSAGENS E REAÇÕES TICKET CRIADO
                envioEmbedTicketCriado = await channelPrivado.send(embed=embedTicketCriado)
                await channelPrivado.send(mencaoReactMembro)
                await envioEmbedTicketCriado.add_reaction("🔒")

                ##REMOVER REAÇÃO
                message = await channel.fetch_message(message_id)
                await message.remove_reaction(nomeEmoji, user)

        if nomeEmoji == emojiMessageCloseTicket:
            #VARIAVEIS DO CODIGO
            new_name = "closed-{}".format(channel)

            #PERMISSÕES DO CANAL
            overwritesTicketFechado = {guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False), user: discord.PermissionOverwrite(read_messages=False, send_messages=False)}
            await channel.edit(overwrites=overwritesTicketFechado)

            # EDIÇÃO NOME DO CANAL
            await channel.edit(name=new_name)

            #ENVIO DE MENSAGEM NO TICKET(FECHADO)
            embedTicketClose = discord.Embed(title="**TICKET ENCERRADO**", color=255, description="Para deletar, basta digitar  '>delete'  ", )
            await channel.send(embed=embedTicketClose)

            ##REMOVER REAÇÃO
            message = await channel.fetch_message(message_id)
            await message.remove_reaction(nomeEmoji, user)

        if message_id == verificacaoMessageID:
            #VARIAVEIS DE EMBED
            tituloEmbedVerificacaoDM = "VERIFICADO COM SUCESSO!"
            corEmbedVerificacaoDM = 255
            descricaoEmbedVerificacaoDM = "Seja Bem Vindo!!!"
            textoFooterEmbedVerificacaoDM = "Developed By BOT'S STORE.py"
            thumbnailURLEmbedVerificacao = "https://media.tenor.com/images/219534dc6ca665b7fd0ba2ff94c6e2a0/tenor.gif"

            #EMBED VERIFICADO DM
            embedVerificadoDM = discord.Embed(title=tituloEmbedVerificacaoDM, color=corEmbedVerificacaoDM, description=descricaoEmbedVerificacaoDM)

            #SETTERS EMBED
            embedVerificadoDM.set_thumbnail(url=thumbnailURLEmbedVerificacao)
            embedVerificadoDM.set_footer(text=textoFooterEmbedVerificacaoDM, icon_url=clientAvatarURL)

            #CARGOS DE VERIFICACAO
            roleNaoVerificado = discord.utils.get(guild.roles, name=naoVerificadoRole)
            roleVerificado = discord.utils.get(guild.roles, name=verificadoRole)

            #SET DE CARGOS
            await user.remove_roles(roleNaoVerificado)
            await user.add_roles(roleVerificado)

            #ENVIO DE EMBED PARA USUARIO DM
            await user.send(embed=embedVerificadoDM)

            ##REMOVER REAÇÃO
            message = await channel.fetch_message(message_id)
            await message.remove_reaction(nomeEmoji, user)

        if channelID == pedidosChannelID:
            #CONTEUDO MESSAGE
            content = await channel.fetch_message(message_id)

            #tratamento do ID do pedido
            variavel = content.embeds[0].description
            findId_Regex: str = re.compile(r"<@[0-9]{18}>")
            _id = findId_Regex.search(str(variavel)).group()
            _id = _id.replace("<@", "")
            usuarioIdPedido: int = _id.replace(">", "")

            #USUARIO FINAL PEDIDO
            userPedido = await client.fetch_user(usuarioIdPedido)

            if emojiID == cancelamentoEmojiID:
                #PERGUNTA MOTIVO
                await channel.send("Qual o motivo do cancelamento?")
                motivo = await client.wait_for("message")
                conteudoMotivo = motivo.content

                #VARIAVEIS EMBED CLIENTE
                cancelamentoEmbedTituloDM = "PEDIDO CANCELADO!"
                corEmbedCancelamentoDM = 255
                descricaoEmbedCancelamentoDM = "Seu pedido foi cancelado!\n\nMotivo: {}\n\nPara mais informações, abra um Ticket em nosso Servidor!".format(conteudoMotivo)
                thumbnailURLEmbedCancelamentoDM = "https://dszw1qtcnsa5e.cloudfront.net/community/20201114/abf0d663-3fe5-4458-867c-762a379522e8/source.gif"

                #EMBED PARA O CLIENTE
                embedDM = discord.Embed(title=cancelamentoEmbedTituloDM, color=corEmbedCancelamentoDM, description=descricaoEmbedCancelamentoDM)

                #SETTERS EMBED CLIENTE
                embedDM.set_thumbnail(url=thumbnailURLEmbedCancelamentoDM)

                # CONTEUDO PARA SER ADICIONADO NA EDIÇÃO DO EMBED DA LOJA
                conteudoEmbedCru = variavel.replace("Deseja Aceitar o Pedido?", "")

                #VARIAVEIS EMBED EDITADO LOJA
                cancelamentoEmbedTitulo = "Pedido Cancelado"
                descricaoEmbedCancelamento = "{}\nStatus: Cancelado\n\nMotivo: {}\n\nCancelado por: {}".format(conteudoEmbedCru, conteudoMotivo, mencaoReactMembro)
                thumbnailURLEmbedCancelamento = "https://dszw1qtcnsa5e.cloudfront.net/community/20201114/abf0d663-3fe5-4458-867c-762a379522e8/source.gif"

                #EMBED EDITADO LOJA
                embedEditadoCancelamento = discord.Embed(title=cancelamentoEmbedTitulo, description=descricaoEmbedCancelamento)

                #SETTERS EMBED EDITADO LOJA
                embedEditadoCancelamento.set_thumbnail(url=thumbnailURLEmbedCancelamento)

                # LIMPEZA CANAL
                await channel.purge(limit=2)

                #EDIÇÃO EMBED LOJA
                await messageReaction.edit(embed=embedEditadoCancelamento)

                #LIMPEZA DE REAÇÃO EMBED LOJA
                await messageReaction.clear_reactions()

                #ENVIO DM CANCELAMENTO PEDIDO EMBED
                user = await client.fetch_user(usuarioIdPedido)
                await user.send(embed=embedDM)

            if emojiID == confirmacaoEmojiID:
                #PERGUNTA PRAZO
                await channel.send("Qual o prazo de Entrega?")
                prazo = await client.wait_for("message")
                contentPrazo = prazo.content

                # CONTEUDO PARA SER ADICIONADO NA EDIÇÃO DO EMBED DA LOJA
                conteudoEmbedCru = variavel.replace("Deseja Aceitar o Pedido?", "")

                #VARIAVEIS EMBED CLIENTE
                confirmacaoTituloDM = "PEDIDO CONFIRMADO COM SUCESSO!"
                corConfirmacaoDM = 255
                descricaoConfirmacaoDM = "Seu pedido foi confirmado!\n\n \n\nData de entrega: {}\n\nPara mais informações, abra um Ticket em nosso Servidor!".format(prazo.content)
                urlConfirmacaoDM = "https://media.baamboozle.com/uploads/images/153804/1612808854_856660"

                #EMBED CLIENTE DM CONFIRMACAO
                embedConfirmacaoDM = discord.Embed(title=confirmacaoTituloDM, color=corConfirmacaoDM, description=descricaoConfirmacaoDM)

                #SETTERS EMBED CLIENTE DM
                embedConfirmacaoDM.set_thumbnail(url=urlConfirmacaoDM)

                #VARIAVEIS EMBED EDITADO LOJA
                tituloEmbedConfirmacao = "PEDIDO CONFIRMADO COM SUCESSO!"
                descricaoEmbedConfirmacao = "{}\nStatus: Confirmado!\n\nPrazo: {}".format(conteudoEmbedCru, contentPrazo)
                corEmbedConfirmacao = 255
                footerEditadoConfirmacao = "Clique no emoji, caso queira dar como entregue o pedido!!!"
                iconUrlFooterEditadoConfirmacao = "https://img2.gratispng.com/20180501/tew/kisspng-airplane-paper-plane-emoji-computer-icons-paper-airplanes-5ae84dca1b96e9.537759831525173706113.jpg"
                thumbnailURLEmbedEditado = "https://media.baamboozle.com/uploads/images/153804/1612808854_856660"

                #EMBED EDITADO LOJA
                embedEditadoConfirmacao = discord.Embed(title=tituloEmbedConfirmacao, color=corEmbedConfirmacao, description=descricaoEmbedConfirmacao)

                #SETTERS EMBED EDITADO LOJA
                embedEditadoConfirmacao.set_thumbnail(url=thumbnailURLEmbedEditado)
                embedEditadoConfirmacao.set_footer(text=footerEditadoConfirmacao, icon_url=iconUrlFooterEditadoConfirmacao)

                #LIMPEZA CANAL
                await channel.purge(limit=2)

                #EDICAO EMBED LOJA
                await messageReaction.edit(embed=embedEditadoConfirmacao)

                #LIMPEZA E ADIÇÃO DE EMOJI
                await messageReaction.clear_reactions()
                await messageReaction.add_reaction("<:entrega:865794124904661012>")

                #ENVIO DE EMBED CLIENTE DM
                user = await client.fetch_user(usuarioIdPedido)
                await user.send(embed=embedConfirmacaoDM)

            if emojiID == entregaPedidoEmojiID:
                #PERGUNTA DESCRICAO ENTREGA PEDIDO
                await channel.send("Descrição da entrega:")
                descricaoEntrega = await client.wait_for("message")
                contentEntrega = descricaoEntrega.content

                # CONTEUDO PARA SER ADICIONADO NA EDIÇÃO DO EMBED DA LOJA
                conteudoEmbedCru = variavel.replace("Deseja Aceitar o Pedido?", "")
                conteudoEmbedCru = conteudoEmbedCru.replace("Status: Confirmado!", "")

                #VARIAVEIS EMBED CLIENTE DM
                tituloEmbedEntregaDM = "PEDIDO ENTREGUE!"
                corEmbedEntregaDM = 255
                descricaoEntregaDM = "Seu pedido foi Entregue!\n\n \n\nInformações da Entrega: {}\n\nPara mais informações, abra um Ticket em nosso Servidor!".format(contentEntrega)
                thumbnailURLEmbedEntregaDM = "https://i.pinimg.com/originals/81/e2/55/81e255e0ceeca98084787662c4f7814c.gif"

                #EMBED ENTREGA CLIENTE DM
                embedEntregaDM = discord.Embed(title=tituloEmbedEntregaDM, color=corEmbedEntregaDM, description=descricaoEntregaDM)

                #SETTERS ENTREGA CLIENTE DM
                embedEntregaDM.set_thumbnail(url=thumbnailURLEmbedEntregaDM)

                #VARIAVEIS ENTREGA LOJA
                tituloEmbedEntregaEditado = "PEDIDO ENTREGUE!"
                corEmbedEntregaEditado = 255
                descricaoEntregaEditado = "{}\nStatus: Entregue!\n\nInformações da Entrega: {}".format(conteudoEmbedCru, contentEntrega)
                thumbnailURLEmbedEntregaEditado = "https://i.pinimg.com/originals/81/e2/55/81e255e0ceeca98084787662c4f7814c.gif"

                #EMBED ENTREGA LOJA EDITADO
                embedEntregaEditado = discord.Embed(title=tituloEmbedEntregaEditado,color=corEmbedEntregaEditado ,description=descricaoEntregaEditado)

                #SETTERS ENTREGA LOJA EDITADO
                embedEntregaEditado.set_thumbnail(url=thumbnailURLEmbedEntregaEditado)

                #LIMPEZA CANAL
                await channel.purge(limit=2)

                #EDIÇÃO EMBED LOJA
                await messageReaction.edit(embed=embedEntregaEditado)

                #LIMPEZA REAÇÃO EMBED LOJA EDITADO
                await messageReaction.clear_reactions()

                #ENVIO ENTREGA CLIENTE DM
                await userPedido.send(embed=embedEntregaDM)

                #ROLE CLIENTE
                roleClienteNome = "CLIENTES |💲|"
                roleCliente = discord.utils.get(guild.roles, name=roleClienteNome)

                #ADIÇÃO DE CARGO CLIENTE
                await userPedido.add_roles(roleCliente)

client.run(token)


## python ./main.py
