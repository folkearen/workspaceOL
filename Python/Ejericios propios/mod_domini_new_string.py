def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

print(replace_domain("alan.munoz.b@gmail.com", "gmail.com", "ceinted.cl"))

def replace_domain(email, old_domain, new_domain):
    if  old_domain in email:
        index = email.index(old_domain)
        new_email = email[:index] + new_domain
        return new_email
    return email

print(replace_domain("alan.munoz.b@gmail.com", "gmail.com", "ceinted.cl"))
print(replace_domain("islerkain@gmail.com", "gmail.com", "consultora.cl"))
print(replace_domain("peitopagadoble.hotmail.com", "hotmail.com", "gmail.com"))