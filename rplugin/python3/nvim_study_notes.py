import pynvim


@pynvim.plugin
class Note(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command("Hello", nargs="*", range="")
    def hellocommand(self, args, range):
        self.nvim.current_line = f"Comando com args: {args}, range: {range}"
