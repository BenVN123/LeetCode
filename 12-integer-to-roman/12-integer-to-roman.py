class Solution:
    def intToRoman(self, num: int) -> str:
        num = "0000" + str(num)
        num = num[-4:]
        output = ''
        
        for i in range(len(num)):
            if num[i] != '0':
                if i == 0:
                    output += (int(num[i]) * 'M')
                elif i == 1:
                    if num[i] == '4':
                        output += 'CD'
                    elif num[i] == '5':
                        output += 'D'
                    elif num[i] == '9':
                        output += 'CM'
                    elif int(num[i]) > 5:
                        output += 'D' + ((int(num[i]) - 5) * 'C')
                    else:
                        output += int(num[i])*'C'
                elif i == 2:
                    if num[i] == '4':
                        output += 'XL'
                    elif num[i] == '5':
                        output += 'L'
                    elif num[i] == '9':
                        output += 'XC'
                    elif int(num[i]) > 5:
                        output += 'L' + ((int(num[i]) - 5) * 'X')
                    else:
                        output += int(num[i])*'X'
                elif i == 3:
                    if num[i] == '4':
                        output += 'IV'
                    elif num[i] == '5':
                        output += 'V'
                    elif num[i] == '9':
                        output += 'IX'
                    elif int(num[i]) > 5:
                        output += 'V' + ((int(num[i]) - 5) * 'I')
                    else:
                        output += int(num[i])*'I'
        return output
        
