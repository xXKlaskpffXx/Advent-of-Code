import hashlib

data = "yzbqklnj"
for num in range(10000000):
    digest = hashlib.md5((data + str(num)).encode())
    result = digest.hexdigest()
    if result[:6] == '000000':
        print(result)
        print(num)

