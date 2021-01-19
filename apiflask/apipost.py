import requests
r = requests.post("http://127.0.0.1:5000/webservice", data={"Profisão": "Analista de sistemas",
                                                            "name": "bar"})
# And done.
print(r.text)
