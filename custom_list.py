

class CustomList(list): #add a custom method which safely removes an item from the list if it exists. 

    def remove_if_exist(self, v):
        try:
            self.remove(v)

        except ValueError:
            print(f"{v} already deleted!")
