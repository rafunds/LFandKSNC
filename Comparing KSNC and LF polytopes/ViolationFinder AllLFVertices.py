import numpy as np
from fractions import Fraction

#def read_input_vectors(file_path):
#    with open(file_path, 'r') as file:
#        input_vectors = [list(map(float, line.strip().split())) for line in file if line.strip()]
#    return input_vectors

def read_input_vectors(file_path):
    with open(file_path, 'r') as file:
        input_vectors = []
        for line in file:
            if line.strip():
                # Convert each value, handling fractions like '1/4'
                vector = []
                for item in line.strip().split():
                    if '/' in item:
                        vector.append(float(Fraction(item)))  # Convert fraction to float
                    else:
                        vector.append(float(item))  # Convert directly if not a fraction
                input_vectors.append(vector)
    return input_vectors    

def read_inequalities(file_path):
    with open(file_path, 'r') as file:
        inequalities = file.readlines()
    return inequalities

def extract_functional_and_bound(inequality):
    if '==' in inequality:
        functional, bound = inequality.split('==')
    elif '<=' in inequality:
        functional, bound = inequality.split('<=')
    else:
        raise ValueError("Inequality format not recognized")
    return functional.strip(), float(bound.strip())

def parse_functional(functional):
    H = np.zeros(36)
    terms = functional.replace('-', '+-').split('+')
    for term in terms:
        term = term.strip()
        if term:
            if 'x' in term:
                if term.startswith('x'):  # Case like 'x1'
                    coef = 1
                    var = term[1:]
                elif term.startswith('-x'):  # Case like '-x1'
                    coef = -1
                    var = term[2:]
                else:
                    parts = term.split('x')
                    coef = int(parts[0]) if parts[0] not in ('', '+') else 1
                    coef = -1 if parts[0] == '-' else coef
                    var = parts[1]
                index = int(var) - 1  # Convert to zero-based index
                H[index] = coef
            else:
                H[0] = int(term)  # Handle constant terms if any
    return H

def evaluate_functional(H, X):
    return np.dot(H, X)

def main():
    input_vectors = read_input_vectors('Vrepresentation_Pa.txt')
    inequalities = read_inequalities('LF_Ineq15.txt')
    
    with open('Pa_respects_Ineq15.txt', 'w') as output_file:
        for input_vector in input_vectors:
            violated_any = False
            for inequality in inequalities:
                inequality = inequality.strip()
                if inequality:
                    functional, bound = extract_functional_and_bound(inequality)
                    H = parse_functional(functional)
                    h_value = evaluate_functional(H, input_vector)
                    if h_value > bound:
                        output_file.write(f"This inequality '{functional} <= {bound}' was violated by this input vector {input_vector}\n")
                        violated_any = True
                        break
                    #if h_value == bound:
                    #    output_file.write(f"{input_vector}\n")
                    #    violated_any = True
                    #    break
            if not violated_any:
                output_file.write(f"{input_vector}\n")

if __name__ == "__main__":
    main()
