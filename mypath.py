# -*- encoding: utf-8 -*-
## every item define -- index name level

A1item = ["thought", "appledaily", "system", "network", "security",
"DevOps", "program", "life", "knowledge", "hobby"]
A1B1item = ["web-server", "apache", "nginx"]
A1B2item = ["web-lang", "php", "php-laravel"]
A1B3item = ["sql-server", "mysql", "mongodb"]
item = {}
i = 1
for x in A1item:
   item [x] = str(i)
   i += 1

for x in A1B1item:
    item[x] = "001_00100"

for key, value in item.items():
    a,b,c = (value.split('_') + [None]*3)[:3]
    if b is None:
        print("%03d_%s" % (int(a),key))
    elif c is None:
        print("    %05d_%s" % (int(b),key))
#        print("\t%05d_%s" % (int(a),int(b),key))
    

