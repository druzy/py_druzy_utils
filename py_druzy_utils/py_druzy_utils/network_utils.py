#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 26 déc. 2015

@author: druzy
'''

from netifaces import interfaces, ifaddresses, AF_INET

def get_local_ip():
    '''renvoie l'ip local comme "192.168.0.19" ou None si non trouvée'''
    res=None
    for inter in interfaces():
        addresses=[i['addr'] for i in ifaddresses(inter).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
        for address in addresses:
            if address.find("127")!=0:
                res=address
                break
        if res is not None:
            break
    return res
            
if __name__=="__main__":
    print(get_local_ip())
        