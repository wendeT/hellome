'''
A simple neural net to learn or-logic gate
Weight - Randomly initialized
learning rate - Randomly initialized
bias - set to -1 
'''
import random


data_x = [[0,0],[1,0],[0,1],[1,1]]
data_y = [0,0,1,1]
weight = [random.random()]*(len(data_y)-1)
l_rate = random.random()
bias = -1
model_y = [0]*len(data_y)



def weight_f(x_index,model_y,data_y):
	weight[0] = round((weight[0] + l_rate*(data_y-model_y)*bias),2)
	weight[1] = round((weight[1] + l_rate*(data_y-model_y)*data_x[x_index][0]),2)
	weight[2] = round((weight[2] + l_rate*(data_y-model_y)*data_x[x_index][1]),2)


def adder_f(index_i):
	new_value = weight[0]*bias + weight[1]*data_x[index_i][0] + weight[2]*data_x[index_i][1]
	return new_value


def activater_f(value_):
	return 1 if value_ > 0 else 0


def train_f():
	flag = 0;epoch = 0
	while flag < len(data_y):
		flag = 0
		epoch += 1
		print 'epoch %d ' % (epoch)
		for i in range(len(data_y)):
			model_y[i] = activater_f(adder_f(i))
			if  model_y[i] == data_y[i]:
				flag += 1
			else:
				print '		Current weight %s ' % (weight)
				weight_f(i,model_y[i],data_y[i])
				print '		Updated weights %s ' % (weight)
if __name__ == '__main__':
	train_f()
	print 'Final weights %s ' % (weight)
	print 'Learning rate %f ' % (l_rate)	
	print 'Bias %f ' % (bias)	















