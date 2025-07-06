import asyncio

from src.firewall.controller import Controller
from src.firewall.ui import FirewallUI


class App:
    async def run(self):
        controller = Controller()
        ui = FirewallUI(controller)
        asyncio.create_task(ui.run_async())

        await asyncio.Event().wait()


if __name__ == "__main__":
    app = App()
    asyncio.run(app.run())
