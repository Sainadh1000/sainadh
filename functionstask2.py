#transfer text into lowercase and checks palindrome or not
def clean_input(text):
    clean_text=text.strip().lower()
    return clean_text
def is_palindrome(text):
        text = clean_input(text)
        if text==text[::-1]:
              print("true")
        else:
              print("false")
def main():
      text=input("enter text:")
      is_palindrome(text)
main()

        
        



