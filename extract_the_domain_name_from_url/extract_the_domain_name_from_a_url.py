# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python
# Extract the domain name from a URL

# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

    # * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
    # * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
    # * url = "https://www.cnet.com"                -> domain name = cnet"
def domain_name(url):
    domain = ""
    
    print(f"Input url => {url}")

    if url[:7] == "http://" and url[9] == "w":
        url_prefix_removed = url[11:]
        domain = url_prefix_removed[:url_prefix_removed.index(".")]

    elif url[:7] == "http://":
        url_prefix = url[:7]
        url_prefix_removed = url[7:]
        domain = url_prefix_removed[:url_prefix_removed.index(".")]


    elif url[:4] == "www.":
        url_prefix_removed = url[4:]
        domain = url_prefix_removed[:url_prefix_removed.index(".")]
        
    elif url[:8] == "https://" and url[8] == "w":
        url_prefix_removed = url[12:]
        domain = url_prefix_removed[:url_prefix_removed.index(".")]

    elif url[:8] == "https://":
        url_prefix_removed = url[8:]
        domain = url_prefix_removed[:url_prefix_removed.index(".")]
    
    else:
        domain = url[:url.index(".")]
        
    print(f"Output => {domain}")
    return domain

# print(domain_name(url))
# print(domain_name(url1))
# print(domain_name(url2))
# print(domain_name(url))
# print(domain_name("icann.org"))
print(domain_name("http://w80fd5s08d6.org"))