from twilio.rest import Client

account_sid = "ACbbef7f076edb70b892fe25e14ee4ec6a"
auth_token = "66ee41c587467a74c42e957f539b2cd7"

client = Client(account_sid, auth_token)

# SMS
# message = client.messages.create(
#     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#     from_="+1 775 458 9306",
#     to="+94 77 637 9650",
# )

# Whatsapp
message = client.messages.create(
      from_="whatsapp:+14155238886",
      body="It's going to rain today. Remember to bring an umbrella",
      to="whatsapp:+94702233551"
    )

print(message.body)