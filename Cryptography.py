class runStringChange:
    ## I will attempt to code different types of ciphers:
    ## Subsitition- Done
    ## Transposition
    #polygraphic
    ##Permutation
    #this is a comment
    def __init__(self):
#         decoder = input('decoder')
#         encoder = input('encoder')
        inputString = input('Give a string\n')
        num = input('Input Cipher Encoding key\n')
        self.encoding(inputString,num)
    
    def encoding(self,string,num):
        num = int(num)
        newString = ""
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        alphabet = list(alphabet)
        for i in range(len(string)):
            letter = string[i]
            if (letter.isupper()):
                newString = newString + chr((ord(letter) + num-65) % 26 +65)
            else:
                newString = newString + chr((ord(letter) + num-97) % 26 +97)
        print(newString)
        
    def stringChange(self,string,decoder,encoder):
        d = decoder.upper()
        e = encoder.upper()
#         d = list(d)
        e = list(e)
        num = 0
        if len(decoder) == len(encoder):
            newString = ""
            for index in d:
                for letter in string.upper():
                    if letter == index:
                        newString = newString + e[num]
                        num+=1
        #                 elif letter == 'A':
        #                     newString = newString + 'I'
        #                 elif letter == 'S':
        #                     newString = newString + 'A'
        #                 elif letter == 'I':
        #                     newString = newString + 'N'
        #                 elif letter == 'L':
        #                     newString = newString + 'T'
        #                 elif letter == 'E':
        #                     newString = newString + 'S'
#                         else:
#                             newString = newString + letter
        print(string.upper())
        print(newString)
        
if __name__ == '__main__':
    
    runStringChange()
