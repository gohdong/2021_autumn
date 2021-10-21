import keyboard
while True:
	recorded = keyboard.record(until='enter')
	print("===========")
	for x in recorded:
		if x.event_type == "down":
			print(x.name,end='')
		# print(dir(x))
		
	# print(recorded)
keyboard.play(recorded)
# while True:
# 	print(keyboard.wait('space'))
# 	print("!!")
# 	# a = keyboard.record()
# 	# print(a)
# 	# print('space was pressed! Wait  ing on it again...')123          asd  adasdasddasd       adasd          