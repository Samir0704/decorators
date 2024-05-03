def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("Ijro etilishidan oldin")

        # qaytarilgan qiymatni olish
        returned_value = func(*args, **kwargs)
        print("ijro etilishidan keyin")

        # qiymatni asl ramkaga qaytarish
        return returned_value

    return inner1


# funksiyaga dekorator qo'shish
@hello_decorator
def sum_two_numbers(a, b):
    print("Funktsiya ichida")
    return a + b


a, b = 2, 2

# funktsiyani qaytarish orqali qiymatni belgilash
print("Sum =", sum_two_numbers(a, b))





# dekoratr zanjirini sinash uchun kod
def decor1(func):
	def inner():
		x = func()
		return x * x
	return inner

def decor(func):
	def inner():
		x = func()
		return 2 * x
	return inner

@decor1
@decor
def num():
	return 10

@decor
@decor1
def num2():
	return 10

print(num())
print(num2())


def hello_decorator(func):
    # inner1 - bu Wrapper funksiyasi
	# argument deb ataladi

	# ichki funksiya tashqi mahalliyga kirishi mumkin
	# funksiya bu holatda "func" kabi yozildi
	def inner1():
		print("Hello, this is before function execution")

		func()

		print("This is after function execution")

	return inner1


# oʻram ichida chaqiriladigan funksiyani aniqlash
def function_to_be_used():
	print("This is inside the function !!")


# ichida "foydalanish_funksiyasi"ni o'tkazish
#Uning xatti-harakatlarini boshqarish uchun dekorator
function_to_be_used = hello_decorator(function_to_be_used)

function_to_be_used()

#



