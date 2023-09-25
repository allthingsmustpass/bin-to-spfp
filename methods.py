def normalizeBinary(binary):
    decimalmark = 0
    str(binary)
    for bit in reversed(binary):
         decimalmark = decimalmark + 1
         if (bit == "1"):
            print("we find it!")
            break
    print("the exponent is: "+str(decimalmark)+".")
    return decimalmark

def findExponent(binary):
    e = 0
    l = len(binary) #idk what better names this can have.
    str(binary)
    for bit in binary:
         e = e + 1
         if (bit == "1"):
            print("we find it!")
            break
    exponent =  l - e
    print("the exponent is: "+str(exponent)+".")
    return exponent
               
def adjustExponent(exponent):
    
    adjusted_exponent = exponent + 2**7 - 1
    print("the adjusted exponent is: "+str(adjusted_exponent)+".")
    return adjusted_exponent

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
    onescomplement = list(onescomplement.strip())
    for i in reversed(onescomplement):
            if (i == "0" and carry == 1):
                twoscomplement = "1" + twoscomplement
                carry = 0
            elif (i == "1" and carry == 1):
                twoscomplement = "0" + twoscomplement
            else:
                twoscomplement = i + twoscomplement

            if (carry == 1):
                print("Overflow!")
            
    print(f"two's compliment is: {twoscomplement}")
    return twoscomplement
            
def fractionalDecimalToBinary(decimal):
    print("working on it.")

def decimalToBinary(decimal):
        binary = ""
        while (decimal != 0):
            remainder = decimal % 2
            print(f"You did "+str(decimal)+" // 2"+ ", its remainder is: "+ str(remainder)+".")
            binary = str(remainder) + binary
            decimal = decimal // 2
        #bit_lenght = int(input("how many bits? "))
        #binary = bitLenght(binary, bit_lenght)
        print(f"the number in binary is: "+binary+".")
        return binary
    
def convertNumber():
    try:
        decimal = int(input("Enter a decimal: "))
        if (decimal > 0):
            sign = "0"
            binary = decimalToBinary(decimal)
            exponent = findExponent(binary)
            mantissa = moveComa(binary, exponent)
            decimal = adjustExponent(exponent)
            adjusted_exponent = decimalToBinary(decimal)
            adjusted_mantissa = normalizeMantissa(mantissa) #fix!
            buildFloatingPoint(sign, adjusted_exponent, adjusted_mantissa)
        elif (decimal < 0):
            sign = "1"
            decimal = removeSign(decimal)
            binary = decimalToBinary(decimal)
            exponent = findExponent(binary)
            mantissa = moveComa(binary, exponent)
            decimal = adjustExponent(exponent)
            adjusted_exponent = decimalToBinary(decimal)
            adjusted_mantissa = normalizeMantissa(mantissa) #fix!
            buildFloatingPoint(sign, adjusted_exponent, adjusted_mantissa)
    except ValueError:
        print(f"u dumb.")

def moveComa(binary, exponent):
        mantissa = binary[:-exponent] + "," + binary[-exponent:]
        print(f"the mantissa with the comma is: {mantissa}")
        return mantissa

def normalizeMantissa(mantissa):
    for i, bit in enumerate(mantissa):
        if(bit == "1"):
            mantissa = mantissa[:i] + "" + mantissa[i+2:] + " 0000 0000 0000 0000 0000"
            break
    print(f"the adjusted mantissa is: {mantissa} ")
    return mantissa

def buildFloatingPoint(sign, adjusted_exponent, adjusted_mantissa):
    print("the sign is: "+sign+" the exponent is: "+adjusted_exponent+" the mantissa is: "+adjusted_mantissa)
    return sign + adjusted_exponent + adjusted_mantissa

def removeSign(decimal):
    """removes the sign from a decimal number if it is negative.

    @param: decimal (int or str): the decimal number that have a sign.

    @return (int): the absolute value of the decimal number without its sign.
    """
    decimal = str(decimal)
    if decimal[0] == "-":
        decimal = decimal[1:]
    print(f"the decimal without sign is: {decimal}")
    decimal = int(decimal)
    return decimal