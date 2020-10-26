# chat-bot-rasa

# run with facebook
rasa run --endpoints endpoints.yml --credentials credentials.yml  & rasa run actions

# run with web
rasa run -m models --enable-api --cors "*"  & rasa run actions

# refresh localhost 5005
fuser -k 5005/tcp
