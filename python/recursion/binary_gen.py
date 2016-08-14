def str_app(x,l):
	return [x+val for val in l]

def gen_str(len):
	if len == 0 :
		return []
	elif len == 1 :
		return ['0','1']
	else:
		return str_app('0',gen_str(len-1))+str_app('1',gen_str(len-1))

print gen_str(4)