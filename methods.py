def onesComplement(binary):
    #i need to match the bit lenght!!!
    onescomplement = ""
    for bit in binary:
        if bit == "0":
            onescomplement += "1"
        else:
            onescomplement += "0"
    print(f"the complement one is: {onescomplement}")
    return onescomplement

def twosComplement(onescomplement):
    #definir longitud de ancho de bits.
    print("in process")

def decimalToBinary(decimal):
        binary = ""
        while (decimal != 0):
            remainder = decimal % 2
            print(f"You did "+str(decimal)+" // 2"+ ", its remainder is: "+ str(remainder)+".")
            binary = str(remainder) + binary
            decimal = decimal // 2
        print(f"the number in binary is: "+binary+".")

        return binary
    
def convertNumber():
    try:
        decimal = int(input("Enter a decimal: "))
        if (decimal > 0):
            int(decimal)
            decimalToBinary(decimal)
        elif (decimal < 0):
            decimal = abs(decimal)
            binary = decimalToBinary(decimal)
            onesComplement(binary)
    except ValueError:
        print(f"u dumb.")
