if __name__ == "__main__":
    import uvicorn
    uvicorn.run("source.main:app", host="0.0.0.0", port=80)