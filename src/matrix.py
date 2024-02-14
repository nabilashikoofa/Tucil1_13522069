import random
import numpy as np

def generate_random_matrix(width, height):
    matrix = []
    for _ in range(height):
        row = [generate_random_token() for _ in range(width)]
        matrix.append(row)
    return matrix

def generate_random_token():
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choices(characters, k=2))

def read_problem_from_file(filename):
    while True:
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()

            buffer_size = int(lines[0].strip())

            matrix_info = lines[1].strip().split()
            matrix_width = int(matrix_info[0])
            matrix_height = int(matrix_info[1])

            if matrix_width <= 0 or matrix_height <= 0:
                raise ValueError("Ukuran matriks tidak valid.")
        
            matrix = [line.strip().split() for line in lines[2:2 + matrix_height]]
            matrix = [[str(cell) for cell in row] for row in matrix]

            sequences = []
            rewards = []
            
            current_line = 2 + matrix_height

            while current_line < len(lines):
                if lines[current_line].strip().isdigit():
                    num_sequences = int(lines[current_line].strip())
                    current_line += 1  
                    for _ in range(num_sequences):
                        sequence_line = lines[current_line].strip().split()
                        sequence = [cell for cell in sequence_line]
                        sequences.append(sequence)
                        
                        current_line += 1  
                        reward = int(lines[current_line].strip())
                        rewards.append(reward)
                        current_line += 1  
                else:
                    current_line += 1 

            sorted_index = np.argsort(rewards)[::-1]
            sequences = [sequences[i] for i in sorted_index]
            rewards = [rewards[i] for i in sorted_index]

            return buffer_size, matrix, sequences, rewards

        except FileNotFoundError:
            print("File tidak ditemukan.")
            filename = input("Masukkan nama file yang berisi matriks: ")
            continue  
        
        except ValueError as ve:
            print("Terjadi kesalahan:", ve)
            filename = input("Masukkan nama file yang berisi matriks: ")
            continue  

        except Exception as e:
            print("Terjadi kesalahan:", e)
            return None, None, None, None 

def write_solution_to_file(filename, buffer_size, matrix, sequences, rewards, solution, best_sequence, score, execution_time):
    try:
        with open(filename, 'w') as file:
            file.write("Buffer Size:\n")
            file.write(f"{buffer_size}\n\n")
            
            file.write("Matrix:\n")
            for row in matrix:
                file.write(' '.join(row) + '\n')
            file.write("\n")
            
            file.write("Sequences:\n")
            for seq in sequences:
                file.write(' '.join(seq) + '\n')
            file.write("\n")
            
            file.write("Rewards:\n")
            for reward in rewards:
                file.write(f"{reward}\n")
            file.write("\n")
            
            if solution is not None:
                file.write("Solution:\n")
                for pos in solution:
                    file.write(f"{pos}\n")
                file.write("\n")
                file.write(f"Best Sequence:\n")
                file.write(' '.join(best_sequence) + '\n')
                file.write("\n")
                file.write(f"Score: {score}\n")
                file.write("\n")
                file.write(f"Execution Time: {execution_time} ms\n")
            else:
                file.write("Tidak ada solusi yang ditemukan.\n")
        print(f"Solusi disimpan dalam file {filename}")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan solusi: {e}")
