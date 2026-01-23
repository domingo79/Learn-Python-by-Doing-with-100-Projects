"""
Creare un programma che produca statistiche diverse su una serie di numeri che l'utente invia nel terminale.
(1) Il programma chiede all'utente di inserire una serie di numeri nel terminale. 
(2) Il programma calcola e stampa diverse statistiche, come il numero di numeri inviati dall'utente, 
la somma, l'intervallo (ovvero la differenza tra il numero più grande e quello più piccolo), frequenza e media.
"""
# Get user input
user_numbers = input("Enter a series of numbers separated by spaces:\n")
# Convert the input to a list of integers
numbers = [int(n) for n in user_numbers.split()]
# Calculate the frequency of each number
total_numbers = len(numbers)
sum_numbers = sum(numbers)
number_range = max(numbers) - min(numbers)
avarage_number = sum_numbers / total_numbers
frequency = {}
for num in numbers:
    if num not in frequency:
        frequency[num] = 1
    else:
        frequency[num] += 1
most_frequent_number = max(frequency, key=frequency.get)

print("Number Analysis Results:")
print("-" * 24)
print(f"Total Numbers: {total_numbers}")
print(f"Sum of Numbers: {sum_numbers}")
print(f"Range of Numbers: {number_range}")
print(
    f"Most Frequent Number: {most_frequent_number} (append {frequency[most_frequent_number]} times)")
print(f"Avarage Number: {avarage_number:.2f}")
