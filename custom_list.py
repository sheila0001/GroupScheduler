
# removes the busy minutes to find the free minutes.
class CustomList(list): #add a custom method which safely removes an item from the list if it exists. 

    def remove_if_exist(self, v):
        try:
            self.remove(v)

        except ValueError:
            pass
