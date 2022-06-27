def details(*dela):
    print("Name :",dela[0]["name"])
    print("address :",dela[0]["address"])
    print("Phone :"+dela[0]["phon"])
    print("age :"+str(dela[0]["age"]))



values={
    "name":"Thanseer",
    "address" : "valuparabu",
    "phon":"123335",
    "age":24
}   

details(values)