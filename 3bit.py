import os

three_bit_trinary = [
    '000','001','002','010','011','012','020','021','022',
    '100','101','102','110','111','112','120','121','122',
    '200','201','202','210','211','212','220','221','222'
]

alphabet = [
    'a','b','c','d','e','f','g','h','i',
    'j','k','l','m','n','o','p','q','r',
    's','t','u','v','w','x','y','z',' '
]

three_bit_output2 = ""

os.system('cls')

def split(inputs):
    return list(inputs)

#print (split(inputs))

# def three_bit_checker(inputs):
while True:
    inputs = input("Type 0, 1, 2 or exit:\n\n")
    for index, value in enumerate(split(inputs)):
        if index == 0:
#            print ("First digit number " + str(index) +" is " + str(value))
            first = value
        elif index == 1:
#            print ("Second digit number " + str(index) +" is " + str(value))
            second = value
        elif index == 2:
#            print ("Third digit number " + str(index) +" is " + str(value))
            third = value
    three_bit = str(first + second + third)
    three_bit_index = three_bit_trinary.index(three_bit)
    three_bit_output2 = (three_bit_output2 + alphabet[three_bit_index] )
    print ("\n" + three_bit_output2 + "\n")