import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "src.main.config.http_server_config:app",
        host="0.0.0.0",
        port=8202,
        reload=True,
        debug=True,
        # workers=3
    )
