import importlib.util, os
path = os.path.join(os.getcwd(),'InnovationProject-main','app.py')
spec = importlib.util.spec_from_file_location('inner_app', path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
app = mod.app
print('app.root_path =', app.root_path)
print('templates dir exists?', os.path.isdir(os.path.join(app.root_path,'templates')))
print('templates listing:', os.listdir(os.path.join(app.root_path,'templates')))
