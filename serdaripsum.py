#!/usr/bin/env python
#-*-coding: utf-8

# Serdar Ipsum Generator

import sys, random, argparse

if __name__ != '__main__':
    print("Not a module!")
    sys.exit(1)

parser = argparse.ArgumentParser(description='To tell me how many verses')
parser.add_argument('length', type=int, help='Verses count to generate')
args = parser.parse_args()

PLENGTH = args.length
song_file = "songs.txt"
MIN_WORDS_PER_LINE = 3
MAX_WORDS_PER_LINE = 6
words = []

with open(song_file) as f:
    lines = f.readlines()

for line in lines:
    line = line.replace("\n", "")
    if line != "-----":
        words_per_line = line.split(' ')
        for word in words_per_line:
            word.replace("\n", "")
            words.append(word.lower())


def generate_a_line():
    random_line_length = random.randint(MIN_WORDS_PER_LINE, MAX_WORDS_PER_LINE)
    song_line = ""
    for i in range(0, random_line_length):
        random_word = random.randint(0, len(words) - 1)
        song_line += words[random_word] + " "
    return song_line[:1].upper() + song_line[1:]


def generate_verse():
    for i in range(0, 4):
        print(generate_a_line())
    print(" ")


def generate_song():
    for i in range(0, PLENGTH):
        generate_verse()


def song_title():
    title = words[random.randint(0, len(words) - 1)] + " " + words[random.randint(0, len(words) - 1)] + " " + words[random.randint(0, len(words) - 1)]
    return title.upper()


print(">> Serdar Ipsum Generator\n")
print(song_title() + "\n")
generate_song()
print(" - Serdar Ortaç\n")