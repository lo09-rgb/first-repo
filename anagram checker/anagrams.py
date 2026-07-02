# Function to check if two strings are anagrams
def check_anagram(str1, str2):
    # Remove spaces and convert both strings to lowercase
    cleaned_str1 = str1.replace(" ", "").lower()
    cleaned_str2 = str2.replace(" ", "").lower()
    
    # If the sorted characters are identical, they are anagrams
    return sorted(cleaned_str1) == sorted(cleaned_str2)

# Get inputs from the user
user_input1 = input("Enter the first phrase or word: ")
user_input2 = input("Enter the second phrase or word: ")

# Execute the check and display the result
if check_anagram(user_input1, user_input2):
    print(f'"{user_input1}" and "{user_input2}" are anagrams!')
else:
    print(f'"{user_input1}" and "{user_input2}" are NOT anagrams.')
