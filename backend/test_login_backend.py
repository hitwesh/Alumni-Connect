import importlib.util, os
path = os.path.join(os.path.dirname(__file__), 'app.py')
spec = importlib.util.spec_from_file_location('backend_app', path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
app = mod.app

c = app.test_client()
# try known user
email = 'hiteshroy2005@gmail.com'
password = 'abcd1234'
resp = c.post('/login', data={'email': email, 'password': password}, follow_redirects=True)
print('status', resp.status_code)
print(resp.data.decode()[:800])
