@app.get("/user-service")
async def read_status():
    """
    Simulates Broken Object Level Authorization (BOLA)
    """
    if random.choice([True, False]):
        raise HTTPException(
            status_code=403, detail="Access Denied - Broken Object Level Authorization"
        )
    return {"message": "User Service Accessed Successfully"}