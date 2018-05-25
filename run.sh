#!/bin/bash

. .env

docker run --name twitter-follow --rm -it \
  -e CONSUMER_KEY=$CONSUMER_KEY \
  -e CONSUMER_SECRET=$CONSUMER_SECRET \
  -e ACCESS_TOKEN=$ACCESS_TOKEN \
  -e ACCESS_TOKEN_SECRET=$ACCESS_TOKEN_SECRET \
  -e DEFAULT_TWITTER_TARGET=$DEFAULT_TWITTER_TARGET \
  -e TELEGRAM_BOT_TOKEN=$TELEGRAM_BOT_TOKEN \
  -e USE_TEST_BOT=$USE_TEST_BOT \
  -e TELEGRAM_TEST_BOT_TOKEN=$TELEGRAM_TEST_BOT_TOKEN \
  -e DEBUG=$DEBUG \
  twitter-follow:dev
