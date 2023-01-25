class UserClass:
  full_name = " "
  email = " "
  __password__ = " "
  mobile_number = " "
  def __init__(self, name, email, password):
    self.full_name = new_name
    self.email = email
    self.__password = password
    
  def update_name(self, new_name):
    self.full_name = new_name
  def  get_name(self):
    return self.full_name
  """ Setter method for private variable passsword """
  def update_password(self, new_number):
    self.mobile_number = new_number
  """ getter method for private variable password"""
  def get_user_password(self):
    return self.__password
    
  