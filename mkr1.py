# Модульна контрольна робота номер 1
# Купрюхін Тимофій Артемович КІ-2
import random 
import numpy as np


def enter_data():
	try:
		question = int(input("Хочете ввести свої данні або скористуватися готовими? 1-свої данні, інші цифри-готові данні "))
	except ValueError: 
		print('\nКоректні данні будь-ласка!!\n')
		return enter_data()
	if question == 1:
		try: 
			N = int(input("Введіть розмірність масиву (N*N) "))
		except ValueError:
			return enter_data()
	else: 
		N = [[8, 4, 3, 7], [5, 1, 8, 3], [4, 1, 5, 7], [8, 8, 2, 2]]
	return N

def create_and_reshape():
	N = enter_data()
	if isinstance(N, int):
		arr = [random.randint(1, 10) for i in range(N**2)]
		arr = [list(i) for i in list(np.reshape(arr, [N, N]))]
	else: arr = N 
	return arr

def calculate_average(arr):
	return sorted(arr, key=lambda x: sum(x)/len(x))

print(calculate_average(create_and_reshape()))