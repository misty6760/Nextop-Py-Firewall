from __future__ import annotations

import asyncio
from datetime import datetime

from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Input, Static

from src.firewall.command import executeCommand


class FirewallUI(App):
    QUIT_BINDINGS = ["q", "quit", "Quit"]

    _instance: FirewallUI | None = None

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.controller.ui = self
        self.log_container = Vertical()
        self.command_input = Input(placeholder="Enter Command...")
        self.mounted = asyncio.Event()

    @classmethod
    def instance(cls) -> FirewallUI:
        if cls._instance is None:
            raise RuntimeError("FirewallUI instance is not generated yet.")
        return cls._instance

    def compose(self) -> ComposeResult:
        yield self.log_container
        yield self.command_input

    def on_mount(self) -> None:
        self.command_input.focus()
        self.mounted.set()

    ########################################################################################

    async def on_input_submitted(self, message: Input.Submitted) -> None:
        cmd = message.value.strip()
        self.command_input.value = ""
        if cmd:
            self.append_log(f"> {cmd}")
            await executeCommand(cmd, self.controller)

    def append_log(
        self,
        message: str,
        now: datetime = None,
    ) -> None:
        if now is None:
            now = datetime.now()
        timestamp = str(now)[11:]
        log_line = Static(f"[{timestamp}] {message}")
        self.log_container.mount(log_line)
        self.log_container.scroll_end(animate=False)

    def generate_dummy_message(self):
        self.append_log("Dummy message")


def process_command(cmd: str) -> str:
    match cmd:
        case cmd if cmd.startswith("block"):
            return f"Blocking Rule Applied: {cmd}"
        case cmd if cmd.startswith("allow"):
            return f"Allowing Rule Applied: {cmd}"
        case cmd if cmd.startswith("cls"):
            return "Clearing logs..."
        case _:
            return f"Unknown command: {cmd}"
