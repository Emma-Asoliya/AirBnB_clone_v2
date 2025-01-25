def do_create(self, args):
        """ Create an object of any class"""
        try:
            class_name = args.split(" ")[0]
        except IndexError:
            pass
        if not class_name:
            print("** class name missing **")
            return
        elif class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        # create Place city_id="0001" user_id="0001" name="My_little_house"
        all_list = args.split(" ")

        new_instance = eval(class_name)()

        for i in range(1, len(all_list)):
            key, value = tuple(all_list[i].split("="))
            if value.startswith('"'):
                value = value.strip('"').replace("_", " ")
            else:
                try:
                    value = eval(value)
                except Exception:
                    print(f"** couldnt evaluate {value}")
                    pass
            if hasattr(new_instance, key):
                setattr(new_instance, key, value)
            
        storage.new(new_instance)
        print(new_instance.id)
        new_instance.save()
