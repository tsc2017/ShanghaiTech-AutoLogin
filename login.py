#!/usr/bin/env python3
 
import urllib
import urllib.parse
import urllib.request
import http.client
import string, random
import json
import getpass
import time

#======================================================
#自动登录请输入账号密码，留空将询问
username = ''
password = ''
#======================================================
#语言 language
lang = 'ZH'
#lang = 'EN'
#======================================================

print('')
if lang == 'ZH':
	print('上海科技大学 校园网络自动登录助手')
	print('开发:上海科技大学 信息科学与技术学院 吕文涛')
	print('开发版本，严禁外传')
else:
	print('ShanghaiTech EZNetLoginer')
	print('Developer : eastpiger (Lv Wentao) , SIST , ShanghaiTech University')
	print('Under development')
while True:	
	print('========================================')
	httpClient = None
	try:
		if username == '':
			if lang == 'ZH':
				print('请输入登录账号：', end="")
			else:
				print('Username:', end="")
			username = input('')
		if password == '':
			if lang == 'ZH':
				print('请输入登录密码（密码并不会在此处显示，请直接输入即可）：',end="")
			else:
				print('Password:',end="")
			password = getpass.getpass('')
		print('')
		if lang == 'ZH':
			print('读取到账号。')
		else:
			print('account got.')
		print('========================================')

		while True:
			#======================================================
			#Define
			url="https://controller.shanghaitech.edu.cn:8445/PortalServer/Webauth/webAuthAction!login.action"
			params = urllib.parse.urlencode({'userName': username, 'password':password,'hasValidateCode':False,'authLan':'zh_CN'})
			cookie_code = ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a','1','2','3','4','5','6','7','8','9','0'], 32)).replace(' ','')
			headers = {'Content-type': 'application/x-www-form-urlencoded'
							, 'Accept': '*/*','Cookie':'JSESSIONID=' + cookie_code}
			httpClient = http.client.HTTPSConnection('controller.shanghaitech.edu.cn', 8445, timeout=30)
			#======================================================

			if lang == 'ZH':
				print('正在登录……',end="")
			else:
				print('Logining……',end="")
			httpClient.request('POST', '/PortalServer/Webauth/webAuthAction!login.action', params, headers)
			response = httpClient.getresponse()
			if response.status != 200:
				if lang == 'ZH':
					print('连接失败！请确认网络已经连接')
				else:
					print('Connection Failed! Is the network available?')
				connect()
				exit()
			else:
				response_data = response.read().decode('utf-8')
				#print(response_data)
				response_data_json = json.loads(response_data)
				if response_data_json['success'] != True:
					if lang == 'ZH':
						print('登录失败！请确认账号可用')
					else:
						print('Login Failed! Is your account available?')
					exit()
				else:
					if lang == 'ZH':
						print('成功！')
						print('登录账号：' + response_data_json['data']['account'])
						print('内网ip：' + response_data_json['data']['ip'])
					else:
						print('Success!')
						print('Username:' + response_data_json['data']['account'])
						print('ClientIP:' + response_data_json['data']['ip'])

			time.sleep(1)
			print('========================================')
		
	except Exception as e:
		if lang == 'ZH':
			print('未知错误，请确认网络已经连接')
		else:
			print('Unknown Error! Is the network available?')
		print(e)
	finally:
		if httpClient:
			httpClient.close()
		#Retry in 1 second after a failed connection
		time.sleep(1)
