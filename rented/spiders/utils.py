def export_html(response):
    page = response.url.split("/")[-2]
    filename = f"{page}.html"
    with open(filename, "wb") as f:
        f.write(response.body)
    
