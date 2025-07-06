from src.firewall.command import command
from src.firewall.ui import FirewallUI


class Controller:
    def __init__(self):
        self.ui: FirewallUI

    @command("block")
    async def block_command(self, arg: str):
        self.ui.append_log(f"Applied Block Rule: {arg}")

    @command("allow")
    async def allow_command(self, arg: str):
        self.ui.append_log(f"Applied Allow Rule: {arg}")

    @command("dummy")
    async def send_dummy_command(self, arg: str):
        self.ui.append_log(f"Dummy message")
