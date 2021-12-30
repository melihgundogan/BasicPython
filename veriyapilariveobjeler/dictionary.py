#key - value bir bilgiye ulaşmak için kullanılır 34 istanbul gibi 41 kocaeli gibi

#sehirler= ["kocaeli","istanbul"]
#plakalar=[41,34]

#print(plakalar[sehirler.index("kocaeli")])

#print(plakalar["kocaeli"]) =>41 olmasını istiyoruz

#plakalar= {"kocaeli": 41, "istanbul": 34}

#print(plakalar["kocaeli"])

#plakalar["ankara"] = 6
#plakalar["kocaeli"] = "new value"

#print(plakalar)

users ={
    "melihgündoğan": {
        "rolles": ["user"],
        "age":21,
        "email": "assa@gmail.com",
        "adrees": "kocaeli",
        "phone": "1231321"
    },    
    "ahmedgündoğan": {
        "rolles": ["admin","user"],
        "age":11,
        "email": "asa@gmail.com",
        "adrees": "kocaeli",
        "phone": "1231343"
    }
}        
print(users["ahmedgündoğan"])
print(users["ahmedgündoğan"]["age"])
print(users["ahmedgündoğan"]["phone"])
print(users["ahmedgündoğan"]["adrees"])
print(users["ahmedgündoğan"]["email"])