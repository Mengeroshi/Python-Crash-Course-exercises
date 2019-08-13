from  user  import Admin

sudo = Admin("Xavier", "saviñon", 21)
sudo.priv.privileges = ["can add post", "can delete post", "can ban user"]

sudo.priv.show_privileges()