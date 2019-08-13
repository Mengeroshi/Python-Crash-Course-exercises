from admin import Admin

sudox = Admin("Xavier", "saviñon", 21)
sudox.priv.privileges = ["can add post", "can delete post", "can ban user"]

sudox.priv.show_privileges()