def test_fun(test,exam,a=2):
    print(test,exam,a)
test_fun('vishnu','suji')

def another_test(ex):
    return 5 * ex
print(another_test(3))

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

try:
    print("Hello")
except:
    print("something went wrong")
else:
    print("nothing went wrong")