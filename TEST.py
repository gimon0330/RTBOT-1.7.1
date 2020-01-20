import discord, asyncio, re, datetime, openpyxl, time, random, urllib, urllib.request , bs4, os, sys, json, configparser
from discord import Member
from discord.ext import commands
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from selenium import webdriver
#import함수

client = discord.Client()

setbancha = 0

# =====================봇이 구동되었을 때 보여지는 코드

@client.event
async def bg_change_playing():
    while True:
        members_sum = 0
        for s in client.guilds:
            members_sum += len(s.members)
        presences_list = ["드립 공부", "알티봇 V2.7.1", "'봇 도움말'로 봇명령어 알아보기", str(len(client.guilds)) + "개의 서버 다니는중", str(members_sum) + "명의 유저들과 함깨"]
        for v in presences_list:
            await asyncio.sleep(9)
            await client.change_presence(activity=discord.Game(v))
    client.loop.create_task(bg_change_playing())

@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")
    client.loop.create_task(bg_change_playing())

# =====================새로 사람이 들어왔을때=====================

@client.event
async def on_member_join(member):
    i=0
    blacklistmem=[580231520816463873,504068405867970560,]
    blackmemcount=2
    for i in range(0,blackmemcount) :
        if blacklistmem[i] == member.id:
            embed = discord.Embed(
                title="블랙리스트 등재 유저 발견(밴)",
                description="자세한 사항에 관해서는 https://discord.gg/정발시공개  를 참조 해주시면 감사하겠습니다",
                color=0xFF0000
            )
            channel = client.get_channel(setbancha)
            await channel.send(embed=embed)
            await member.guild.ban(member,reason="블랙리스트 등재", delete_message_days=1)
            break

# =====================메세지를 읽었을떄=====================

@client.event
async def on_message(message):

    if message.author.bot:
        return None
        
    #######################################함수 시작#####################################

    if message.content == '친밀도 초기화':
        if message.author.id == 467666650183761920 :
            file = openpyxl.load_workbook("친밀도.xlsx")
            sheet = file.active
            for i in range(1, 211):
                sheet["A"+str(i)].value = "0"
            await message.channel.send("친밀도 리스트 초기화 완료")
            file.save("친밀도.xlsx")
        else :
            await message.channel.send('어허.. 이 명령어는 트펙만 쓸수 있는 명령어다!')
        
    #####################################################################################

    if message.content == '서버 정보' :
        embed=discord.Embed(title=message.guild.name, color=0x00fffff)
        embed.set_thumbnail(url=message.guild.icon_url)
        embed.add_field(name="서버 생성 일시", value=message.guild.created_at, inline=True)
        embed.add_field(name="서버 주인", value=message.guild.owner.name, inline=True)
        embed.add_field(name="상세 정보", value="인원수 : " + str(len(message.guild.members)) + "명\n" + "역할수 : " +str(len(message.guild.roles)) + "개\n 이모티콘 수 : " + str(len(message.guild.emojis)) + "개", inline=True)
        await message.channel.send(embed=embed)
        
    #####################################################################################

    if message.content == "봇 명령어":
        embed = discord.Embed(
            title = '옛다 명령어다',
            description = '현재 숨겨진 명령어 : 17개 (발견되면 리스트에 추가)',
            colour = 0x00FFFF
        )
        embed.add_field(name='안녕하살법', value = '안녕하살법 해쥼',inline = False)
        embed.add_field(name='배그각재줘', value='오늘 배그각 알려줌', inline=False)
        embed.add_field(name='기억해 [단어]', value='!기억해 [입력] [출력] 형식으로 적으면 학습함', inline=False)
        embed.add_field(name='말해 [단어]', value='!말해 [기억해에서 적은 입력] 형식으로 적으면 학습한내용 말함', inline=False)
        embed.add_field(name='!기억초기화', value='학습한 데이터 초기화함', inline=False)
        embed.add_field(name='기억목록', value='학습한 데이터목록 알려줌', inline=False)
        embed.add_field(name='요즘 학교 개같아', value='..?', inline=False)
        embed.add_field(name='학교 안다녀', value='어..그래', inline=False)
        embed.add_field(name='[단어] 이대로 가면', value='티어 왜살아', inline=False)
        embed.add_field(name='..야 [단어]', value='금기의 명령어야', inline=False)
        embed.add_field(name='ㄴㄷㅆ', value='뭔가 숨어있을지도..?', inline=False)
        embed.add_field(name='내꺼 [단어]', value='이건 이제 내꼬얌 >ㅅ<', inline=False)
        embed.add_field(name='으 씹덕', value='웩..   ..?근데 코드가 한줄이 아닌데?', inline=False)
        embed.add_field(name='time', value='시간 알랴쥼', inline=False)
        embed.add_field(name='헤모글로빈 분자식', value='C3032H4816O872N780S8Fe4', inline=False)
        embed.add_field(name='국밥 [단어]', value='그걸 왜 먹냐? 차라리 뜨끈한 국밥 든든하게 먹겠다', inline=False)
        embed.add_field(name='문법나치', value='외 네 맞춤뻡이 머가 어떼서', inline=False)
        embed.add_field(name='명령어 추가 신청 [입력] [출력]', value='생각해보고 트펙이 넣어줄거임 ㅇㅇ', inline=False)
        embed.add_field(name='신청 엑셀 초기화', value='신청해둔거 싹다 지움', inline=False)
        embed.add_field(name='그치만 [단어]', value='그치만.. 나는 이딴 드립 치려는 너가 싫은걸??', inline=False)
        embed.add_field(name='가프리무너', value='아아악!! 내눈!!!', inline=False)
        embed.add_field(name='time', value='시간!', inline=False)
        embed.add_field(name='초대장', value='봇 초대장이다 흐헤헤헿', inline=False)
        embed.add_field(name='!영화순위', value='영화를 1~20순위로 나눈 영화순위 정보를 제공합니다.', inline=False)
        embed.add_field(name='!서버 정보', value='서버의 정보를 보여줄 예정임', inline=False)
        embed.add_field(name='와! [단어]', value='네.. 그것 참 어렵죠..', inline=False)
        embed.add_field(name='!경고 관련', value='응 트펙만 쓸수 있는거임 ㅅㄱ(관리자도 못씀ㅋ)', inline=False)

        await message.channel.send(embed=embed)
        
    #####################################################################################


    if message.content.startswith('밴 채널 설정'):
        setbancha = message.channel.id
        await message.channel.send(str(setbancha)+ "로 설정 완료")

    if message.content == '밴 채널 조회':
        await message.channel.send("현재 밴채널으 아이디는: "+str(setbancha)+" 입니다")

    if message.content == '있었는데요':
        await message.channel.send("없었습니다")
        
    #####################################################################################

    if message.content == '안녕하살법':
        await message.channel.send("안녕하살법 받아치기!")

    if message.content == '곤니찌사뽀':
        await message.channel.send("곤니찌삿뽀 가에시!!")

    if message.content == '안녕하살법 받아치기':
        await message.channel.send("안녕하살법 받아치기 받아치기!!!")
        
    #####################################################################################

    if message.content.startswith('요즘 학교 개같아'):
        await message.channel.send("학교 어디다녀?")

    if message.content.startswith('학교 안다녀'):
        await message.channel.send("아.. 답변 고마워..")
        
    #####################################################################################

    if message.content[len(message.content)-6:len(message.content)] == '이대로 가면':
        await message.channel.send('라이더')
        
    #####################################################################################

    if message.content.startswith('..야'):
        await message.channel.send(message.author.name+' : "야 '+message.content[4:]+'"')
        await message.channel.send(message.content[4:]+' : (...)')
        await message.channel.send(message.author.name+' : "...소난다(그런가)"')
        await message.channel.send(message.author.name+' : "넣을게."')
        await message.channel.send("||아 쑤1바 이건좀;||")
        await message.channel.send(message.content[4:]+' : (...!!!)')
        await message.channel.send(message.author.name+' : "화낸척하기는...사실 너 이게 좋은거잖아"')
        await message.channel.send(message.content[4:]+' : (...)')
        await message.channel.send("이후... 안해 때려쳐 ")


    if message.content.startswith('역사 모드'):
        await message.channel.send("아 제발 뒤진다")
        
    #####################################################################################

    if message.content.startswith('배그각 재줘'):
        random = int(now.microsecond) % 2
        if random==1:
            await message.channel.send(embed=discord.Embed(title="배그각입니다.", color=0x00FFFF))
        else:
            await message.channel.send(embed=discord.Embed(title="자러갑시다...", color=0xFF0000))
        
    #####################################################################################

    if message.content == ('와가나와'):
        await message.channel.send("와가나와 "+message.author.id+"\n홍마족 제일의 마법사이자\n폭렬 마법을 다루는 자!")

    if message.content == ('바크레츠바크레츠'):
        await message.channel.send("랄~랄~라~!")

    if message.content == 'ㄴㄷㅆ' :
        await message.channel.send("네 다음 씹덕~^^")
        
    #####################################################################################

    if message.content.startswith('띵킹'):
        await message.channel.send("""
        ⠀⠀⠀      ⢀⣀⣀⣀
⠀⠀ ⠰⡿⠿⠛⠛⠻⠿⣷
⠀⠀⠀⠀⠀⠀⣀⣄⡀⠀⠀⠀⠀⢀⣀⣀⣤⣄⣀⡀
⠀⠀⠀⠀⠀⢸⣿⣿⣷⠀⠀⠀⠀⠛⠛⣿⣿⣿⡛⠿⠷
⠀⠀⠀⠀⠀⠘⠿⠿⠋⠀⠀⠀⠀⠀⠀⣿⣿⣿⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁

⠀⠀⠀⠀⣿⣷⣄⠀⢶⣶⣷⣶⣶⣤⣀
⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠈⠙⠻⠗
⠀⠀⠀⣰⣿⣿⣿⠀⠀⠀⠀⢀⣀⣠⣤⣴⣶⡄
⠀⣠⣾⣿⣿⣿⣥⣶⣶⣿⣿⣿⣿⣿⠿⠿⠛⠃
⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁
⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁
⠀⠀⠛⢿⣿⣿⣿⣿⣿⣿⡿⠟
⠀⠀⠀⠀⠀⠉⠉⠉""")

    if message.content.startswith('내꺼 '):
        await message.channel.send("이제"+message.content[2:]+" (은)는 제겁니다\n"+message.content[3:]+" 는 제 맘대로 할 수 있는 겁니다.")
        
    #####################################################################################

    if message.content == '으 씹덕':
        if message.content[5:] == '티어' :
            await message.channel.send("아 그건 진짜 좀 아니다 겁나 더럽네;;")
        else :
            await message.channel.send("그게 뭔데 10덕아")
        
    #####################################################################################

    if message.content.startswith('time'):
        embed = discord.Embed(title="현재 시간은?", description= str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일 | " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second), color=0x00ff00)
        await message.channel.send(embed=embed)
        
    #####################################################################################

    if message.content.startswith('헤모글로빈 분자식'):
        embed = discord.Embed(title="헤모글로빈 분자식", description="C3032H4816O872N780S8Fe4" , color=0x00ff00)
        await message.channel.send(embed=embed)
        he+=1
        if he==10 :
            await message.channel.send('제발.. 그만...')
            he=0
        
    #####################################################################################

    if message.content.startswith('국밥'):
        if message.content.startswith('국밥 트펙') :
            await message.channel.send("무너 더러워")
        else :
            await message.channel.send(message.content[3:]+"을 왜먹냐 그걸 먹을바에야 차라리 뜨끈한 국밥 든든하게 먹겠다.")
        
    #####################################################################################

    if message.content.startswith('문법나치') :
        await message.channel.send(message.content[5:]+"아 그거 왜 하꼬 사냐 문뻡 파께할껴야 문법 나치 드러운 Shake들")
        
    #####################################################################################

    if message.content.startswith('!영화순위'):
        # http://ticket2.movie.daum.net/movie/movieranklist.aspx 크롤링한 사이트
        i1 = 0 # 랭킹 string값
        embed = discord.Embed(
            title = "영화순위",
            description = "영화순위입니다.",
            colour= discord.Color.red()
        )
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'http://ticket2.movie.daum.net/movie/movieranklist.aspx'
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        moviechartBase = bsObj.find('div', {'class': 'main_detail'})
        moviechart1 = moviechartBase.find('ul', {'class': 'list_boxthumb'})
        moviechart2 = moviechart1.find_all('li')

        for i in range(0, 20):
            i1 = i1+1
            stri1 = str(i1) # i1은 영화랭킹을 나타내는데 사용됩니다

            moviechartLi1 = moviechart2[i]  # i번째 LI ------------------------- ?등랭킹 영화---------------------------
            moviechartLi1Div = moviechartLi1.find('div', {'class': 'desc_boxthumb'})  # 영화박스 나타내는 Div
            moviechartLi1MovieName1 = moviechartLi1Div.find('strong', {'class': 'tit_join'})
            moviechartLi1MovieName = moviechartLi1MovieName1.text.strip()  # 영화 제목

            moviechartLi1Ratting1 = moviechartLi1Div.find('div', {'class': 'raking_grade'})
            moviechartLi1Ratting2 = moviechartLi1Ratting1.find('em', {'class': 'emph_grade'})
            moviechartLi1Ratting = moviechartLi1Ratting2.text.strip()  # 영화 평점

            moviechartLi1openDay1 = moviechartLi1Div.find('dl', {'class': 'list_state'})
            moviechartLi1openDay2 = moviechartLi1openDay1.find_all('dd')  # 개봉날짜, 예매율 두개포함한 dd임
            moviechartLi1openDay3 = moviechartLi1openDay2[0]
            moviechartLi1Yerating1 = moviechartLi1openDay2[1]
            moviechartLi1openDay = moviechartLi1openDay3.text.strip()  # 개봉날짜
            moviechartLi1Yerating = moviechartLi1Yerating1.text.strip()  # 예매율 ,랭킹변동
            # ------------------------- ?등랭킹 영화---------------------------
            embed.add_field(name='---------------랭킹'+stri1+'위---------------',
                            value='\n영화제목 : '+moviechartLi1MovieName+'\n영화평점 : '+moviechartLi1Ratting+'점'+'\n개봉날짜 : '+moviechartLi1openDay+'\n예매율,랭킹변동 : '+moviechartLi1Yerating,
                            inline=False
                            ) # 영화랭킹
        await message.channel.send(embed=embed)

    #####################################################################################

    if message.content == '!프로필':
        user=message.author
        if user.display_name == user.name:
            embed = discord.Embed(title=user.name + " 님의 프로필", color=0x00ff00)
        else:
            embed = discord.Embed(title=user.name + " 님의 프로필",description="닉네임 : (" + user.name + ")", color=0x00ff00)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="유저 ID", value=str(user.id), inline=False)
        st = str(user.status)
        if st == "online":
            sta = "온라인"
        elif st == "offline":
            sta = "오프라인"
        elif st == "idle":
            sta = "자리 비움"
        elif st == "dnd" or st == "do_not_disturb":
            sta = "방해 금지"
        embed.add_field(name="현재 상태", value=sta, inline=True)
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000)/1000)
        embed.add_field(name="Discord 가입 일시", value=str(date.year) + "년 " + str(date.month) + "월 " + str(date.day) + "일 ", inline=True)
        joat = user.joined_at.isoformat()
        embed.add_field(name="서버 가입 일시", value=joat, inline=True)
        if user.guild_permissions.administrator:
            embed.add_field(name="서버 권한", value="ADMINISTRATOR (관리자)", inline=True)
        else:
            embed.add_field(name="서버 권한", value="USER (유저)", inline=True)
        
        await message.channel.send(embed=embed)
        

    #####################################################################################

    if message.content == '프사 내놔':
        embed = discord.Embed(title=message.author.name+" 님의 프로필사진", description= '', color=0x00ff00)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    #####################################################################################

    if message.content.startswith("명령어 추가 신청"):
        file = openpyxl.load_workbook('추가신청.xlsx')
        sheet = file.active
        slashwhere = 0
        for i in range(10,201) :
            if message.content[i] == '/' :
                slashwhere = i
                break
        learn1=message.content[10:slashwhere]
        learn2=message.content[slashwhere+1:]
        for i in range(1, 201):
            if sheet["A"+str(i)].value == "-":
                sheet["A" + str(i)].value = learn1
                sheet["B" + str(i)].value = learn2
                embed = discord.Embed(
                    title="명령어 추가 신청",
                    description='`'+learn1+'`'+"을 유저가 보냈을경우,"+'`'+learn2+'`'+"을 봇이 말한다\n"+"신청 되었습니다 관리자의 승인을 기다려 주세용"
                )
                await message.channel.send(embed=embed)
                break
        file.save("추가신청.xlsx")

    if message.content.startswith("신청 엑셀 초기화"):
        if message.author.id == 467666650183761920 :
            file = openpyxl.load_workbook("추가신청.xlsx")
            sheet = file.active
            for i in range(1, 211):
                sheet["A"+str(i)].value = "-"
            await message.channel.send("신청 리스트 초기화 완료")
            file.save("추가신청.xlsx")
        else :
            await message.channel.send('어허.. 이 명령어는 트펙만 쓸수 있는 명령어다!')

        #완성
    #####################################################################################

    if message.content.startswith("기억해"):
        file = openpyxl.load_workbook('기억.xlsx')
        sheet = file.active
        slashwhere = 0
        for i in range(4,201) :
            if message.content[i] == '/' :
                slashwhere = i
                break

        learn1=message.content[4:slashwhere]
        learn2=message.content[slashwhere+1:]

        for i in range(1, 201):
            if sheet["A"+str(i)].value == "-":
                sheet["A" + str(i)].value = learn1
                sheet["B" + str(i)].value = learn2
                sheet["C" + str(i)].value = message.author.name
                embed = discord.Embed(
                    title="기억 완료!",
                    description='`'+learn1+'`'+"을 유저가 보냈을경우,"+'`'+learn2+'`'+"을 봇이 말한다\n"
                )
                embed.add_field(name='남은 용량',value=str(i)+'/200')
                await message.channel.send(embed=embed)
                break
        file.save("기억.xlsx")

    if message.content.startswith("말해"):
        file = openpyxl.load_workbook("기억.xlsx")
        sheet = file.active
        slashwhere = 0
        commandyes=False

        for i in range(1, 201):
            if sheet["A" + str(i)].value == message.content[3:]:
                await message.channel.send(sheet["B" + str(i)].value)
                commandyes=True
                break
        
        if commandyes == False :
            embed = discord.Embed(
                    title="명령어 없어",
                    description="명령어가 발견되지 않았습니다",
                    color=0xFF0000
                )

    if message.content.startswith("!기억 초기화") or message.content.startswith("!기억초기화"):
        if message.author.id == 467666650183761920 :
            file = openpyxl.load_workbook("기억.xlsx")
            sheet = file.active
            for i in range(1, 201):
                sheet["A"+str(i)].value = "-"
            await message.channel.send("기억초기화 완료")
            file.save("기억.xlsx")
        else :
            await message.channel.send('어허.. 이 명령어는 트펙만 쓸수 있는 명령어다!')
        

    if message.content.startswith("기억목록") or message.content.startswith("기억 목록"):
        file = openpyxl.load_workbook("기억.xlsx")
        sheet = file.active
        embed = discord.Embed(
                    title="명령어 목록",
                    description="옛다 명령어다",
                    color=0x00FFFF
                )
        for i in range(1, 201):
            if sheet["A" + str(i)].value == "-" and i == 1:
                embed = discord.Embed(
                    title="명령어 목록",
                    description="명령어가 발견되지 않았습니다",
                    color=0xFF0000
                )
                break
            if sheet["A" + str(i)].value != "-":
                embed.add_field(name="입력 : "+sheet["A" + str(i)].value, value= " 출력 : "+ sheet["B" + str(i)].value, inline=False)
            else:
                break
        await message.channel.send(embed=embed)

    #####################################################################################

    if message.content.startswith('그치만') :
        await message.channel.send("그치만.. "+message.content[4:]+" 짱.. 이렇게라도 하지 않으면 "+message.content[4:]+" 짱 내게 관심도 없는걸..?")
        await message.channel.send("손나 바카나!! 그럴리가 없잖아! 넌 하나뿐인 내 "+str(message.author.name)+" 이라구... 그리고... 꽤나 재밌고말이지...")
        
    #####################################################################################

    if message.content == '가프리무너' :
        await message.channel.send('가프리 ♥ 무너')
        
    #####################################################################################

    if message.content.startswith("#한강"):
        output = hangang_main()
        await message.channel.send(embed=output)
        
    #####################################################################################

    if message.content == '무너 호출!' :
        await message.channel.send("<@605289666073329674>")
        
    #####################################################################################

    if message.content == '나무위키' :
        await message.channel.send("으 꺼무위키")
        
    #####################################################################################

    if message.content == '초대장' :
        await message.channel.send("https://discordapp.com/api/oauth2/authorize?client_id=661477460390707201&permissions=8&scope=bot")
        
    #####################################################################################

    if message.content == '무너 상태' or message.content == '무너상태' :
        now = datetime.datetime.now() 
        random = int(now.microsecond) % 3
        if random == 0 :
            embed = discord.Embed(title="오늘의 무너 상태 : 미인은 아니지만 돼지도 아닌 무언가", description= str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일 | " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second) + '일자 상태입니다', color=0x00ff00)
            await message.channel.send(embed=embed)
        if random == 1 :
            embed = discord.Embed(title="오늘의 무너 상태 : 미인 :princess:", description= str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일 | " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second) + '일자 상태입니다', color=0x00ff00)
            await message.channel.send(embed=embed)
        if random == 2 :
            embed = discord.Embed(title="오늘의 무너 상태 : 돼지 :pig:", description= str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일 | " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second) + '일자 상태입니다', color=0x00ff00)
            await message.channel.send(embed=embed)

    ######################################################################################

    if message.content.startswith('와!') :
        await message.channel.send('와!'+message.content[2:]+' 아시는구나!\n참고로 그거 겁.나 어.렵.습.니.다')

    #######################################################################################

    if message.content.startswith('!실시간검색어') or message.content.startswith('!실검'):
        url = "https://www.naver.com/"
        html = urllib.request.urlopen(url)

        bsObj = bs4.BeautifulSoup(html, "html.parser")
        realTimeSerach1 = bsObj.find('div', {'class': 'ah_roll_area PM_CL_realtimeKeyword_rolling'})
        realTimeSerach2 = realTimeSerach1.find('ul', {'class': 'ah_l'})
        realTimeSerach3 = realTimeSerach2.find_all('li')


        embed = discord.Embed(
            title='네이버 실시간 검색어',
            description='실시간검색어',
            colour=discord.Colour.green()
        )
        for i in range(0,19):
            realTimeSerach4 = realTimeSerach3[i]
            realTimeSerach5 = realTimeSerach4.find('span', {'class': 'ah_k'})
            realTimeSerach = realTimeSerach5.text.replace(' ', '')
            realURL = 'https://search.naver.com/search.naver?ie=utf8&query='+realTimeSerach
            print(realTimeSerach)
            embed.add_field(name=str(i+1)+'위', value='**----'+realTimeSerach +'----**'+ '\n'+realURL, inline=False)

        await client.send_message(message.channel, embed=embed)

    bannum = 2
    mutnum = 1

    ##############################################################

    if message.content.startswith('경고 설정') :
        bannum = (int(message.content[6:]))
        await message.channel.send(message.content[6:]+"으로 경고 횟수를 설정 하였습니다")

    author5 = message.guild.get_member(message.content[9:27])
    warnfile = openpyxl.load_workbook('경고.xlsx')
    warnsheet = warnfile.active
    why = str(message.content[28:])
    whysheet = 'C'

    #경고 횟수 설정 함수#############################################

    if message.content.startswith('경고 부여') :
        i = 1
        while True :
            if warnsheet["A" + str(i)].value == str(message.content[9:27]) :
                warnsheet['B' + str(i)].value = int(warnsheet["B" + str(i)].value) + 1
                warnfile.save("경고.xlsx")
                if warnsheet["B" + str(i)].value == bannum:
                    await message.channel.send(author5 + "님은 경고 " + bannum + "회 누적으로 서버에서 추방되었습니다.")
                    await message.guild.kick(author5)
                else:
                    embed = discord.Embed(
                        title="경고",
                        color=0xFF0000
                    )
                    embed.add_field(name="경고 유저",value=str(author5), inline=False)
                    embed.add_field(name="경고 횟수",value=str(warnsheet["B" + str(i)].value) +" 회", inline=False)
                    embed.add_field(name="사유",value=why, inline=False)
                    embed.add_field(name="경고 부여 관리자",value=message.author.name, inline=False)
                    await message.channel.send(embed=embed)
                    warnsheet[str(whysheet) + str(i)].value = why
                    whysheet = chr(ord(whysheet) + 1)
                break
            if warnsheet["A" + str(i)].value == None:
                warnsheet["A" + str(i)].value = str(message.content[9:27])
                warnsheet["B" + str(i)].value = 1
                warnsheet[str(whysheet) + str(i)].value = why
                whysheet = chr(ord(whysheet) + 1)
                warnfile.save("경고.xlsx")
                await message.channel.send(str(author5) + "님은 경고를 1회 받았습니다.")
                break
            i += 1

    #경고 부여 함수##############################################################

    if message.content.startswith('경고 확인') :
        i = 1
        if message.content[6:24] == None :
            while True :
                if warnsheet['A' + str(i)] == str(message.author.id):
                    await message.channel.send(int(warnsheet['A' + str(i)]) + "회 경고")
                    break
                elif warnsheet['A' +str(i)] == None :
                    await message.channel.send('0회 경고')
                    break
                i += 1
        else :
            while True :
                if warnsheet['A' + str(i)] == str(message.content[6:24]):
                    await message.channel.send(warnsheet['A' + str(i)] + "회 경고")
                    break
                elif warnsheet['A' + str(i)] == None :
                    await message.channel.send('0회 경고')
                    break
                i += 1

    #경고 확인 함수#############################################################


    #봇 실행
client.run(NjYxNDc3NDYwMzkwNzA3MjAx.XiUygQ.8NTqQFnLn1IpzVGIQTyFvV1emaY)
