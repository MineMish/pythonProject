class Code:
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model
        self.code = "dell C:\Windos\System108 "
class Drawing:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.textures = "64 textures"
class  Game(Drawing, Code):
    def print_info(self):
#        print(self.version)
        print(self.textures)
        print(self.code)

# delleelleel = Game(version ="Last")
# delleelleel.print_info()