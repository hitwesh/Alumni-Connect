import importlib.util
import os

inner_app_path = os.path.join(os.getcwd(), 'InnovationProject-main', 'app.py')
spec = importlib.util.spec_from_file_location('inner_app', inner_app_path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
app = mod.app

c = app.test_client()
# register a test user
resp = c.post('/register', data={'name':'Inner Test','email':'innertest@example.com','password':'pwd','role':'student'}, follow_redirects=True)
print('register status', resp.status_code)
# login
resp2 = c.post('/login', data={'email':'innertest@example.com','password':'pwd'}, follow_redirects=True)
print('login status', resp2.status_code)
print(resp2.data.decode()[:500])
