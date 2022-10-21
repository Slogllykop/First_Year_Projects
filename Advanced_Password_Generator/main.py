import sys

version = float(f"{sys.version_info.major}.{sys.version_info.minor}")

if version < 3.10:
    raise Exception(f"You have Python {version} installed\nPython 3.10 or a more recent version is required.")

else: 
    from PasswordGenerator import Generator
    import os

    if __name__ == "__main__":

        dimensions = 'mode 50'
        color = 'color 5E'
        os.system(dimensions)
        os.system(color)

        G = Generator()
        G.run()


# TO DO
# check the choices if they are greater than 1
# check if password length is 100<
