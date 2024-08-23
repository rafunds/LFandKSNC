# Function to generate all possible combinations of 0s and 1s for a given length
def generate_binary_strings(length):
    binary_strings = []
    for i in range(2**length):
        binary_strings.append(format(i, '0{}b'.format(length)))
    return binary_strings

# Function 'generate_final_vector()'' generates the final KSNC deterministic assignment

#To find Pa one should comment out A3B3
#To find Pb one should comment out A2B2
#To find Pc one should comment out A2B3
#To find Pd one should comment out A3B2

#Note that the deterministic behaviors will be 32 dimensional
#To read the 36-dimensional behavior for the intersection polytope one needs to
#translate the correct dimension to the 3,3-LF scenario once you input these points to
#a program that makes V-rep to H-rep transformations such as PORTA or PANDA

#If using PORTA the outputs will be inequalities with x=(x1,x2,...,x32) vectors and
#when considering the intersection the final behavior is an x=(x1,x2,...,x36) vector
#according to the fixed choices (see README of the GitHub)

#Here is how one does the translation (after PORTA is used):

#Pa does not need a translation

#Pb needs a translation x17->x21, x18->x22, ..., x32->x36

#Pc needs a translation x21->x25, x22->x26, ..., x32->x36

#Pd needs a translation x29->x33, x30->x34, x31->x35, x32->x36


def generate_final_vector(L):
    final_v = []
    for A1 in range(2):
        for B1 in range(2):
            v=0
            if str(A1)==L[0] and str(B1)==L[3]: #If the values of the assignments match the global one we change it to 1
                v=1
            final_v.append(v)
    for A1 in range(2):
        for B2 in range(2):
            v=0
            if str(A1)==L[0] and str(B2)==L[4]:
                v=1
            final_v.append(v)
    for A1 in range(2):
        for B3 in range(2):
            v=0
            if str(A1)==L[0] and str(B3)==L[5]:
                v=1
            final_v.append(v)
    for A2 in range(2):
        for B1 in range(2):
            v=0
            if str(A2)==L[1] and str(B1)==L[3]:
                v=1
            final_v.append(v)
    for A2 in range(2):
        for B2 in range(2):
            v=0
            if str(A2)==L[1] and str(B2)==L[4]:
                v=1
            final_v.append(v)
    for A2 in range(2):
        for B3 in range(2):
            v=0
            if str(A2)==L[1] and str(B3)==L[5]:
                v=1
            final_v.append(v)
    for A3 in range(2):
        for B1 in range(2):
            v=0
            if str(A3)==L[2] and str(B1)==L[3]:
                v=1
            final_v.append(v)
    for A3 in range(2):
        for B2 in range(2):
            v=0
            if str(A3)==L[2] and str(B2)==L[4]:
                v=1
            final_v.append(v)
    for A3 in range(2):
        for B3 in range(2):
            v=0
            if str(A3)==L[2] and str(B3)==L[5]:
                v=1
            final_v.append(v)
    return final_v

# Main loop
for L in generate_binary_strings(6):
    final_v = generate_final_vector(L)
    #print(L)
    print(final_v)
    #print(len(final_v))
