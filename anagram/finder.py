import sys
import anagram.filereader as reader
from collections import Counter


all_words = reader.read_file('/usr/share/dict/words')
all_words.append('i')
all_words.append('a')
ini_name = input('Введите имя: ')


def find_anagrams(name, word_list):
    name_letter_map = Counter(name)
    anagrams = []
    for word in word_list:
        test = ''
        word_letter_map = Counter(word.lower)
        for letter in word:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test += letter
            if Counter(test) == word_letter_map:
                anagrams.append(word)
    print(*anagrams, sep='\n')


if __name__ == '__main__':
    find_anagrams()
