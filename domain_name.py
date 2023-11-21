# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python
# Extract the domain name from a URL

# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

    # * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
    # * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
    # * url = "https://www.cnet.com"                -> domain name = cnet"

url = "http://github.com/carbonfive/raygun"
url = "https://www.cnet.com"
# print(url[:8])
# print(url[8])
# url = "http://www.zombie-bites.com"
# url = "www.xakep.ru"
url = "https://youtube.com"
# print(url[7]) # w
# print(url[:12])

# print(url[:4])

# # elif url[:11] == "http://www.":
if url[:7] == "http://" and url[7] == "w":
    print(f"url: {url}")
    # print(url[:11])
    url_prefix = url[:11]
    print(f"url_prefix: {url_prefix}")
    # print(url[11:])
    url_prefix_removed = url[11:]
    print(f"url_prefix_removed: {url_prefix_removed}")
    # print(url[11:].index("."))
    domain = url_prefix_removed[:url_prefix_removed.index(".")]
    print(f"domain: {domain}")

elif url[:7] == "http://":
    print(f"url: {url}")
    # print(url[:7])
    url_prefix = url[:7]
    print(f"url_prefix: {url_prefix}")
    # print(url[7:])
    url_prefix_removed = url[7:]
    print(f"url_prefix_removed: {url_prefix_removed}")
    # print(url[7:].index("."))
    domain = url_prefix_removed[:url_prefix_removed.index(".")]
    print(f"domain: {domain}")

elif url[:4] == "www.":
    print(f"url: {url}")
    # print(url[:7])
    url_prefix = url[:4]
    print(f"url_prefix: {url_prefix}")
    # print(url[7:])
    url_prefix_removed = url[4:]
    print(f"url_prefix_removed: {url_prefix_removed}")
    # print(url[7:].index("."))
    domain = url_prefix_removed[:url_prefix_removed.index(".")]
    print(f"domain: {domain}")
    
elif url[:8] == "https://" and url[8] == "w":
    print(f"url: {url}")
    # print(url[:12])
    url_prefix= url[:12]
    print(f"url_prefix: {url_prefix}")
    # print(url[12:])
    url_prefix_removed = url[12:]
    print(f"url_prefix_removed: {url_prefix_removed}")
    # print(url[12:].index("."))
    domain = url_prefix_removed[:url_prefix_removed.index(".")]
    print(f"domain: {domain}")

elif url[:8] == "https://":
    print(f"url: {url}")
    # print(url[:12])
    url_prefix= url[:8]
    print(f"url_prefix: {url_prefix}")
    # print(url[12:])
    url_prefix_removed = url[8:]
    print(f"url_prefix_removed: {url_prefix_removed}")
    # print(url[12:].index("."))
    domain = url_prefix_removed[:url_prefix_removed.index(".")]
    print(f"domain: {domain}")

# print(url[:7])
# url = len("http://")
# print(f"url {url}") # 7

# url1 = len("http://www.")
# print(f"url1 {url1}") # 11

# url2 = len("https://www.")
# print(f"url2 {url2}") # 12



def domain_name(url):
    domain = ""

    if url[:7] == "http://" and url[7] == "w":
        # print(f"url: {url}")
        # print(url[:11])
        # url_prefix = url[:11]
        # print(f"url_prefix: {url_prefix}")
        # print(url[11:])
        url_prefix_removed = url[11:]
        # print(f"url_prefix_removed: {url_prefix_removed}")
        # print(url[11:].index("."))
        domain = url_prefix_removed[:url_prefix_removed.index(".")]
        # print(f"domain: {domain}")

    elif url[:7] == "http://":
        # print(f"url: {url}")
        # print(url[:7])
        url_prefix = url[:7]
        # print(f"url_prefix: {url_prefix}")
        # print(url[7:])
        url_prefix_removed = url[7:]
        # print(f"url_prefix_removed: {url_prefix_removed}")
        # print(url[7:].index("."))
        domain = url_prefix_removed[:url_prefix_removed.index(".")]
        # print(f"domain: {domain}")

    elif url[:4] == "www.":
        # print(f"url: {url}")
        # print(url[:7])
        # url_prefix = url[:4]
        # print(f"url_prefix: {url_prefix}")
        # print(url[7:])
        url_prefix_removed = url[4:]
        # print(f"url_prefix_removed: {url_prefix_removed}")
        # print(url[7:].index("."))
        domain = url_prefix_removed[:url_prefix_removed.index(".")]
        # print(f"domain: {domain}")
        
    elif url[:8] == "https://" and url[8] == "w":
        # print(f"url: {url}")
        # print(url[:12])
        # url_prefix= url[:12]
        # print(f"url_prefix: {url_prefix}")
        # print(url[12:])
        url_prefix_removed = url[12:]
        # print(f"url_prefix_removed: {url_prefix_removed}")
        # print(url[12:].index("."))
        domain = url_prefix_removed[:url_prefix_removed.index(".")]
        # print(f"domain: {domain}")

    elif url[:8] == "https://":
        # print(f"url: {url}")
        # print(url[:12])
        # url_prefix= url[:8]
        # print(f"url_prefix: {url_prefix}")
        # print(url[12:])
        url_prefix_removed = url[8:]
        # print(f"url_prefix_removed: {url_prefix_removed}")
        # print(url[12:].index("."))
        domain = url_prefix_removed[:url_prefix_removed.index(".")]
        # print(f"domain: {domain}")
    
    return domain

# print(domain_name(url))
# print(domain_name(url1))
# print(domain_name(url2))
print(domain_name(url))