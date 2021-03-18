import sys, getopt, io, re
import requests, logging, time
import json, csv

from .class_tracker import My_DcTracker_Class
from .func_arg import my_argument_function

def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))

    for arg in args:
        print('passed argument :: {}'.format(arg))

    argu = my_argument_function(sys.argv[1:])

    my_object = My_DcTracker_Class(argu)
    my_dict = my_object.get_request()
    my_keys = my_object.get_tempK(my_dict)
    my_celsius = my_object.set_tempC(my_keys)
    my_time = my_object.set_time(my_dict)
    my_data = my_object.set_matplot(my_celsius, my_time)

if __name__ == '__main__':
    main()


