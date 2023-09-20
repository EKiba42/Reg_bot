import uvicorn


uvicorn.run("prostir.http.app:app", port=8000, host="127.0.0.1", reload=True)
