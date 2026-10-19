import os
import signal
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

# Значения берём из переменных окружения.
# Если переменной нет - используем значение по умолчанию.
NAME = os.getenv("STUDENT_NAME", "Bakhtjan")
SURNAME = os.getenv("STUDENT_SURNAME", "Apsatarov")
GROUP = os.getenv("STUDENT_GROUP", "IT2-2314")
STUDENT_ID = os.getenv("STUDENT_ID", "37510")


def build_text():
    return (
        "================================\n"
        "DevOps Student Application\n"
        "================================\n"
        "\n"
        f"Name: {NAME}\n"
        f"Surname: {SURNAME}\n"
        f"Group: {GROUP}\n"
        f"Student ID: {STUDENT_ID}\n"
        "\n"
        "Application is running successfully!\n"
    )


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = build_text().encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def stop(signum, frame):
    # Быстрая остановка контейнера по команде docker stop
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGTERM, stop)
    print(build_text(), flush=True)
    print("Server started on port 8000", flush=True)
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
