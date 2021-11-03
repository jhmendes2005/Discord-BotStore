import discord
import json
import time
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import has_permissions, MissingPermissions

from modules import client as configClient, message as EmbedMessage

command_Prefix = str
client = configClient.client
EmbedMessage = EmbedMessage.message

texto = []
bot = Bot("!")

with open("./config.exemplo.json") as f:
    config = json.load(f)
    command_Prefix = config['prefixCommand']


class command:

    @bot.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def colocar_regras(message):
        await message.channel.purge(limit=1)
        embed = discord.Embed(title="Regras ( Leia com atenção ):",
                              description="1-Proibido Conteúdo pornográfico.\n\n 2-Proibido Discriminação, homofobia, racismo, xenofobia, etc...\n\n3-Proibido Plágio/cópia de qualquer conteúdo do nosso servidor.\n\n4-Proibido flood, Spam ou textos indesejados.\n\n5-Proibido Marcação excessiva de cargos do servidor.\n\n6-Proibido Explanação de informações e fotos de membros.\n\n7-Proibido Divulgação, seja dentro ou fora do servidor.\n\n\n\n**POLITICAS DA LOJA:**\n\n1- Nosso prazo de confirmação de pagamento, é de até 24H úteis.\n\n2- Fazemos serviços mediante a um pagamento confirmado.\n\n3- Oferecemos garantia ao cliente em até 24H após a entrega do serviço.\n\n4- Manutenções somente com agendamentos pagos, ou emergenciais.(podendo ser cobrado de acordo com a disponibilidade da equipe)\n\n5- Cobrimos 100% manutenções em Host, ou crashes que não sejam relacionados a mal uso do cliente.\n\n6- Implementação de novas funcionalidades, serão cobradas.\n\n7- Nós temos a responsabilidade em cumprir o compromisso com o cliente, independente do plano escolhido. Ou seja, cumpriremos 100% do plano, ou seu dinheiro de volta. (Caso tenha passado 50% dos dias de ativação do plano, nós iremos reembolsar proporcionalmente o valor que seria restante do plano.\n\n8- Nós não reembolsamos em HIPÓTESE ALGUMA, planos de host, pois a hospedagem, é feita através de outra empresa. (Caso haja algum problema na ativação da host, ou alguma falha que seja passível a reembolso, nossa loja irá reembolsar os clientes)\n\n9- Nossos serviços tem um prazo de entrega, definida na hora da compra. Sendo até 7 dias ÚTEIS (caso seja um trabalho muito grande)\n\n10- Após o fim dos planos assinados, caso não haja renovação, os serviços são cancelados automaticamente, e ficam inativos até a renovação do mesmo.\n\n11- Nós nunca iremos pedir logins e senhas aos clientes!\n\n12- Todos os dados que tenham contato conosco, são 100% SIGILOSOS, não são vendidos/dados a ninguém.\n\n13- Somente o FOUNDER pode receber os pagamentos dos clientes. Outras pessoas que pedirem pagamentos relacionados a qualquer que seja nossos serviços, favor se recusar a pagar!\n\n(@here)\n",
                              color=discord.Color.from_rgb(255, 0, 255))
        channel = message.channel
        embed.set_footer(text="BOT'S STORE.py ©", icon_url=client.user.avatar_url)
        await channel.send(embed=embed)

    @bot.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def colocar_preco(message):
        await message.channel.purge(limit=+1)
        embed = discord.Embed(
            title="PACOTES BOT´s STORE",
            color=255,
            description="\nㅤ\nㅤ\n**BOT COMUNIDADE**\n\n- Mensagem de Boas Vindas, e saídas 100% Personalizáveis.\n\n- Cargos Por Reações.\n\n- Comandos para colocar Embeds Personalizados (Regras, Avisos e etc.)\n\n- Comandos de Limpeza de Chat.\n\n- Comandos de Trava e destrava de canais (Lock e Unlock).\n\n- Comandos de Ban e Kick.\n\n- Comandos de deletar Canais.\n\n- Auto Role.\n\nPlano excelente para Comunidades de Discord, que queiram dar uma cara nova em seu servidor, tendo um BOT próprio, para chamar atenção dos outros servidores convêncionais!\n\n**PREÇO =** R$50/Mês (Host 100% Grátis) \n\n\n\n\n**BOT LOJAS**\n\n- Mensagem de Boas Vindas, e saídas 100% Personalizáveis.\n\n- Cargos Por Reações.\n\n- Comandos para colocar Embeds Personalizados (Regras, Avisos e etc.)\n\n- Comandos de Limpeza de Chat.\n\n- Comandos de Trava e destrava de canais (Lock e Unlock).\n\n- Comandos de Ban e Kick.\n\n- Comandos de deletar Canais.\n\n- Auto Role.\n\n- Sistema de tickets.\n\n- Sistema de assitente de vendas.\n\n\nExcelente opção para quem tem uma loja virtual no Discord! Nossos sistemas de Ticket e Assistente de vendas, ajudam a pegar os pedidos, sem muita enrolação com os clientes! Além dele possuir tudo oque se precisa para uma comunidade!!!\n\n**PREÇO =** R$70/Mês (Host 100% Grátis) \n"
        )

        embed.set_thumbnail(url="https://eventos.villadolago.com.br/media/magentothem/default/ajaxloader.gif")
        await message.channel.send(embed=embed)


    @command.has_permission(your specified permission)
    async def clear(message, amount=int(1)):
        content: str = message.content.lower()
        content = content.replace(command_Prefix, "")

        try:
            if(int(content.split()[1]) > 1):
                amount = int(content.split()[1])
            await message.channel.purge(limit=amount + 1)
        except:
            await message.channel.send("ocorreu um erro, e serão limpadas as 4 ultimas mensagens")
            time.sleep(2)
            await message.channel.purge(limit=4)
            return

        await message.channel.send(f"O {message.author.mention} pediu para mim limpar {amount} mensagens, e eu limpei!! 😁😁\n\n ```mensagem auto-deletada em 1 segundo```")
        time.sleep(1)
        await message.channel.purge(limit=1)

    async def ping(message):
        tittle = f"@{message.author.mention} olhe isso :3"
        extra = f"Estou com {round(client.latency * 1000)}ms"
        embed = EmbedMessage(tittle=tittle, extra=extra)

        msg = await message.channel.send(embed=embed)
        await msg.add_reaction("🔌")

    @bot.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def kick(message):
        await message.channel.purge(limit=1)
        content: str = message.content.lower()
        print(content)
        content = content.replace(command_Prefix, "")
        content = content.replace("<", "")
        content = content.replace("@", "")
        content = content.replace("!", "")
        content = content.replace(">", "")
        content = content.replace("kick", "")
        content = content.replace(" ", "")
        content = int(content)
        canal = client.get_channel(id=854187604399357952)
        user = discord.utils.get(message.guild.members, id=content)
        msg = "O {} Foi expulso!!".format(user)
        await user.kick()
        await canal.send(msg)

    @bot.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def ban(message):
        await message.channel.purge(limit=1)
        content: str = message.content.lower()
        content = content.replace(command_Prefix, "")
        content = content.replace("<", "")
        content = content.replace("@", "")
        content = content.replace("!", "")
        content = content.replace(">", "")
        content = content.replace("kick", "")
        content = content.replace(" ", "")
        content = int(content)
        canal = client.get_channel(id=854187604399357952)
        user = discord.utils.get(message.guild.members, id=content)
        msg = "O {} Foi banido!!".format(user)
        await user.ban()
        await canal.send(msg)

    @bot.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def delete(message):
        existing_channel = discord.utils.get(message.guild.channels, id=message.channel.id)
        if existing_channel == discord.utils.get(message.guild.channels, id=message.channel.id):
            await existing_channel.delete()

    @bot.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def colocar_ticket(message):
        await message.channel.purge(limit=1)

        embed = discord.Embed(title="ABRIR TICKET DE COMPRAS!",
                              description="CLIQUE NO EMOJI A BAIXO PARA REALIZAR UM PEDIDO!\n\nApós isso, será aberto um canal de mensagens totalmente privado!!")

        embed.set_thumbnail(url="https://www.atelieguglielmoniloja.com.br/res/site/img/png-transparent-shopping-cart-computer-icons-e-commerce-buy-angle-text-logo.gif")
        embed.set_footer(text="Developed By BOT'S STORE.py", icon_url=client.user.avatar_url)
        msg = await message.channel.send(embed=embed)
        await msg.add_reaction("📩")

    @bot.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def colocar_verificacao(message):
        await message.channel.purge(limit=1)

        embed = discord.Embed(title="REALIZAR VERIFICAÇÃO!",
                              description="CLIQUE NO EMOJI A BAIXO PARA REALIZAR A VERIFICAÇÃO!\n\nFazemos isso, para termos controle total do servidor!!")

        embed.set_thumbnail(url="https://media.tenor.com/images/219534dc6ca665b7fd0ba2ff94c6e2a0/tenor.gif")
        embed.set_footer(text="Developed By BOT'S STORE.py", icon_url=client.user.avatar_url)
        msg = await message.channel.send(embed=embed)
        await msg.add_reaction("✅")

    async def pedido(message):
        await message.channel.purge(limit=1)
        canal = client.get_channel(id=864683201045463040)

        await message.channel.send("```Qual seria seu pedido? (Descreva oque deseja no BOT)``` {}".format(message.author.mention))

        pedido = await client.wait_for("message")

        await message.channel.purge(limit=2)

        embed = discord.Embed(
        title="NOVO PEDIDO!!!!",
        color=255,
        description=" Pedido: {}\n\nPedido Feito por: {}\n\n\nDeseja Aceitar o Pedido?".format(pedido.content, message.author.mention, message.author.id),
        )
        embed.set_thumbnail(url="https://c.tenor.com/4k_GRJkuNMQAAAAi/open-mouth-exclamation-question-mark.gif")

        msg = await canal.send(embed=embed)
        await msg.add_reaction("<:X_:865722854603096064>")
        await msg.add_reaction("<:ACCEPT:865722659484205118>")

        embed2 = EmbedMessage(tittle="PEDIDO FEITO COM SUCESSO!!", extra="Aguarde algum ADM ler e entrar em contato sobre seu pedido. (RESPONDEMOS EM NO MÁXIMO 24H!)\n\n\nO Atendimento vem pelo mesmo ticket, não precisa fechar!")

        embed3 = discord.Embed(
            title="SEU PEDIDO FOI FEITO COM SUCESSO!!",
            color=255,
            description=" Pedido: {}\nPedido Feito por: {}\n\n(RESPONDEMOS EM NO MÁXIMO 24H!)".format(pedido.content, message.author.mention),
        )
        embed3.set_thumbnail(url="https://c.tenor.com/4k_GRJkuNMQAAAAi/open-mouth-exclamation-question-mark.gif")

        await message.author.send(embed=embed3)
        await message.channel.send(embed=embed2)

    async def teste(message):
        print(bot.commands)

    @bot.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def avisos(message):
        content: str = message.content.lower()
        content = content.replace(command_Prefix, "")
        content = content.replace("<", "")
        content = content.replace("@", "")
        content = content.replace("!", "")
        content = content.replace(">", "")
        content = content.replace("aviso", "")
        content = content.replace(" ", "")

        canal = client.get_channel(id=864657193135374336)
        embed = discord.Embed(
            title="AVISO",
            color=255,
            description=content,
        )

        await canal.send(embed=embed)
        await canal.send("@everyone @here")

    @bot.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def lock(message):
        await message.channel.purge(limit=1)
        await message.channel.set_permissions(message.guild.default_role, send_messages=False)
        time.sleep(2)

        await message.channel.send("Canal travado!!")
        await message.channel.purge(limit=1)

    @bot.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def unlock(message):
        await message.channel.purge(limit=1)
        await message.channel.set_permissions(message.guild.default_role, send_messages=True)
        time.sleep(2)

        await message.channel.send("Canal destravado!!")
        await message.channel.purge(limit=1)

    @client.event
    async def on_command_error(ctx, error):
        await ctx.message.delete()
        if isinstance(error, commands.CommandInvokeError):
            print("Command used in invalid channel")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(error, delete_after=30)
            return
        raise error