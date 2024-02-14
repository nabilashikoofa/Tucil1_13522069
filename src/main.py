import os
import sys
from solver import find_solution_brute_force, find_token_recursive, find_token, validate_hexdump, text_to_sequence   
from matrix import generate_random_matrix, generate_random_token, read_problem_from_file, write_solution_to_file

def main():
    option = input("Pilih mode:\n1. File TXT - membaca sebuah berkas ber-ekstensi .txt \n2. Mode CLI - matriks dan sekuens diberikan secara acak oleh generator \nPilih mode (1/2): ")

    if option == "1":
        filename = input("Masukkan nama file yang berisi matriks: ")
        file_path = os.path.join("test/", filename)

        buffer_size, matrix, sequences, rewards = read_problem_from_file(file_path)
        if buffer_size is not None:

            best_solution, best_sequence, score, execution_time = find_solution_brute_force(matrix, sequences, rewards)
            if best_solution is not None:
                print("\nReward:", score)
                print("\nSequence:", best_sequence)
                print("Solution:", best_solution)
                
                print("\nExecution Time:", execution_time, "ms\n")
                
                optionFile = input("Apakah ingin menyimpan solusi? (y/n)? ")
                if optionFile == "y":
                    output_filename = input("Masukkan nama file untuk menyimpan solusi: ")
                    if not output_filename or " " in output_filename:
                        print("Nama file tidak boleh kosong atau hanya berisi spasi.")
                        return
                    output_file_path = os.path.join("test/output/", output_filename)
                    write_solution_to_file(output_file_path, buffer_size, matrix, sequences, rewards, best_solution, best_sequence, score, execution_time)
                    
            else:
                print("Tidak ada solusi yang ditemukan.")
        else:
            print("Gagal membaca file.")

    elif option == "2":
        while True:
            matrix_width = int(input("Masukkan lebar matriks: "))
            if matrix_width > 0:
                break
            print("Lebar matriks harus lebih besar dari nol.")

        while True:
            matrix_height = int(input("Masukkan tinggi matriks: "))
            if matrix_height > 0:
                break
            print("Tinggi matriks harus lebih besar dari nol.")

        buffer_size = int(input("Masukkan ukuran buffer: "))
        if buffer_size <= 0:
            print("Ukuran buffer harus lebih besar dari nol.")
            return

        num_sequences = int(input("Masukkan jumlah sequences: "))
        if num_sequences <= 0:
            print("Jumlah sequences harus lebih besar dari nol.")
            return

        matrix = generate_random_matrix(matrix_width, matrix_height)

        sequences = []
        rewards = []
        for i in range(num_sequences):
            sequence = input(f"Masukkan sequence ke-{i + 1}: ")
            sequence = sequence.replace(' ', '')
            if not all(c in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in sequence):
                print("Sequence hanya boleh berisi angka dan huruf hexadecimal.")
                return
            sequences.append(sequence)
            reward = int(input(f"Masukkan reward untuk sequence ke-{i + 1}: "))
            rewards.append(reward)

        best_solution, best_sequence, score, execution_time = find_solution_brute_force(matrix, sequences, rewards)
        if best_solution is not None:
            print("\nReward:", score)
            print("\nSequence:", best_sequence)
            print("Solution:", best_solution)
                            
            print("\nExecution Time:", execution_time, "ms\n")
                
            optionFile = input("Apakah ingin menyimpan solusi? (y/n)? ")
            if optionFile == "y":
                output_filename = input("Masukkan nama file untuk menyimpan solusi: ")
                if not output_filename or " " in output_filename:
                    print("Nama file tidak boleh kosong atau hanya berisi spasi.")
                    return
                output_file_path = os.path.join("test/output/", output_filename)
                write_solution_to_file(output_file_path, buffer_size, matrix, sequences, rewards, best_solution, best_sequence, score, execution_time)
                    
        
        if best_solution is not None:
            print("Solution:", best_solution)
            print("Score:", score)

            output_filename = input("Masukkan nama file untuk menyimpan solusi: ")
            if not output_filename or " " in output_filename:
                print("Nama file tidak boleh kosong atau hanya berisi spasi.")
                return

            output_file_path = os.path.join("test/output/", output_filename)
            if not os.path.exists("test/output/"):
                os.makedirs("test/output/")

            write_solution_to_file(output_file_path, buffer_size, matrix, sequences, rewards, best_solution, best_sequence, score, execution_time)

        else:
            print("Tidak ada solusi yang ditemukan.")
    else:
        print("Opsi tidak valid.")

if __name__ == "__main__":
    main()
