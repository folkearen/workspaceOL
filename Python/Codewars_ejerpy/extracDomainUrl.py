"""
Escriba una función que cuando se le da una URL como una cadena, 
analiza solo el nombre de dominio y lo devuelve como una cadena. 
Por ejemplo:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
"""
def domain_name(url):
    if url.startswith("http://"):
        url = url.lstrip("http://")
        return url[:url.index(".")]
    elif url.startswith("https://"):
        url = url.lstrip("https://")
        return url[:url.index(".")]

    elif url.startswith("http://www."):
        url = url.lstrip("http://www.")
        url = url.lstrip(".")
        return url[:url.index(".")]

    elif url.startswith("https://www."):
        url = url.lstrip("https://www.")
        url = url.lstrip(".")
        return url[:url.index(".")]
    elif url.startswith("www."):
        url = url.lstrip("www.")
        url = url.lstrip(".")
        return url[:url.index(".")]
    else:
        return url[:url.index(".")]
  

print(domain_name("http://zombie-bites.com"))