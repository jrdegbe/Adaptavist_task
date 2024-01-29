## Word Count Tool ##

Overview
The Word Count Tool is a Python script designed to count the occurrences of each word in a text file. It outputs a sorted list of words and their corresponding counts, with the most frequent words first. This tool is particularly useful for analyzing text data, identifying common patterns in word usage, and general text processing tasks.

Features
- Case Insensitive Counting: Counts words regardless of their case (upper/lower).
- Punctuation Handling: Ignores punctuation, ensuring accurate word counts.
- Sorting by Frequency: Outputs words sorted by their frequency in descending order.
- Command-Line Interface: Easy to use with a simple command-line interface.

Dependencies
- This script uses Python's standard libraries, so no additional installations are required. It's compatible with Python 3.x.

Installation
- No installation is required. Simply clone or download this repository to your local machine.

Usage
- To use the Word Count Tool, run the script from the command line, passing the path to your text file as an argument:

python main.py example.txt

Example
- Given a file example.txt with the following content:


Running the script will produce:
python main.py example.txt
et: 6
eget: 5
in: 5
neque: 4
tortor: 4
eu: 4
id: 4
pellentesque: 4
at: 4
tempor: 3
ut: 3
non: 3
sodales: 3
arcu: 3
donec: 3
tellus: 3
nunc: 3
vitae: 3
urna: 3
nec: 3
semper: 3
ipsum: 2
dolor: 2
sit: 2
amet: 2
adipiscing: 2
sed: 2
magna: 2
ac: 2
mi: 2
ultrices: 2
vel: 2
eros: 2
metus: 2
vulputate: 2
scelerisque: 2
felis: 2
venenatis: 2
nisl: 2
morbi: 2
tempus: 2
quam: 2
risus: 2
quis: 2
tincidunt: 2
viverra: 2
lorem: 1
consectetur: 1
elit: 1
do: 1
eiusmod: 1
incididunt: 1
labore: 1
dolore: 1
aliqua: 1
gravida: 1
dignissim: 1
convallis: 1
aenean: 1
ultricies: 1
mauris: 1
pharetra: 1
odio: 1
orci: 1
volutpat: 1
diam: 1
faucibus: 1
luctus: 1
lectus: 1
fringilla: 1
habitant: 1
tristique: 1
senectus: 1
netus: 1
lobortis: 1
nam: 1
aliquam: 1
sem: 1
consequat: 1
porta: 1
lacinia: 1
velit: 1
laoreet: 1
feugiat: 1
fermentum: 1
posuere: 1
mollis: 1
duis: 1
condimentum: 1
mattis: 1
egestas: 1
purus: 1
accumsan: 1
nisi: 1
a: 1
cras: 1
auctor: 1

Testing
- Unit tests are located in the same word_count_tool/ directory. Run them to ensure the tool's reliability using:

python -m unittest test_main