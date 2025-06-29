import asyncio

from mitmproxy import http
from mitmproxy.options import Options
from mitmproxy.tools.dump import DumpMaster

BLOCKED_DOMAINS = ["example.com", "www.google.com", "www.youtube.com", "www.acmicpc.net"]
class DomainBlock:
    def request(self, flow: http.HTTPFlow) -> None:
        host = flow.request.pretty_host
        if host in BLOCKED_DOMAINS:
            flow.response = http.Response.make(
                403,
                b"<h1>Access Denied Blocked Domain</h1>"
                b"<img src='https://http.cat/403'>",
                {"Content-Type": "text/html"}
            )
        print(f"[Blocked] {host}")

async def start_proxy():
    options = Options(listen_host="127.0.0.1", listen_port=8080)
    master = DumpMaster(options, with_termlog=False, with_dumper=False)
    master.addons.add(DomainBlock())

    print(f"[INFO] MITMProxy is running (Port: 8080)")

    try:
        await master.run()
    except KeyboardInterrupt:
        await master.shutdown()

asyncio.run(start_proxy())