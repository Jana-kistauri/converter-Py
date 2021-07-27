'''
სანტიმეტრი, მეტრი, კილომეტრი, მილი.

პროგრამის მუშაობის ლოგიკის მაგალითი:
1) ინტერაქტიულ რეჟიმში პროგრამა გვეკითხება რომელი საზომი ერთეული შეგვყავს (სანტიმეტრი? მეტრი? კილომეტრი თუ მილი?), მაგ. ავირჩიეთ კილომეტრი;
2) საზომი ერთეულის არჩევის შემდეგ შეგვყავს მისი რიცხვითი მნიშვნელობა, მაგ. 10;
3) პროგრამა ისევ გვეკითხება რომელ საზომ ერთეულში გვსურს ზემოთაღნიშნული მნიშვნელობის დაკონვერტირება, მაგ. ავირჩიეთ მილი;
4) ეკრანზე იბეჭდება: 10 კილომეტრი არის 6.21371 მილი;
5) გააკონტროლეთ, რომ პროგრამაში თითოულ ნაბიჯზე მოხდეს კორექტული მნიშვნელობების შეტანა;
6) პროგრამაში გამოიყენეთ კლასები და მეთოდები

'''


class Converter:

	def __init__(self, op1, amount, op2):
		self.op1 = op1
		self.amount = amount
		self.op2 = op2



	def sm_To_M(self):
		return self.amount / 100

	def sm_To_Km(self):
		return self.amount / 100000

	def sm_To_Ml(self):
		return self.amount / 16093.4

	def m_To_Sm(self):
		return self.amount * 100

	def m_To_Km(self):
		return self.amount / 1000

	def m_To_Ml(self):
		return self.amount / 1609.34

	def km_To_Sm(self):
		return self.amount * 100000

	def km_To_m(self):
		return self.amount * 1000

	def km_To_Ml(self):
		return self.amount / 1.60934

	def ml_To_Sm(self):
		return self.amount * 160934

	def ml_To_m(self):
		return self.amount * 1609.34

	def ml_To_Km(self):
		return self.amount * 1.60934


def checkAmountType(amount):
	while True:

		if not amount.isdigit():
			amount = input("გთხოვთ, შეიტანეთ რიცხვი: ")
			continue

		if  int(amount) < 0:
			amount = input("გთხოვთ, შეიტანეთ დადებითი რიცხვი: ")
			continue

		amount = int(amount)
		break

	return amount


def checkOptionsType(op):

	while True:

		if op.isdigit():
			op = input("გთხოვთ შეიყვანეთ ერთეულის დასახელება - (sm, m, km, ml): ")
			continue
		else:
			op = op.lower()



		if not (op == "sm" or op == "m" or op == "km" or op == "ml" or "exit"):
			op = input("გთხოვთ შეიყვანეთ ერთეულის სწორი დასახელება - (sm, m, km, ml): ")
			continue

		break

	return op


def is_op1_equal_op2(op1, op2):
	while True:
		
		if op1 == op2:
			op2 = input("გთხოვთ, შეიყვანეთ პირველისგან განსხვავებული ერთული: ")
			continue

		break	

	return op2


		

def menu():

	while True:

		op1 = input("შეიტანეთ საზომი ერთეული (sm, m, km, ml) ან 'exit' გამოსვლისთვის: ")
		op1 = checkOptionsType(op1)

		if op1 == "exit":
			print("ნახვამდის!")
			break
		

		amount = input("შეიტანეთ რაოდენობა: ")
		amount = checkAmountType(amount);

		op2 = input("შეიტანეთ მეორე საზომი ერთეული (sm, m, km, ml) ან 'exit' გამოსვლისთვის: ")
		op2 = checkOptionsType(op2)

		print("-" * 30)

		if op2 == "exit":
			print("ნახვამდის!")
			break

		op2 = is_op1_equal_op2(op1, op2)
	 


		userInput = Converter(op1, amount, op2)

		if op1 == "sm":
			if op2 == "m":
				converted = userInput.sm_To_M()

			elif op2 == "km":
				converted = userInput.sm_To_Km()

			elif op2 == "ml":
				converted = userInput.sm_To_Ml()



		elif op1 == "m":
			if op2 == "sm":
				converted = userInput.m_To_Sm()

			elif op2 == "km":
				converted = userInput.m_To_Km()

			elif op2 == "ml":
				converted = userInput.m_To_Ml()



		elif op1 == "km":
			if op2 == "sm":
				converted = userInput.km_To_Sm()

			elif op2 == "m":
				converted = userInput.km_To_m()

			elif op2 == "ml":
				converted = userInput.km_To_Ml()



		elif op1 == "ml":
			if op2 == "sm":
				converted = userInput.ml_To_Sm()

			elif op2 == "m":
				converted = userInput.ml_To_m()

			elif op2 == "km":
				converted = userInput.ml_To_Km()

		print(f"{amount} {op1} = {converted} {op2} \n")

menu()


