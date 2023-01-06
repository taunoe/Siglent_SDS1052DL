import pyvisa

rm = pyvisa.ResourceManager()
resources = rm.list_resources_info() #dict

for key, values in resources.items():
  for val in values:
    print(key, ":", val)

res = rm.list_resources() #tuple
print(res)