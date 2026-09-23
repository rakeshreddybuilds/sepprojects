# print("Hello World!")

# Strings

# message = "Helllo Worldss"

# print(message[::-1])
# print(message[0], message[-1])

# print(message[0] == message[-1])

# Take a String and swap its first half and second half
# example; "abcdef" to "defabc"
# first lets check the length of the string
# print(len(message))
# print(len(message) // 2)
# first_half = message[0:7]
# second_half = message[7:14]
# full_message = second_half + first_half
# print(full_message)

message = "I'm luffy king of the pirates"
message_split = message.split()
# print(len(message_split) // 2)
message_middle_word = len(message_split) // 2
new_message = message_split[message_middle_word]
print(new_message)
