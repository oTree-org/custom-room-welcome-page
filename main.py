from pathlib import Path
from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route


def homepage(request):
    html = Path('RoomInputLabel.html').read_text('utf8')
    return HTMLResponse(html)


app = Starlette(debug=True, routes=[
    Route('/', homepage),
])