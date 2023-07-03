import random
import pickle
def ticket(a,b,xz,cz,c,d,e,f):
	fo=open('data.dat','ab')
	fi=open('teling.txt','a')
	fi.write('1')
	fi.write('\n')
	fi.close()
	kop={}
	z={1117:'Vistara at  9:00Am',1217:"Go Air at 10:00Am",1317:'Air India at 11:00Am',1417:'Indigo at 3:00Pm',1516:'Spice jet at 4:00Pm',1617:'Air Asia at 5:00Pm'}
	p={'Name':b,'Age':xz,'DOB':cz,'From':c,'To':d,'Date of journey':e,'Flight Detail':z[f]}
	kop[a]=p
	pickle.dump(kop,fo)
	fo.close()
def cancel(s):
	fo=open('data.dat','ab+')
	fi=open('teling.txt','a+')
	fo.seek(0)
	fi.seek(0)
	sg=fi.readlines()
	pr=len(sg)
	fi.close()
	c=0
	tz=[]
	for i in range(pr):
		set1=pickle.load(fo)
		if s  in set1.keys():
			c=c+1
			ty=set1.pop(s)	
		else:
			tz.append(set1)
	fo.close()
	ft=open('data.dat','wb')
	fn=open('teling.txt','w')
	for i in range(len(tz)):
		pickle.dump(tz[i],ft)
		fn.write('1')
		fn.write('\n')
	fn.close()
	ft.close()
	if c==0:
		return 'not found'
	else:
			return ty
	fo.close()
def check(m):
	fo=open('data.dat','ab+')
	fi=open('teling.txt','a+')
	fo.seek(0)
	fi.seek(0)
	eg=fi.readlines()
	pg=len(eg)
	fi.close()
	c=0
	for i in range(pg):
		set=pickle.load(fo)
		if m in set.keys():
			t=set[m]
			c=c+1
			return t
	if c==0:
		return 'not found'
	fo.close()
l='abcdefghijklABCDEFGHIJKL'
ks='mnopqrstuvwxyzMNOPQRSTUVWXYZ'
a='-'*50
b='-' * 50
print('\t\t',a)
print('\t\t\tFlight Managment system')
print('\t\t',b)
while True:
	print('\t\t1.login')
	print('\t\t2.exit')
	a=int(input('\t\tEnter Your Choice:'))
	if a==1:
		p=input('\t\tenter your full name:')
		d=input('\t\tenter a password:')
		print('\t\tWelcome',p)
		while True:
			print('\t\t1.Book Ticket')
			print('\t\t2.Cancel Ticket')
			print('\t\t3.Check Ticket')
			print('\t\t4.logout and Exit')
			z=int(input('\t\tEntet your choice:'))
			if z==1:
				print('\t\tTicket booking centre')
				q=random.randint(7056,9999)
				w=input('Enter your full name:')
				fz=input('Enter your age:')
				fx=input('Enter your DOB:')
				fro=input('Enter From:')
				to=input('Enter To:')
				date=input('Enter a journey date(DD|MM|YYYY):')
				if fro[0] in l:
					print('\t\t1117.Vistara Time:9:00 Am')
					print('\t\t1217.Go Air Time:10:00 Am')
					print('\t\t1317.Air India Time:11:00 Am')
					s=int(input('enter flight no you want to go:'))
					ticket(q,w,fz,fx,fro,to,date,s)
					print('your ticket is successfully done and your ticket no is:',q)
				elif fro[0] in ks:
					print('\t\t1417.Indigo Time:3:00 Pm')
					print('\t\t1517.Spice jet Time:4:00 Pm')
					print('\t\t1617.Air Asia Time:5:00 Pm')
					s=int(input('enter flight no you want to go:'))
					ticket(q,w,fz,fx,fro,to,date,s)
					print('your ticket is successfully done and your ticket no is:',q)
				else:
					p=1+2
			elif z==2:
				print('\t\tCancelling Ticket Window')
				a=int(input('\t\tenter your ticket no:'))
				f=cancel(a)
				if f=='not found':
					print('not found')
				else:
					we=f.keys()
					print('your ticket')
					print('-'*71)
					for i in we:
						print('\t\t\t',i,':',f[i])
					print('-'*71)
					print('\t\t\tcancel sucess')
			elif z==3:
				print('\t\tTicket Checking Center')
				u=int(input('enter ticket no:'))
				op=check(u)
				l=type(op)
				if op=='not found':
					print('not found')
				else:
					qw=op.keys()
					print('your tickets is:')
					print('-'*71)
					for i in qw:
						print('\t\t\t',i,'::',op[i])
					print('-'*71)
			elif z==4:
				r=input('enter your password:')
				if r==d:
					break
				else:
					print('wrong password')
			else:
				print('404:Not Found')
	elif a==2:
		print('\t\tthank you')
		break
	else:
		print('\t\t404:page not found')
	