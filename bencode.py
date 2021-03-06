#!/usr/bin/env python 2.7

"""This is a proof of concept of 1 piece of a BitTorrent Client
    For Next Version: Allow user input & graceful Error Handling
"""
from __future__ import print_function

text = "text"
num = 42
user_list = ["luna", "friend"]
user_dict = {"cow":"moo", "spam":"eggs"}

enc_str = "4:spam"
enc_int = "143e"
enc_list = "l4:luna6:friende"
enc_dict = "d3:cow3:moo4:spam4:eggs4:test5:testae"


def ben_str(text):
    print('Bencoding "Text"')
    length = str(len(text))
    data = '{0}:{1}'.format(length, text)
    # data = str(length + ":" + text)
    print("Bencoded: " + data + "\n")
    return data

def ben_int(num):
    print('Bencoding 42 ')
    data = 'i{0}e'.format(num) #See if this will work
    # data = str("i" + str(num) + "e") #Comment this out
    # print('Bencoded: i', num,'e' + "\n")
    print('Bencoded: ' + data + "\n")
    return data    

def ben_list(user_list):
    print('Bencoding ["luna", "friend"] ')
    tmp_list = ["l"]
    for i in user_list:
        length = len(i)
        tmp_list.append(str(length) + ":" + str(i))
    tmp_list.append("e")
    new = ''.join(tmp_list)
    print('Bencoded ' + new + "\n")
    return new

def ben_dict(user_dict):
    print('Bencoding {"cow":"moo", "spam":"eggs"} ')
    tmp_list = ["d"]
    for i in user_dict:
        length = len(i)
        length2 = len(user_dict[i])

        tmp_list.append(str(length) + ":" + str(i) + str(length2) + ":" + str(user_dict[i]))
    tmp_list.append("e")

    new = ''.join(tmp_list)
    print('Bencoded: ' + new + "\n")
    return new

def dec_str(enc_str):
    print('Decoding "4:spam" ')
    new = ''.join(i for i in enc_str if i.isalpha())
    print('Decoded: ' + new + "\n")    
    return new

def dec_int(enc_int):
    print('Decoding "143e" ')
    new = ''.join(i for i in enc_int if i.isdigit())
    print('Decoded: ' + new + "\n")
    return int(new)

def dec_list(enc_list):
    print('Decoding "l4:luna6:friende" ')
    enc_list = enc_list[1:-1]
    new = ''.join(i for i in enc_list if not i.isdigit())
    new = new[1:]
    new = new.replace(":", ",")
    new_list = new.split(",") 
    new2 = new.replace(",", ", ")
    print("Decoded: [" + new2 + "]" + "\n") 
    return new_list 
    
def dec_dict(enc_dict):
    print('Decoding "d3:cow3:moo4:spam4:eggs4:test5:testae" ')
    enc_dict = enc_dict[1:-1]
    new = ''.join(i for i in enc_dict if not i.isdigit())
    new = new[1:] 
    new_list = new.split(":")
    new_dict = dict(zip(new_list[0::2], new_list[1::2]))
    new2 = str(new_dict)
    print('Decoded: ' + new2 + "\n")
    return new_dict


if __name__ == "__main__":
    print("\n" + "Bencoding is an Encoding Method used in BitTorrent")
    print("Here is a demo: \n \n")

    print("-------BENCODING SECTION------ \n")

    ben_str(text)
    ben_int(num)
    ben_list(user_list)
    ben_dict(user_dict)
    
    print("------DECODING SECTION------ \n")

    dec_str(enc_str)
    dec_int(enc_int)
    dec_list(enc_list)
    dec_dict(enc_dict)

    print(" \n------END------ \n")
    print("Thanks so much for checking out this Bencoding Demo")
    print("Have a Nice Day!!! :)")