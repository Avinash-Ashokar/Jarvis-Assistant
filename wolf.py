import wolframalpha

app_id = 'QP3PU3-2732W55TG7'  # get your own at https://products.wolframalpha.com/api/
client = wolframalpha.Client(app_id)


def wolf_search(val):
    res = client.query(val)
    return next(res.results).speak
