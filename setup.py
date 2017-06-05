import facebook

graph = facebook.GraphAPI(access_token='EAACEdEose0cBALEHGaGkgGHOh5aWSvXVwhZASniobSbBf24pK5pw78AYlL9f8CYtgza0RPfurWnF39kEBfA4kyP5s63YfHu93bQBh6MQ6ZCYKhOOg0nAZA9GY3dX7yuvRJdar0yhkESKeyoaCDIs8FN3qS9nKRUxtZBrZBbj0XvJvBteFfCmyvjQ95e20GhkZD', version='2.7')

profile = graph.get_object("me")
friends = graph.get_connections("1395616190500982", "likes")
#graph.put_object("me", "feed", message="Hey its me RJ")
print(friends)
print(profile)