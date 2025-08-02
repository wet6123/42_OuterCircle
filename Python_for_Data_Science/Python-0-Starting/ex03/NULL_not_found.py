def NULL_not_found(object: any) -> int:
  object_type = type(object)
  if object_type == type(None):
    print(f"Nothing: None {object_type}")
  elif object_type == float and object != object:
    print(f"Cheese: nan {object_type}")
  elif object_type == int and object == 0:
    print(f"Zero: 0 {object_type}")
  elif object_type == str and object == "":
    print(f"Empty: {object_type}")
  elif object_type == bool and object is False:
    print(f"Fake: False {object_type}")
  else: 
    print("Type not Found")
    return 1
  return 0
