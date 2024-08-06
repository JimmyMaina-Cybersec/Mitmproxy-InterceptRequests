from mitmproxy import http


class InterceptpRequests:
    def __inti__(self):
        pass

    def request(flow: http.HTTPFlow) -> None:
        # logging the intercepted url
        print(f"Intercepting http request from {flow.request.pretty_url}")

        # Logging Original Headers
        print("Original Headers")
        for header, value in flow.request.headers.items():
            print(f"{header}: {value}")

        # Modifying User Agent Header
        print("Modifying User Agent")
        flow.request.headers["User-Agent"] = "MyCustomAgent"

        # Logging Modified Headers
        for header, value in flow.request.headers.items():
            print(f"{header}: {value}")

        # Blocking Request to a specific domain
        if "youtube.com" in flow.request.host:
            flow.response = flow.Response.make(
                403,
                b"Blocked Request to YouTube",
                {"Content-Type": "text/plain"}
            )

        # Redirecting request to a different domain
        if "docs.mitmproxy.org/stable/mitmproxytutorial-interceptrequests/" in flow.request.host:
            flow.request.host = "youtube.com/watch?v=z5XdX_ryHoc"
            flow.request.port = 80
