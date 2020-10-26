# chat-bot-rasa

### run
rasa run --endpoints endpoints.yml --credentials credentials.yml  & rasa run actions

rasa run -m models --enable-api --cors "*"  & rasa run actions

# refresh localhost 5005
fuser -k 5005/tcp
