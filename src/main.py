from fastapi import FastAPI
import DataSchemes as sch

app = FastAPI()

@app.get('/login/')
async def logIn():
    pass

@app.post('/sign-in')
async def signIn():
    pass

@app.delete('/usuarios')
async def delUsuarios():
    pass

@app.put('/usuarios')
async def putUsuarios():
    pass

@app.get('/organzacion')
async def getOrg():
    pass

@app.get('/productos/jwt/organization/inventory')
async def getProducts(jwt:str, organization:int, inventory: int) -> dict:    
    return {}

@app.delete('/productos')
async def delProducts():
    pass

@app.post('/productos')
async def postProducts():
    return {"":""}

@app.put('/productos')
async def putProducts():
    pass
