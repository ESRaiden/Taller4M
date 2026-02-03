from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root_v2():
    return {
        "api": "User Management v2",
        "version": "2.0.0",
        "_links": {
            "self": {
                "href": "/",
                "method": "GET"
            },
            "users": {
                "href": "/users",
                "method": "GET"
            },
            "stats": {
                "href": "/stats",
                "method": "GET"
            },
            "health": {
                "href": "/health",
                "method": "GET"
            },
            "docs": {
                "href": "/docs",
                "method": "GET"
            }
        }
    }