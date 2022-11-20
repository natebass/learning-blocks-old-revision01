
from current_grades import Api



@app.get("/report", response_class=HTMLResponse)
async def read_item(request: Request, school_id: str, item_id: str, api_key: str):
    aries_api = Api(school_id, item_id, api_key)
    query_result = aries_api.get_current_grades_demo()
    return templates.TemplateResponse("report.html", {"request": request, "school_id": school_id, "item_id": item_id,
                                                      "api_key": api_key, "query_result": query_result})


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/current_grades")
async def get_current_grades():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
