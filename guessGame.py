#coding=utf-8
import random
class Guess(object):
	'''
	获胜是在指定次数内猜出电脑生成的随机四位数	
	每次猜错电脑会返回相应结果，A表示有一个数位置正确，B表示有一个数在答案中有但位置不正确,
	0000标示四个数全都没有

	'''
	def __init__(self,times):
		
		self.answer = ''
		self.times = times
		self.useanswer = ''
	def randanswer(self):
		'''
		sample 生成不重复的列表
		'''
		self.answerList = random.sample(range(0,10),4)
		for i in self.answerList:
			self.answer+=str(i)
		# print self.answer　　
	def userinput(self):
		'''
		用来检测用户输入是否合法，不合法的输入并不会增加猜测次数
		'''
		while 1:
			usi= raw_input('请输入四位不等整数')
			if usi == 'exit' or (usi.isdigit() and len(usi)==4 and usi[0]!=usi[1]!=usi[2]!=usi[3]):
				return usi
			else:
				print "你输入的不符合格式！！"
	def ruler(self):
		'''
		这部分是游戏的精华部分，用来控制电脑的返回结果
		'''
		self.resultA = ''
		self.resultB = ''
		if self.answer == self.useanswer:
			print '你胜利了'
			return 'bingo'
		else:
			for i in range(4):
				if self.useanswer[i] == self.answer[i]:
					self.resultA += 'A'
				elif self.useanswer[i] in self.answer:
					self.resultB += 'B'
			if len(self.resultA)+len(self.resultB) == 0:
				print '0000'
			else:
				print (self.resultA+self.resultB)
	def showanswer(self):
		print '答案是',self.answer
	def giveup(self):
		'''
		用户可以输入exit标示放弃,同时电脑会讲答案返回给用户
		'''
		if self.useanswer =='exit':
			self.showanswer()
			return 1
	def rungame(self):
		'''
		游戏主体，结合各个方法实现游戏目的
		'''
		self.randanswer()
		i=0
		while 1:
			i+=1
			if i==self.times:
				self.showanswer()
				break
			self.useanswer = self.userinput()
			if self.giveup() or self.ruler():
				break
if __name__=="__main__":
	p1 = Guess(times=10)
	p1.rungame()