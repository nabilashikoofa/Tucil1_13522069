import time
import random
import numpy as np

def find_solution_brute_force(matrix, sequences, rewards):
    best_solution = None
    best_sequence = None
    best_score = 0 
    start_time = time.time()
    execution_time = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            for seq_index, sequence in enumerate(sequences):
                if matrix[i][j] == sequence[0]:

                    solution = find_token(matrix, sequences, sequence)
                    if solution:
                        reward = sum(sequences[seq_index].count(matrix[pos[0]][pos[1]]) * rewards[seq_index] for pos in solution)
                        if reward > best_score:
                            best_solution = solution
                            best_sequence = sequence 
                            best_score = reward 
    
    end_time = time.time() 
    execution_time = end_time - start_time
    execution_time = round(execution_time, 5)

    return best_solution, best_sequence, best_score, execution_time

def find_token_recursive(matrix, sequences, current_sequence, current_index, current_position, visited, current_token_index):
    if current_index == len(current_sequence):
        return [current_position]

    row, col = current_position
    next_token = current_sequence[current_token_index]

    # Implementasi untuk arah atas
    if (row + 1 < len(matrix) and matrix[row + 1][col] == next_token and (row + 1, col) not in visited):
        result = find_token_recursive(matrix, sequences, current_sequence, current_index + 1, (row + 1, col), visited + [(row + 1, col)], current_token_index + 1)
        if result:
            return [(row, col)] + result

    # Implementasi untuk arah kanan
    if (col + 1 < len(matrix[0]) and matrix[row][col + 1] == next_token and (row, col + 1) not in visited):
        result = find_token_recursive(matrix, sequences, current_sequence, current_index + 1, (row, col + 1), visited + [(row, col + 1)], current_token_index + 1)
        if result:
            return [(row, col)] + result

    # Implementasi untuk arah kiri
    if (col - 1 >= 0 and matrix[row][col - 1] == next_token and (row, col - 1) not in visited):
        result = find_token_recursive(matrix, sequences, current_sequence, current_index + 1, (row, col - 1), visited + [(row, col - 1)], current_token_index + 1)
        if result:
            return [(row, col)] + result

    # Implementasi untuk arah atas
    if (row - 1 >= 0 and matrix[row - 1][col] == next_token and (row - 1, col) not in visited):
        result = find_token_recursive(matrix, sequences, current_sequence, current_index + 1, (row - 1, col), visited + [(row - 1, col)], current_token_index + 1)
        if result:
            return [(row, col)] + result

    return None

def find_token(matrix, sequences, current_sequence):

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == current_sequence[0]:

                result = find_token_recursive(matrix, sequences, current_sequence, 1, (i, j), [(i, j)], 0)
                if result:
                    return result
    return None

def validate_hexdump(hexdump):
    # Fungsi untuk mengecek apakah semua elemen hexdump adalah string yang valid
    for row in hexdump:
        for token in row:
            if not isinstance(token, str) or len(token) != 2 or not token.isalnum():
                raise ValueError(f"Setiap token harus terdiri dari dua karakter alfanumerik")

def text_to_sequence(text):
    sequences = []
    current_sequence = ""

    for char in text:
        if char.isalnum():
            current_sequence += char

        else:
            if current_sequence:
                sequences.append(current_sequence)
                current_sequence = ""

    # Tambahkan urutan terakhir ke daftar sekuens jika tidak kosong
    if current_sequence:
        sequences.append(current_sequence)

    return sequences

