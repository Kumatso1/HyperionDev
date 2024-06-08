def alternate_char_case(text):
  """
  This function takes a string and alternates the case of characters.

  Args:
      text: The input string.

  Returns:
      A new string with alternating upper and lower case characters.
  """
  result = ""
  for i, char in enumerate(text):
    if i % 2 == 0:
       result += char.upper()
    else:
       result +=char.lower()
  return result

def alternate_word_case(text):
  """
  This function takes a string and alternates the case of words.

  Args:
      text: The input string.

  Returns:
      A new string with alternating upper and lower case words.
  """
  words = text.split()
  result = " ".join(word.upper() if i % 2 == 0 else word.lower() for i, word in enumerate(words))
  return result

# Example usage for alternate character case
text1 = "Hello World"
alternate_text1 = alternate_char_case(text1)
print(alternate_text1)  # Output: HeLlO WoRlD

# Example usage for alternate word case
text2 = "I am learning to code"
alternate_text2 = alternate_word_case(text2)
print(alternate_text2)  # Output: i AM learning TO code
