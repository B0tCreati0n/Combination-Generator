import itertools
import os

def generate_combinations(input_string):
    characters = []
    for char in input_string:
        if char == '*':
            characters.append('0123456789')
        elif char == '#':
            characters.append('abcdefghijklmnopqrstuvwxyz')
        elif char == '¤':
            characters.append('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        elif char == '!':
            characters.append('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
        elif char == '?':
            characters.append('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
        else:
            characters.append(char)

    combinations = [''.join(combination) for combination in itertools.product(*characters)]
    return combinations

def save_combinations(combinations, location, filename):
    with open(location + '/' + filename, 'w') as file:
        for combination in combinations:
            file.write(combination + '\n')

def get_valid_location():
    while True:
        location = input("Enter the location to save the file: ")
        if not os.path.isdir(location):
            print("Invalid location. Please enter a valid directory.")
        else:
            return location

def get_valid_filename(location):
    while True:
        filename = input("Enter the filename: ")
        if os.path.isfile(os.path.join(location, filename)):
            print("File with the same name already exists.")
            choice = input("Do you want to overwrite the file? (y/n): ")
            if choice.lower() == 'y':
                return filename
        else:
            return filename

def should_proceed(combinations_count):
    if combinations_count > 1000000:
        choice = input("The number of combinations exceeds 1 million. It may take a long time to generate and save all the combinations, it also could fill many megabytes and even one or more gigabytes. Do you want to proceed? (y/n): ")
        if choice.lower() != 'y':
            print("Aborted by the user.")
            exit()

def main():
    input_string = input("Enter the combination pattern (NOTE: For a big pattern, it may take longer to process):\n * for 0-9\n # for a-z\n ¤ for A-Z\n ! for special characters\n ? for numbers, letters, and special characters: ")
    location = get_valid_location()
    filename = get_valid_filename(location)

    combinations = generate_combinations(input_string)
    should_proceed(len(combinations))
    save_combinations(combinations, location, filename)

    print("Combinations generated and saved successfully!")

if __name__ == '__main__':
    main()
