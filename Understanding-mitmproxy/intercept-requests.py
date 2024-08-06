from mitmproxy import http


class InterceptRequests:
    def __init__(self):
        pass

    def request(self, flow: http.HTTPFlow) -> None:
        # Logging the intercepted URL
        print(f"Intercepting HTTP request to {flow.request.pretty_url}")

        # Logging Original Headers
        print("Original Headers")
        for header, value in flow.request.headers.items():
            print(f"{header}: {value}")

        # Modifying User Agent Header
        print("Modifying User Agent")
        flow.request.headers["user-agent"] = "MyCustomAgent"

        # Logging Modified Headers
        print("Modified Headers")
        for header, value in flow.request.headers.items():
            print(f"{header}: {value}")

        # Blocking Request to a specific domain
        if "youtube.com" in flow.request.pretty_url:
            flow.response = http.Response.make(
                403,
                b"Blocked Request to YouTube",
                {"Content-Type": "text/plain"}
            )
            return  # Stop further processing

        # Redirecting request to a different domain
        if "docs.mitmproxy.org" in flow.request.pretty_url:
            flow.request.host = "youtube.com"
            flow.request.port = 80
            flow.request.scheme = "http"  # Ensure the scheme is set for redirection
            print(f"Redirecting request to {flow.request.pretty_url}")
