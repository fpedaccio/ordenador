try:
    100/0
except Exception as e:
    print(e.__class__.__name__)