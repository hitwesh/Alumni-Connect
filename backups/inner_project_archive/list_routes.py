from app import app
for rule in sorted(app.url_map.iter_rules(), key=lambda r: r.rule):
    print(rule.rule, sorted(rule.methods))
