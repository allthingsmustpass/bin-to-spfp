def bitLenght(binary, bit_lenght):
    if len(binary) >= bit_lenght:
        return binary
    else:
        addedceros = bit_lenght - len(binary)
        for i in range(addedceros):
            binary = '0' + binary
        return binary

def onesComplement(binary):
    onescomplement = ""
    for bit in binary:
        if bit == "0":
            onescomplement += "1"
        else:
            onescomplement += "0"
    print(f"the complement one is: {onescomplement}")
    return onescomplement

def twosComplement(onescomplement):
    carry = 1
    twoscomplement = ""
    onescomplement = list(onescomplement.strip(""))
    for i in reversed(onescomplement):
            if (i == "0" and carry == 1):
                twoscomplement = "1" + twoscomplement
                carry = 0
            elif (i == "1" and carry == 1):
                twoscomplement = "0" + twoscomplement
            else:
                twoscomplement = i + twoscomplement
    str(twoscomplement)
    print(f"two's compliment is: {twoscomplement}")
            
def fractionalDecimalToBinary(decimal):
    print("working on it.")

def decimalToBinary(decimal):
        binary = ""
        while (decimal != 0):
            remainder = decimal % 2
            print(f"You did "+str(decimal)+" // 2"+ ", its remainder is: "+ str(remainder)+".")
            binary = str(remainder) + binary
            decimal = decimal // 2
        bit_lenght = int(input("how many bits? "))
        binary = bitLenght(binary, bit_lenght)
        print(f"the number in binary is: "+binary+".")
        return binary
    
def convertNumber():
    try:
        decimal = int(input("Enter a decimal: "))
        if (decimal > 0):
            decimalToBinary(decimal)
        elif (decimal < 0):
            decimal = abs(decimal)
            binary = decimalToBinary(decimal)
            onescomplement = onesComplement(binary)
            twosComplement(onescomplement)
    except ValueError:
        print(f"u dumb.")