import uvicorn
import os
import mysql.connector
from dotenv import load_dotenv

from fastapi import FastAPI,Request,Form,Query
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse,RedirectResponse,JSONResponse
from starlette.middleware.sessions import SessionMiddleware
from starlette.datastructures import URL
from pydantic import BaseModel


load_dotenv()

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = os.getenv("MY_PASSWORD"),
    database ="website"
)


class Newname(BaseModel):
    newname : str


app = FastAPI()

app.add_middleware(SessionMiddleware,secret_key="secret-key-string")
app.mount("/static",StaticFiles(directory="static"),name="static")
templates =  Jinja2Templates(directory="templates")



@app.get("/",response_class=HTMLResponse)
async def root(request:Request):
    print("Here is HomePage !")
    return templates.TemplateResponse("index.html",{"request":request})



@app.get("/member",response_class=HTMLResponse)
async def member(request:Request):
    if request.session.get("sign-in") == True:
        mycursor = mydb.cursor()
        print("Here is Member")
        name = request.session.get("name")
        user_id = request.session.get("id")
        mycursor.execute("SELECT member.id,member.name,message.content,message.id FROM message LEFT JOIN member ON message.member_id = member.id")
        messages = mycursor.fetchall()
        mycursor.close()
        return templates.TemplateResponse("member.html",{"request":request,"name":name,"messages":messages,"user_id":user_id})
    else:
        return RedirectResponse(url="/",status_code=303)


@app.get("/error",response_class=HTMLResponse)
async def error(request:Request,message:str|  None=None):
    return templates.TemplateResponse("error.html",{"request":request,"message":message})


@app.post("/signup")
async def signup(request: Request,name:str=Form(...),username:str =Form(...),password:str = Form(...)):
    print("here is signup!")
    try:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM member WHERE username = %s",(username,))
        result = mycursor.fetchall()
        if result :
            message = "帳號重複！請輸入其他名稱。"
            url = URL("/error").include_query_params(message=message)
            return RedirectResponse(url,status_code=303)
        else:
            print("success")
            mycursor.execute("INSERT INTO member (name,username,password)VALUES (%s,%s,%s)",(name,username,password,))
            mydb.commit()
            mycursor.close()
            return RedirectResponse(url="/",status_code=303)

    except Exception as e:
        print(f"Error during signup: {e}")
        message = "註冊失敗，請稍後再試。"
        url = URL("/error").include_query_params(message=message)
        return RedirectResponse(url, status_code=303)



@app.post("/signin")
async def signin(request: Request,username:str =Form(...),password:str = Form(...)):
    print("Here is signin !")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM member WHERE username = %s AND password = %s",(username,password,))
    result = mycursor.fetchone()
    mycursor.close()
    if result:
        request.session["sign-in"] = True
        request.session["username"] = result[2]
        request.session["name"] = result[1]
        request.session["id"] = result[0]
        return RedirectResponse(url="/member",status_code=303)
    else:
        try:
            message = "帳號或密碼錯誤！"
            url = URL("/error").include_query_params(message=message)
            return RedirectResponse(url, status_code=303)
        except Exception as e:
            message = "失敗，請稍後再試。"
            url = URL("/error").include_query_params(message=message)
            return RedirectResponse(url, status_code=303)



@app.get("/signout")
async def signout(request:Request):
    print("Here is signout !")
    request.session.clear()
    return RedirectResponse(url="/",status_code=303)



@app.get("/api/member")
async def search(request:Request, username: str = Query(...)):
    print("Here is search")
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM member WHERE username = %s",(username,))
    myresult = mycursor.fetchone()
    if myresult:
        data = {"id":myresult["id"],
                "name":myresult["name"],
                "username":myresult["username"]}
    else:
        data = None    
    return JSONResponse(content={"data":data})


@app.patch("/api/member")
async def update_name(request:Request,newname :Newname):
    print("Here is patch")
    username = request.session.get("username")
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("UPDATE member SET name = %s WHERE username =%s ",(newname.newname,username,))
    print(f"username:{username}, newname: {newname.newname}")
    try:
        mydb.commit()
        result = {"ok":True}
    except Exception as e:
        result = {"error":True}
    finally:
        mycursor.close()
    return JSONResponse(content=result)



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)