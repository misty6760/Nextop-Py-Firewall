import asyncio

from mitmproxy import options
from mitmproxy.http import HTTPFlow
from mitmproxy.tools.dump import DumpMaster

class URLCapture:
    def request(self, flow: HTTPFlow) -> None:
        print(f"[URL] {flow.request.pretty_url}")


async def start_proxy():
    opts = options.Options(listen_host="127.0.0.1", listen_port=8080)
    master = DumpMaster(opts)
    master.addons.add(URLCapture())

    print(f"[INFO] MITMProxy is running (Port: 8080)")
    try:
        await master.run()
    except KeyboardInterrupt:
        await master.shutdown()


asyncio.run(start_proxy())
