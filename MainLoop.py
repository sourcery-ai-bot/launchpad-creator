from imports import *
import ReadEffect as re

def MainLoop(root):
	global DetectMidi
	global Page

	while(True):
		try:
			root.update()
		except:
			print('application closed')
			sys.exit()

		if DetectMidi==True:
			events = lp.ButtonStateRaw( returnPressure = True )
			if events != []:
				if events[0] >= 255:
					print(" PRESSURE: " + str(events[0]-255) + " " + str(events[1]))
				else:
					#Note On event
					if events[1] > 0:
						#print(" PRESSURE: " + str(events[0]) + " " + str(events[1]) )
						#lp.LedCtrlRawByCode(events[0],80)

						#GAM.Get(events[0])
						if events[0] == 89:
							Page=0
						if events[0] == 79:
							Page=1
						if events[0] == 69:
							Page=2
						if events[0] == 59:
							Page=3
						if events[0] == 49:
							Page=4
						if events[0] == 39:
							Page=5
						if events[0] == 29:
							Page=6
						if events[0] == 19:
							Page=7
			
						re.Read('./.Projects/Kaskobi - Paris/Kaskobi - Paris.json',events[0], Page)

					#Note Off event		
					else:
						pass
						#print(" PRESSURE: " + str(events[0]) + " " + str(events[1]) )
						#lp.LedCtrlRawByCode(events[0],3)
