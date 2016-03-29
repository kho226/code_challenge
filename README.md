# Pangram
python library with tools for determining if a string is an pangram

The sentence "A quick brown fox jumps over the lazy dog" contains every single letter in the 
alphabet. Such sentences are called pangrams. Contains a method called get_missing_letters as will as other variations and returns
a string with all the letters it is missing (which prevent it from being an anagram).

The case of the letters is ignored
The return is all the lower case letters it is missing, in alphabetical order 

Examples:

1) "A quick brown fox jumps over the lazy dog"

Returns: ""

(This sentence contains every letter)

2) "A slow yellow fox crawls under the proactive dog"

Returns: "bjkmqz"

3) "Lions, and tigers, and bears, oh my!"

Returns: "cfjkpquvwxz"

4) ""

Returns: "abcdefghijklmnopqrstuvwxyz"
