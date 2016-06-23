#!/usr/bin/env python
#script for downloading images from a urls stored at a txt file.
import sys
import getopt
import requests

def load_txt(file_name):
    """
    Read a file line  by line and returns an array of urls
    :param file_name: name of the file to extract urls.
    """
    url_list = []
    try:
        f = open(file_name)
    except IOError as e:
        print("Error reading filename: %s does not exists\n" %e)
        sys.exit()

    next = f.readline()
    while  next != "":
        url_list.append(next.rstrip('\n'))
        next = f.readline()

    return url_list

def  store_url_images(url):
    """
    Request images from URL  in order to download to local
    :param url:  URL  of the resource to  download
    """
    filename =  url.split('/')[-1]
    #url = "https://upload.wikimedia.org/wikipedia/en/d/d8/Url-logo.png"
    try:
        r = requests.get(url, stream=True)
        with open(filename, 'wb') as f:
            print("Data from url %s stored at local\n" %url)
            for chunk in r.iter_content(chunk_size=1024):
                if chunk: # filter out keep-alive new chunk
                    f.write(chunk)
    except requests.exceptions.RequestException as e:
        print("Error getting data from url %s\n" %url)

def main (argv):
    """
    Main function of the script.
    :param arvs: list of arguments
    """
    input_file_text = ""

    try:
        opts, args = getopt.getopt(argv, "i:", ["inputfile="])
    except getopt.GetoptError:
        print("script.py -i <inputfile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("script.py -i <inputfile>")
            sys.exit()
        elif opt in ("-i", "--inputfile"):
            inputfile = arg
            #load plain txt in order to get URLs
            list_url  = load_txt(inputfile)
            #http request data and store data
            for url in list_url:
                store_url_images(url)

if __name__ == "__main__":
    main(sys.argv[1:])
