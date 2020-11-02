import urllib.request


def total_size(url):      
    try:
        response = urllib.request.urlopen(url)      #opening url
        try:
            r = response.read()
            size= len(r)/1024                       # size in KB
            return size
        except:
            print('Denied')
            return 'N/A'
    
    except:
        print('Denied')
        return 'N/A'                               # return 'N/A' if url blocks or take immense time


#a = total_size('https://www.exeterpremedia.com/')
#print(a)