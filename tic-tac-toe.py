b = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
players = ['x', '0']
winner = False

player = input(f'Начинаем игру "крестики-нолики". Игрок №1 выбирает фигуру - "x" или "0": ')
n = 1

while player not in ('x', '0'):
	player = input("Ошибка! Вы должны выбрать 'x' или '0. Попробуйте еще раз: ")
	n = 1

while winner is False:
	if b.count('-') != 0:
		print('    0     1     2')
		for j in range(3):
			print(j, end=' ')
			for i in range(3):
				print(' ', b[3 * j + i], ' ', end=' ')
			print('\n')

		print(f'Ходит игрок №{n}. Ваша фигура - "{player}".')
		move = input("Введите через пробел номер столбца и номер строки, после чего нажмите ENTER: ").split()

		if move[0] not in ('0', '1', '2') or move[1] not in ('0', '1', '2'):
			print(f'Ваш ход должен лежать в диапазоне от 0 до 2')
		elif b[3 * int(move[1]) + int(move[0])] != '-':
			print('Эта клетка уже занята!')
		else:
			b[3 * int(move[1]) + int(move[0])] = player
			player = players[0] if player == players[1] else players[1]

			win = [[b[0], b[1], b[2]], [b[3], b[4], b[5]], [b[6], b[7], b[8]], [b[0], b[3], b[6]],
				   [b[1], b[4], b[7]], [b[2], b[5], b[8]], [b[0], b[4], b[8]], [b[2], b[4], b[6]]]
			for elem in win:
				if elem[0] == elem[1] == elem[2] != '-':
					print(f"Игра закончена! Игрок №{n} победил!")
					winner = True
			n = 2 if n == 1 else 1

	else:
		print('Вы сыграли вничью!')
		break



