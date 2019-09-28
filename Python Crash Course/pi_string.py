with open ('./pi_digits.txt') as file_object:
    lines = file_object.readlines();

pi_string = ''
for line in lines:
    # strip the right part of the string 
    pi_string += line.rstrip();

print(pi_string);
print(len(pi_string));