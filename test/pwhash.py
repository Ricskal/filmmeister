from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
hash = generate_password_hash('test')
print(hash)

print(check_password_hash(hash, 'test'))
print(check_password_hash(hash, 'test2'))