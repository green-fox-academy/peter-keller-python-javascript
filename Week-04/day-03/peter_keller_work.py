class Tasks(object):
    def get_apple(self):
        item = "apple"
        return item

#    def sum_of_elements(self, list_of_numbers):
#        sum_result = 0
#        for item in list_of_numbers:
#            sum_result += int(item)
           
#        return sum_result

    def anagram(self, text_one, text_two):
        if len(text_one) == len(text_two):
            if sorted(text_one) == sorted(text_two):
                return True
            else:
                return False

#    def count_letters(self, word):
#        dictionary = {}
#        for characters in list(word):
#            dictionary[characters] = word.count(characters)
#        return dictionary
            
#    def fibonacci(self, number):
#        a,b = 1,1
#        for i in range(number-1):
#            a, b = b, a + b
#        return a