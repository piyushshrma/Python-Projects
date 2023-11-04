st=input("Enter string for checking palindrome:");

cleaned=''

for c in st:
    if(c.isalpha()):
        cleaned+=c.lower();

def reverse_str(x):
  return x[::-1];

reverse=reverse_str(cleaned);
if(reverse==cleaned):
     print("HURRAY! Its palindrome.")
else:
    print("OhHHHH SHittttttttt! Its not palindrome.")
