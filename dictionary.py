customer= {
    "name" : "John wick",
    "age": 55,
    "is_verified":True
}
customer["name"]="jack smith" #value update thai jashe
print(customer["name"]) #jo key nai hoy to aa error deshe
print(customer.get("birthdat")) #aa none aapshe error nai aape
print(customer.get("birthdate","jan 1 1980")) # aa defult value aapi e print karashe