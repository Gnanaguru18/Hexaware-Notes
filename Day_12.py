# break -> stop loop
# continue -> skip one iteration
# return -> exits out of function
 
 
# def print_nums():
#     for num in range(1, 10):
#         if num == 6:
#             break
 
#         print(num)
#     print("Execution continues 🎊")
 
 
# def skip_even():
#     for num in range(1, 10):
#         if num % 2 == 0:
#             continue
#         print(num)
#     print("Execution continues 🎊")
 
 
# Task 1: Find the first negative value
# def process_until_duplicate(numbers):
#     check_dup=set()
#     for i in numbers:
#         if i in check_dup:
#             print(f"Found duplicate, process stopped")
#             break
#         check_dup.add(i)
#         print(f"Processed {i}")

        
 
# if __name__ == "__main__":
#     process_until_duplicate(["apple", "banana", "carrot", "apple", "date", "banana"])
 

def censorship_bot(messages, banned_words):
    for i in banned_words:
        for j in messages:
            if i in j:
                continue
            print(f"Approved message: {j}")

 
messages = [
    "Hello everyone!",
    "This is a bad word example!",
    "Let's keep our chat clean!",
    "Oops another bad content!",
    "Have a nice day!"
]
 
banned_words = ["bad", "oops"]
censorship_bot(messages,banned_words)