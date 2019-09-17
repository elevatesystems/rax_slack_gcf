# rax_slack_gcf

publish to google cloud functions:
1. create new project by going to https://console.cloud.google.com/projectcreate
2. name project, setup billing (dont worry unless your cloud monitoring account YUUUGE you'll be fine)
3. install gcloud cli using directions [here](https://cloud.google.com/sdk/docs/#install_the_latest_cloud_tools_version_cloudsdk_current_version)
4. use your project name to deploy the app with the deploy script: `APP_PROJECT=MY-PROJECT-NAME WEBHOOK_URL=MY_SLACK_WEBHOOK_URL ./deploy.sh`, once command is done, note the https url, you'll need it

go create a slack webhook with these directions: https://api.slack.com/incoming-webhooks

setup your rax notifications:
1. visit https://intelligence.rackspace.com/cloud/notifications
2. name the plan, select type webhook, and paste in the URL from previous step.
3. go test by triggering an alert.
