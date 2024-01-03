# https://www.codewars.com/kata/51f2b4448cadf20ed0000386/train/python


def remove_url_anchor(url):
    # TODO: complete
    if "#" in url:    
        anchor_index = url.index("#")
        return url[:anchor_index]
    return url