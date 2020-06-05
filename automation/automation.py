import shutil 
import re 

file = open('potential-contacts.txt')
global contents 
contents = file.read()

# print(contents)

# Email regex due to zapier
regex_email = re.findall(r'[\w\.-]+@[\w\.-]+', contents)
# print(regex_email)
# Extract phone numbers from zapier d
regex_phone = re.findall(r'(\+?\d[-\.\s]?)?(\(\d{3}\)\s?|\d{3}[-\.\s]?)\d{3}[-\.\s]?\d{4}', contents)
# print(contents)
print(regex_phone)

