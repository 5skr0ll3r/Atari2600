currentXPos = 15
HDirection = None
HBlank = 68
cpuCycles = 5

def calcTIACycles(cpuCycles):
	return cpuCycles * 3

def realPosX(currentXPos, HBlank):
	positionX = currentXPos + HBlank 
	return positionX

def setPositionX(positionX, tiaCycles, fineNum, HDirection, asl):
	remainder = positionX % tiaCycles
	xor = remainder ^ tiaCycles
	AShiftLeft = xor << asl
	print('=' * 20)
	print(f'Normal\nCurrent X Position (with HBlank as offset:68): {positionX} \nMoving {HDirection}\nRemainder (sbc): {remainder}\n(xor): {xor}\n(asl): {AShiftLeft}\n')
	print(f'Bin\nCurrent X Position (with HBlank as offset:68): {bin(positionX)} \nMoving {HDirection}\nRemainder (sbc): {bin(remainder)}\n(xor): {bin(xor)}\n(asl): {bin(AShiftLeft)}\n')


def main():
	positionX = realPosX(currentXPos, HBlank)



	while True:
		key = input("Press key: ")
		if(key == 'a'):
			HDirection = "Left"
			positionX -= 1

		elif(key == 'd'):
			HDirection = "Right"
			positionX += 1

		setPositionX(positionX, 15, calcTIACycles(cpuCycles), HDirection, 4)

if __name__ == '__main__':
	main()
