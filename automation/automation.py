import shutil 
import re 

file = 'potential-contacts.txt'

f = open('./potential-contacts.txt')
global contents 
contents = f.read()


# Email regex due to zapier
def pull_email_from_file(importFile):
    contents = importFile
    regex = re.findall(r'[\w\.-]+@[\w\.-]+', contents)

    with open(contents, 'w') as f:
        f.write('\n'.join(regex))  


    # print(regex_email)

    # contents += regex_email

    new_copy = shutil.copy('potential-contacts.txt', './new-email.txt')
    print(new_copy)
    return new_copy


def pull_number_from_file(importFile):
    contents = importFile

    re.findall(r'(\+?\d[-\.\s]?)?(\(\d{3}\)\s?|\d{3}[-\.\s]?)\d{3}[-\.\s]?\d{4}', contents)

    new_copy = shutil.copy('potential-contacts.txt', './new-phone.txt')
    
    return new_copy


pull_email_from_file(file)
pull_number_from_file(contents)
