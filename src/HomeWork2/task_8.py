""" Codewars 4Ku
Write a function called sumIntervals/sum_intervals()
that accepts an array of intervals, and returns the sum of all the interval lengths.
Overlapping intervals should only be counted once.
Intervals
Intervals are represented by a pair of integers in the form of an array.
The first value of the interval will always be less than the second value.
Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.
Overlapping Intervals
List containing overlapping intervals:
[   [1,4],   [7, 10],   [3, 5]]
The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap,
we can treat the interval as [1, 5], which has a length of 4."""


def sum_of_intervals(intervals):
    list_in = []
    for x in intervals:
        for y in range(x[0], max(x)):  # max элемент всего списка, как крайний, на сколько помню
            if [y, y + 1] not in list_in:
                list_in.append([y, y + 1])
    return len(list_in)


""" Codewars 6Ku
Is similar to factorial of a number, In primorial, not all the natural numbers get multiplied,
only prime numbers are multiplied to calculate the primorial of a number.
It's denoted with P# and it is the product of the first n prime numbers.
Task: Given a number N , calculate its primorial.
Notes: Only positive numbers will be passed (N > 0) .
Input >> Output Examples: 1- numPrimorial (3) ==> return (30)
Explanation: Since the passed number is (3) ,
Then the primorial should obtained by multiplying 2 * 3 * 5 = 30 ."""


def num_primorial(n):
    sieve = list(range(n * n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    sieve = [x for x in sieve if x != 0]
    c = 1
    for i in range(n):
        c *= sieve[i]
    return c


""" Codewars 4Ku
There is a secret string which is unknown to you.
Given a collection of random triplets from the string, recover the original string.
A triplet here is defined as a sequence of three letters such
that each letter occurs somewhere before the next in the given string.
"whi" is a triplet for the string "whatisup".
As a simplification, you may assume that no letter occurs more than once in the secret string.
You can assume nothing about the triplets given to you other than that
they are valid triplets and that they contain sufficient information
to deduce the original string.
In particular, this means that the secret string will never contain letters
that do not occur in one of the triplets given to you."""


def recover_Secret(triplets):
    sec = list({n for row in triplets for n in row})
    sort_word(triplets, sec)
    return "".join(sec)


def sort_word(tr, sw):
    flag = False
    if flag:
        return sw
    for i in range(len(tr)):
        for x in range(3):
            for y in range(x + 1, 3):
                if sw.index(tr[i][x]) > sw.index(tr[i][y]):
                    sw[sw.index(tr[i][x])], sw[sw.index(tr[i][y])] = \
                        sw[sw.index(tr[i][y])], sw[sw.index(tr[i][x])]
                    flag = False
                    return sort_word(tr, sw)


""" Codewars 6Ku
Polycarpus works as a DJ in the best Berland nightclub,
and he often uses dubstep music in his performance. Recently,
he has decided to take a couple of old songs and make dubstep remixes from them.
Let's assume that a song consists of some number of words (that don't contain WUB).
To make the dubstep remix of this song, Polycarpus inserts a certain
number of words "WUB" before the first word of the song (the number may be zero),
after the last word (the number may be zero), and between words
(at least one between any pair of neighbouring words),
and then the boy glues together all the words, including "WUB",
in one string and plays the song at the club.
For example, a song with words "I AM X" can transform into a dubstep remix
as "WUBWUBIWUBAMWUBWUBX" and cannot transform into "WUBWUBIAMWUBX".
Recently, Jonny has heard Polycarpus's new dubstep track,
but since he isn't into modern music, he decided to find out what was the initial
song that Polycarpus remixed. Help Jonny restore the original song"""


def song_decoder(song):
    return " ".join(song.replace("WUB", " ").split())


""" Codewars 7Ku
Your task is to make a function that can take any non-negative integer as an argument
and return it with its digits in descending order.
Essentially, rearrange the digits to create the highest possible number.
Examples: Input: 42145 Output: 54421
Input: 145263 Output: 654321
Input: 123456789 Output: 987654321
"""


def Descending_Order(num):
    return int(''.join(sorted(str(num))[::-1]))


print(Descending_Order(1529543))
