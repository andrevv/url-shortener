from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse

from .logic import to_short, to_original

app = FastAPI()


@app.post('/shorten', status_code=200)
def shorted(url: str):
    return to_short(url)


@app.get('/redirect')
def redirect(short_url: str):
    original_url = to_original(short_url)
    return RedirectResponse(url=original_url, status_code=status.HTTP_301_MOVED_PERMANENTLY)
