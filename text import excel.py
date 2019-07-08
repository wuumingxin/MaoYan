import xlwt

def file_txt(path):
	with open(path, 'r', encoding='utf-8') as f:
		file = f.readlines()
	return file

def write_excel(a):
	# global false, null, true
	# false = False
	# true = True
	# null = ''
	workbook = xlwt.Workbook(encoding='utf-8')
	sheet = workbook.add_sheet('数据表')
	lieming = ['index','image','title','actor','time','score']
	for i in range(6):
		sheet.write(0, i, lieming[i])
	count = 0
	for y in a:
		count += 1
		y = eval(y)
		for z in range(6):
			n = y[lieming[z]]
			sheet.write(count, z, n)
	workbook.save('maoyantop100.xls')

def main():
	file_name = 'result.txt'
	file_shuju = file_txt(file_name)
	write_excel(file_shuju)

if __name__ == '__main__':
	main()

