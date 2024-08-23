import numpy as np

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
    input_vector = [
            1,   0,   0,   0,
            0.5, 0.5, 0,   0,
            0.5, 0.5, 0,   0,
            0.5, 0,   0.5, 0,
            0,   0.5, 0.5, 0,
            0,   0.5, 0.5, 0,
            0.5, 0,   0.5, 0,
            0.5, 0,   0,   0.5,
            0,   0.5, 0.5, 0
    ]  # Replace with your actual input vector
    inequalities = read_inequalities('IntersectionPolytopeNontrivialInequalitiesOnly.txt')
    
    with open('output_results.txt', 'w') as output_file:
        for inequality in inequalities:
            inequality = inequality.strip()
            if inequality:
                functional, bound = extract_functional_and_bound(inequality)
                H = parse_functional(functional)
                h_value = evaluate_functional(H, input_vector)
                output_file.write(f"h(X) for '{functional}' is {h_value} and the bound is {bound}\n")

if __name__ == "__main__":
    main()


