import discord
import asyncio
import datetime
import pytz

from discord import channel
from discord import embeds
from discord import colour
from discord import reaction

#---------------------------------------------------------

everyone = True
client = discord.Client()
token = "ODA3NDk4NTg4OTMzNTg2OTU0.YB43qg.nBtkN00RKQ0sUoRjrlwCXZgK5gQ"

@client.event
async def on_ready():
    print("봇 구동 완료")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("봇 구동중"))

@client.event
async def on_message(message):
    if message.content == "=테스트": # 메세지 감지
        await message.channel.send ("{} | {}, Hello".format(message.author, message.author.mention))
        await message.author.send ("{} | {}, User, Hello".format(message.author, message.author.mention))
        
    if message.content == "=서버링크": # 메세지 감지
        await message.channel.send ("{} | {}, 님께 DM으로 서버링크 전송완료!".format(message.author, message.author.mention))
        await message.author.send ("{} | {}, 님께 서버링크가 도착했습니다!\nhttps://discord.gg/KSejN8M".format(message.author, message.author.mention))


    if message.content.startswith("?"):
        await message.channel.send("잊어..")
    
#---------------------------------------------------------

    if message.content.startswith ("=청소"):
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="📢ㅣ메시지 삭제 알림", description="`디스코드 채팅 {}개의 채팅이\nL>관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다`".format(amount, message.author), color=0x000000)
            embed.set_footer(text="문의 : 주릭#2989", icon_url="https://blogfiles.pstatic.net/MjAyMTA0MThfMTg5/MDAxNjE4NzE4MzY5MTk4.8cQaBA06gc58z6me8AvjBzHYe83lmT8i5c9O3xKnNU0g.4ReoV465HGpqPo-8hq66fJKRispldAV2NKrNCjoWtAsg.JPEG.jjoolung/9._700PX.jpg?type=w2")
            await message.channel.send(embed=embed)
        
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}, 님은 명령어를 사용할 수 있는 권한이 없습니다!".format(message.author.mention))

#---------------------------------------------------------

    if message.content.startswith("=투표"):
        i = (message.author.guild_permissions.administrator)

        vote = message.content[4:].split("/")
        await message.channel.send("`📊ㅣ투표` - " + vote[0])
        for i in range(1, len(vote)):
            choose = await message.channel.send("```" + vote[i] + "```")
            await choose.add_reaction('✔️')

#---------------------------------------------------------

    if message.content.startswith ("=공지"):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            channel = client.get_channel(738761142024929303) #채널아이디
            embed = discord.Embed(title="**📢ㅣ공지사항**", description="공지사항 내용은 항상 숙지 해주시기 바랍니다\n――――――――――――――――――――――――――――\n\n{}\n\n――――――――――――――――――――――――――――".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="문의 : 주릭#2989 | 담당 관리자 : {}".format(message.author), icon_url="https://blogfiles.pstatic.net/MjAyMTA0MThfMTg5/MDAxNjE4NzE4MzY5MTk4.8cQaBA06gc58z6me8AvjBzHYe83lmT8i5c9O3xKnNU0g.4ReoV465HGpqPo-8hq66fJKRispldAV2NKrNCjoWtAsg.JPEG.jjoolung/9._700PX.jpg?type=w2") #이미지 링크
            embed.set_thumbnail(url="https://blogfiles.pstatic.net/MjAyMTA0MTlfNzkg/MDAxNjE4ODEwNjI0MzI5.N4kftu6J5xopqkBmhkZ9SE39Ucr79dF20Ww9toWvnyAg.bS1V9H5Bq84j6RgqDmXEuy979ScCS172iDUCahbvAqUg.PNG.jjoolung/notice.png?type=w2") #이미지 링크
            await channel.send ("@everyone", embed=embed)
            await message.author.send("```――――――――――――――――――――――――――――\n[ BOT 자동 알림 ]\nL>정상적으로 공지가 채널에 작성이 완료되었습니다! \n\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}\n――――――――――――――――――――――――――――```".format(channel, message.author, notice))
 
        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))

#---------------------------------------------------------

    if message.content.startswith ("=규칙"):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            channel = client.get_channel(738776580821745694) #채널아이디
            embed = discord.Embed(title="**🔔ㅣ규칙사항**", description="규칙사항 내용은 항상 숙지 해주시기 바랍니다.\n규칙을 숙지하지 않고 발생하는 사건의\n모든 책임은 본인에게 있습니다.\n――――――――――――――――――――――――――――\n\n{}\n\n――――――――――――――――――――――――――――".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="문의 : 주릭#2989 | 담당 관리자 : {}".format(message.author), icon_url="https://blogfiles.pstatic.net/MjAyMTA0MThfMTg5/MDAxNjE4NzE4MzY5MTk4.8cQaBA06gc58z6me8AvjBzHYe83lmT8i5c9O3xKnNU0g.4ReoV465HGpqPo-8hq66fJKRispldAV2NKrNCjoWtAsg.JPEG.jjoolung/9._700PX.jpg?type=w2") #이미지 링크
            embed.set_thumbnail(url="https://blogfiles.pstatic.net/MjAyMTA0MThfMTI4/MDAxNjE4NzIxNjg0NjAw.ZwtxpxqOm3Iw03Sj0nNdKC9r58hFmrrnTL9vubZPp_Yg.gpYfQ8IZyFzP8qF41y0glnldDUnRnBdx3VJcsDlscdIg.PNG.jjoolung/%EA%B7%9C%EC%B9%99%EC%82%AC%ED%95%AD.png?type=w2") #이미지 링크
            await channel.send ("@everyone", embed=embed)
            await message.author.send("```――――――――――――――――――――――――――――\n[ BOT 자동 알림 ]\nL>정상적으로 공지가 채널에 작성이 완료되었습니다! \n\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}\n――――――――――――――――――――――――――――```".format(channel, message.author, notice))
 
        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))

#---------------------------------------------------------

    if message.content.startswith ("=가이드"):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            channel = client.get_channel(833608988494790706) #채널아이디
            embed = discord.Embed(title="**🔔ㅣ가이드**", description="서버에서 잘 활동하고 싶다면 필독!――――――――――――――――――――――――――――\n\n{}\n\n――――――――――――――――――――――――――――".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="문의 : 주릭#2989 | 담당 관리자 : {}".format(message.author), icon_url="https://blogfiles.pstatic.net/MjAyMTA0MThfMTg5/MDAxNjE4NzE4MzY5MTk4.8cQaBA06gc58z6me8AvjBzHYe83lmT8i5c9O3xKnNU0g.4ReoV465HGpqPo-8hq66fJKRispldAV2NKrNCjoWtAsg.JPEG.jjoolung/9._700PX.jpg?type=w2") #이미지 링크
            embed.set_thumbnail(url="https://blogfiles.pstatic.net/MjAyMTA0MTlfMTY3/MDAxNjE4ODE5NjUyMTY2.BLQ4aETRX9PbHF29noBKtuuH5GUHx0eZWpsqDnnzqTQg.mNO8BxhVYgLtx7ws1MY7ifm-MTQrVKUaGwkHpLEbvKwg.PNG.jjoolung/guide.png?type=w2") #이미지 링크
            await channel.send ("@everyone", embed=embed)
            await message.author.send("```――――――――――――――――――――――――――――\n[ BOT 자동 알림 ]\nL>정상적으로 공지가 채널에 작성이 완료되었습니다! \n\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}\n――――――――――――――――――――――――――――```".format(channel, message.author, notice))
 
        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))

#---------------------------------------------------------

    if message.content == "=호출": #특정입력
        ch = client.get_channel(833583634735693875) #채널아이디
        await ch.send ("{} | {}, 님이 호출을 하셨습니다.\n해결 가능한 관리팀 인원은 도움 부탁드립니다.\n@everyone".format(message.author, message.author.mention))



    if message.content == "=호출": # 메세지 감지
        embed = discord.Embed(title="🔔ㅣ호출안내", description="호출접수 현황",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)

        embed.add_field(name="접수 여부", value="관리팀 호출 접수가 완료되었습니다.", inline=False)
        embed.add_field(name="언제쯤 해결되나요?", value="확인되는대로 해결해드리겠습니다. ", inline=False)

        embed.add_field(name="호출 시스템을 이용해주셔서 감사합니다.", value="다음에도 무슨일이 있다면\n편하게 호출 부탁드립니다.", inline=True)

        embed.set_footer(text="문의 : 주릭#2989", icon_url="https://blogfiles.pstatic.net/MjAyMTA0MThfMTg5/MDAxNjE4NzE4MzY5MTk4.8cQaBA06gc58z6me8AvjBzHYe83lmT8i5c9O3xKnNU0g.4ReoV465HGpqPo-8hq66fJKRispldAV2NKrNCjoWtAsg.JPEG.jjoolung/9._700PX.jpg?type=w2") #하단 프로필
        embed.set_thumbnail(url="https://blogfiles.pstatic.net/MjAyMTA0MTlfMTU2/MDAxNjE4ODEwNjIzOTk4.fwXDP2l9r3LkwCPYmo4pHYr5Uw2ffMUUGGPSeU0vVzog.u1sLQYBEWh1XlK_BWiOjVoUMVmcj6A5Bv3qA0a_bKJMg.PNG.jjoolung/bell.png?type=w2") #썸네일
        await message.author.send (embed=embed)

#---------------------------------------------------------

    if message.content == "=명령어": # 메세지 감지
        embed = discord.Embed(title="서버 명령어 안내", description="        ",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)

        embed.add_field(name="=호출", value="관리자를 긴급호출합니다.", inline=False) 
        embed.add_field(name="=서버링크", value="서버의 초대코드를 제공합니다.", inline=True)
        embed.add_field(name="?", value="옛날 물음표 서버는 잊어줘요..", inline=True)

        embed.set_footer(text="문의 : 주릭#2989", icon_url="https://blogfiles.pstatic.net/MjAyMTA0MThfMTg5/MDAxNjE4NzE4MzY5MTk4.8cQaBA06gc58z6me8AvjBzHYe83lmT8i5c9O3xKnNU0g.4ReoV465HGpqPo-8hq66fJKRispldAV2NKrNCjoWtAsg.JPEG.jjoolung/9._700PX.jpg?type=w2")
        embed.set_thumbnail(url="https://blogfiles.pstatic.net/MjAyMTA0MTlfNiAg/MDAxNjE4ODE1NzQwNTQ4.KwrbfcBbp2FyBTyw3YHz6knJJDAtaGIPPGjrPEnlMfkg.Y3--9xPx_Ng5fEjUIc8SRrMmv613u5tnjQRlU4bvKakg.PNG.jjoolung/admin.png?type=w2")
        await message.channel.send (embed=embed)

#---------------------------------------------------------

client.run(token)