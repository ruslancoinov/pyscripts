import hashlib as hl

# set of all available algorithms in mathlib (these're methods)
print(*hl.algorithms_guaranteed, sep=' ', end='\n\n')
# set of all available algorithms in system, includes openssl
print(*hl.algorithms_available, sep=' ')

# encode in bytes is necessary ('utf-8' as default); hexdigits are for output
hash_object = hl.sha1(('qwerty'.encode()))
print(hash_object.hexdigest())
