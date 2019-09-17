#!/usr/bin/env bash
check_env() {
    if [[ -z "$WEBHOOK_URL" || -z "$APP_PROJECT" ]]
    then
        echo "Please set the environment variables WEBHOOK_URL and APP_PROJECT"
        exit 1
    fi
}

deploy() {

  check_env

  echo "Deploying slackRax cloud function."
  gcloud beta functions deploy slackRax --set-env-vars WEBHOOK_URL="$WEBHOOK_URL" --source functions/slackRax/ --runtime python37 --trigger-http --entry-point=handleRequest --project $APP_PROJECT
  echo "all the things deployed!!! _o/"
}

main() {
  deploy
}

main
