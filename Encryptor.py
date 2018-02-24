import GCD_Calculator as gcd


alphabet_list = ['a','b','c','d','e','f','g','h','i',
                 'j','k','l','m','n','o','p','q','r',
                 's','t','u','v','w','x','y','z']

for i in range(26):
    exec(alphabet_list[i] + ' = ' + str(i))
i = 8

def get_keys():
    global n, n_0, prime_1, prime_2
    prime_1 = input("First prime number: ")
    prime_2 = input("Second prime number: ")
    n = int(prime_1) * int(prime_2)
    n_0 = (int(prime_1) - 1)*(int(prime_2) -1)
    set_e()

def set_e():
    global public_key, private_key
    e_value = int(input("Set value of e such that gcd(e, " + str(n_0) + ")=1 and 1 < e < " + str(n_0)+ ": "))
    if gcd.gcd(e_value, n_0) == 1 and 1 < e and e < n_0:
        public_key = (e_value, n)
        private_key = (solve_mod(e_value, 1 , n_0), n)
        print("Public key: " + str(public_key) +"\nPrivate key: " +str(private_key))
    else:
        set_e()
    
def solve_mod(coeff, value, mod):
    count = 1
    while True:
        if (coeff * count) % mod == value:
            return count
        elif count == mod - 1:
            return "Not found."
        else:
            count += 2
def send(M, key):
    return (M ** key[0]) % key[1]

def encrypt(s,key):
    output = list()
    s = s.lower()
    for i in s:
        if i != ' ':
            exec("curr_x = " + i, globals())
            output.append(curr_x)

    output_2 = list()
    for j in output:
        output_2.append(send(j,key))

    output_3 = str()
    for k in output_2:
        output_3 += str(k) + ' '

    return output_3[:-1]

def decrypt(s, key):
    lst = s.split(' ')
    output = list()

    for i in lst:
        output.append((int(i) ** key[0]) % key[1])
    
    output_2 = str()
    for j in output:
        output_2 += alphabet_list[j]

    return output_2
















