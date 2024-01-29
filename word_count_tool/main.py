import sys
import string
import argparse
import os  

def word_count(filename):
    """
    Count the occurrences of each word in a file and return a sorted dictionary.

    Args:
    filename (str): The path to the text file.

    Returns:
    dict: A sorted dictionary of word counts.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read().lower()
            content = content.translate(str.maketrans("", "", string.punctuation))
            words = content.split()

        word_count_dict = {}
        for word in words:
            word_count_dict[word] = word_count_dict.get(word, 0) + 1

        return dict(sorted(word_count_dict.items(), key=lambda item: item[1], reverse=True))
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description='Word Count Script')
    parser.add_argument('input_file', type=str, help='The filename of the text file')
    args = parser.parse_args()

    # Combine the current directory with the provided input_file
    input_file_path = os.path.join(os.getcwd(), args.input_file)

    result = word_count(input_file_path)
    if isinstance(result, dict):
        for word, count in result.items():
            print(f"{word}: {count}")
    else:
        print(result)

if __name__ == "__main__":
    main()
