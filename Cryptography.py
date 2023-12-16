class crypto:
    ## I will attempt to code different types of ciphers:
    ## Subsitition- Done
    ## Transposition - Done
    #polygraphic
    ##Permutation
    #this is a comment
    def __init__(self):
        self.runGUI()
    def testInt(self,string):
        '''Runs a test to make sure that the input for the ciphers is an integer: 
        input is a string of a number'''
        e = True
        while e == True:
            s = input(string)
            try:
                n = int(s)
                break
            except ValueError:
                print("Input: " + s + " is not a number\n")
        return n
    def testStr(self,string):
        '''Runs a test to make sure that the input does not contain an integer
        input is a string'''
        listNum = [0,1,2,3,4,5,6,7,8,9]
        e = True
        while e == True:
            s = input(string)
            for letter in s:
                if letter in listNum:
                    print('Input ' + s +  ' contains a number\n')
                else:
                    continue
            return s
            
    def getCipher(self):
        '''Calls the correct cipher based on user input, if cipher is out of range, testInt() is called again'''
        e = True
        while e == True:
            n = self.testInt('Pick one of the following ciphers\n1-Substitution\n2-Transposition\n3-SubstitutionDecode\n')
            if n == 1:
                self.subsitutionCipher()
                e = False
            elif n == 2:
                self.transpositionCipher()
                e = False
            elif n == 3:
                self.substitutionDecode()
                e = False
            else:
                print(str(n) + " is not a valid input.\n")
    def runGUI(self):
        '''provides the GUI for the User'''
        e = True
        while e == True:
            self.getCipher()
            question = input('Do you want to continue? Y or N\n')
            if question == 'N':
                print('ending program\n')
                e = False
            else:
                continue
    def subsitutionCipher(self):
        '''Runs the substitution cipher for the user'''
        string = input('Give a string\n')
        num = int(input('Input Cipher Encoding key (1-26)\n'))
        newString = ""
        print('Your input was ' + string + ' .')
        string = string.replace(" ", "")
        string = string.upper()
        for i in range(len(string)):
            letter = string[i]
            newString = newString + chr((ord(letter) + num-65) % 26 +65)
           
        print('Your output was '+ newString + ' .')
    def substitutionDecode(self):
        stringEncrypt = self.testStr('Provide the encyrypted string\n')
        num = self.testInt('Input Cipher Encoding key (1-26)\n')
        newString = ""
        print('The inputed string was '+ stringEncrypt + ' .')
        stringEncrypt = stringEncrypt.replace(" ", "")
        stringEncrypt = stringEncrypt.upper()
        for i in range(len(stringEncrypt)):
            letter = stringEncrypt[i]
            newString = newString + chr((ord(letter) - num-65) % 26 + 65)
        print('Your output was ' + newString + ' .')


    
    def transpositionCipher(self):
        '''Runs the transposition cipher for the user'''
        listOfKey = []
        key = self.testStr('Provide a key, must only contain letters\n')
        key = key.upper()
        tempListOfKey = [*key]
        num = 1
        for i in range(len(tempListOfKey)):
            listOfKey.append([])
            listOfKey[i].append([])
            listOfKey[i].append([])
            listOfKey[i].append([])
            listOfKey[i].append([])
            listOfKey[i][0] = tempListOfKey[i]
            listOfKey[i][1] = num
            num += 1
        listOfKey.sort(key=lambda x: x[0])
        n = 1
        for i in range(len(listOfKey)):
            listOfKey[i][2] = n
            n += 1
        listOfKey.sort(key=lambda x: x[1])
        userString = self.testStr('Provide the message to encode\n')
        userString = userString.replace(" ", "")
        userString = userString.upper()
        sizeKey = len(listOfKey)
        sizeUserString = len(userString)
        size3 = (sizeUserString//sizeKey) + 1
        groups = []
        for i in range(size3):
            group = userString[i * sizeKey: (i+1) * sizeKey]
            groups.append(group)
        if sizeUserString % sizeKey != 0:
            num0 = sizeKey - sizeUserString % sizeKey
            groups[-1] += '0' * num0
        for i in range(len(listOfKey)):
            for j in range(size3):
                listOfKey[i][3].append([])
                listOfKey[i][3][j] = groups[j][i]
        listOfKey.sort(key=lambda x: x[2])
        output = []
        for i in range(sizeKey):
            output.append(listOfKey[i][3])
        for i in range(sizeKey):
            output[i] = "".join(output[i])
        output = "".join(output)
        output = output.replace('0','')
        print(output)

if __name__ == '__main__':
    
    crypto()
