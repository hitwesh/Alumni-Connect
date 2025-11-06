import importlib.util
import os

backend_app_path = os.path.join(os.path.dirname(__file__), 'app.py')
spec = importlib.util.spec_from_file_location('backend_app', backend_app_path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
app = mod.app

c = app.test_client()
resp = c.post('/register', data={'name':'Unit Test','email':'unittest@example.com','password':'pwd','role':'student'}, follow_redirects=True)
print('register status', resp.status_code)
print('register len', len(resp.data))
# try login
resp2 = c.post('/login', data={'email':'unittest@example.com','password':'pwd'}, follow_redirects=True)
print('login status', resp2.status_code)
print(resp2.data.decode()[:800])
