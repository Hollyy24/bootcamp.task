import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from starlette.datastructures import URL

app = FastAPI()

app.add_middleware(SessionMiddleware,secret_key="secret-key-string")
app.mount("/static",StaticFiles(directory="static"),name="static")
templates = Jinja2Templates(directory="templates")



@app.get("/",response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})



@app.post("/signin")
async def signin(request: Request,username:str =Form(...),password:str = Form(...)):
    if username == "test" and password == "test":
        request.session["sign-in"] = True
        return RedirectResponse(url="/member",status_code=303)
    elif username == ""  or password == "" :
        message = "請輸入帳號、密碼"
        url = URL("/error").include_query_params(message=message)
        return RedirectResponse(url,status_code=303)
    elif username != "test" or password != "test":
        message = "帳號、密碼輸入錯誤"
        url = URL("/error").include_query_params(message=message)
        return RedirectResponse(url,status_code=303)
    

    
    
    
@app.get("/member",response_class=HTMLResponse)
async def member(request:Request):
    if request.session.get("sign-in") == True:
        return templates.TemplateResponse("member.html",{"request":request})
    else:
        return RedirectResponse(url="/",status_code=303)


@app.get(f"/error",response_class=HTMLResponse)
async def error(request:Request,message:str):
    return templates.TemplateResponse("error.html",{"request":request,"message":message})



@app.get("/signout",response_class=HTMLResponse)
async def signout(request:Request):
    request.session["sign-in"] = False
    print(request.session.get("user"))
    return RedirectResponse(url="/",status_code=303)




#task4

@app.get("/square/{number}",response_class=HTMLResponse)
async def Squared(request:Request,number:int):
    if number <= 0:
        squared_number = "請輸入正整數"
    else:
        squared_number = number ** 2
    return templates.TemplateResponse("squared.html",{"request":request,"squared_number":squared_number})