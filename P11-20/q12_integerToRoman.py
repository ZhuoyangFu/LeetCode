# Solution 1
# class Solution(object):
#     def intToRoman(self, num):
#         """
#         :type num: int
#         :rtype: str
#         """
#         list = ''
#
#         while num > 0:
#             if num >= 1000:
#                 n, num = num // 1000, num % 1000
#                 list += n * 'M'
#             if num >= 500:
#                 if str(num)[0] == '9':
#                     list += 'CM'
#                     num -= 900
#                 else:
#                     n, num = num // 500, num % 500
#                     list += n * 'D'
#             if num >= 100:
#                 if str(num)[0] == '4':
#                     list += 'CD'
#                     num -= 400
#                 else:
#                     n, num = num // 100, num % 100
#                     list += n * 'C'
#             if num >= 50:
#                 if str(num)[0] == '9':
#                     list += 'XC'
#                     num -= 90
#                 else:
#                     n, num = num // 50, num % 50
#                     list += n * 'L'
#             if num >= 10:
#                 if str(num)[0] == '4':
#                     list += 'XL'
#                     num -= 40
#                 else:
#                     n, num = num // 10, num % 10
#                     list += n * 'X'
#             if num >= 5:
#                 if num == 9:
#                     list += 'IX'
#                     num -= 9
#                 else:
#                     n, num = num // 5, num % 5
#                     list += n * 'V'
#             if num >= 0:
#                 if num == 4:
#                     list += 'IV'
#                     num -= 4
#                 else:
#                     list += num * 'I'
#                     num = 0
#         return list
#---------------------------------------------------------------------------------------------------
#Solution 2
class Solution(object):
    #Advanced answer from Internet
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        int_to_roman = [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),
                        (100,"C"),(90,"XC"),(50,"L"),(40,"XL"),
                        (10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]

        roman_num = ""
        for number,roman in int_to_roman:
            count,num = divmod(num,number)
            roman_num += roman * count
            if num == 0:
                break
        return roman_num