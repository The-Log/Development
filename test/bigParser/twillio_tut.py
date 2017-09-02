from twilio.rest import Client

c = Client("AC402bb5eee2a9bc760d2417395c394d1a", "33ae8485c985badec56911ca3a8c25a0")

number='15754940173'
message='this better work'

# print(client.send_message({'from': '15714940173','to': number,'text': message }))
c.messages.create(to="+15714940173",from_="+13474346447", body="Hello from Python")
