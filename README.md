# Fastapi-Prometheus-Basic-Auth
Monitoring FastAPI application with Prometheus and implemented basic authentication for the Prometheus UI
## Prometheus Setup ##
Prometheus was used to monitor this application and Alertmanager to send email notifications when the application is down.

The files involved in prometheus configuration are alert.rules.yml, alertmanager.yml, docker-compose.yml, main.py, prometheus.yml, web.yml. 

# Main.py

from starlette_exporter import PrometheusMiddleware, handle_metrics
app.add_middleware(PrometheusMiddleware) 
app.add_route("/metrics", handle_metrics)
In main.py, PrometheusMiddleware was added, which collects metrics for every HTTP request. The ‘/metrics’ endpoint is exposed via the handle_metrics function. This endpoint is where Prometheus scrapes metrics data.
Prometheus is accessible at port 9090. 

# docker-compose.yml 

In docker-compose.yml file defined prometheus and alertmanager services. Configured each service with ports and volumes. 

# Prometheus configuration 

prometheus.yml :  Prometheus was configured  to scrape metrics from the application every 15 seconds. It also includes the alerting configuration to send alerts to Alertmanager.
alert.rules.yml: In this alerts are defined which triggers when the instance is down for more than 30 seconds.

#  alertmanager.yml 

Configures Alertmanager to send email notifications when an alert is triggered. It includes settings for email servers, recipient addresses, and email formatting. It consists of parameters like group_wait: 30s, group_interval:5m and repeat_interval:1h.

group_wait:30s: When an alert is first generated, Alertmanager waits for 30 seconds to collect more alerts that might belong to the same group before sending the notification. 
group_interval:5m: After sending an initial notification for a group of alerts, Alertmanager waits for 5 minutes before sending another notification for new alerts in the same group.
repeat_interval:1h: If an alert remains active, Alertmanager will send a reminder notification every 1 hour.
Send_resolved:true: This means that if an alert condition is no longer met, and the alert is resolved, a notification will be sent to inform that the issue has been fixed.

# Authentication of Prometheus UI (web.yml)
In  web.yml ‘admin: $2a$12$U.8r6p7GgKa6vFol630HB.eTcfAD1Af5SlVOHC6R3lCDHUT47xU6C’
Where admin is the username and password is $2a$12$U.8r6p7GgKa6vFol630HB.eTcfAD1Af5SlVOHC6R3lCDHUT47xU6C is the hash of the ‘Saikiran’ word (was generated by bcrypt-generator.com)

This hash can be generated using ‘https://bcrypt-generator.com/’ . And also need to ensure the same username ‘admin’ and password ‘Saikiran’ are mentioned in the prometheus.yml file. 

In the future, 
# Sending Alerts with Outlook and Gmail Accounts
# 1. Sending Alerts with Outlook Account
To send alerts using an Outlook account, replace the specific fields in `alertmanager.yml` with the following values:
In the `global` section:
- `smtp_require_tls` to `true` => `smtp_require_tls: true`
In the `receivers` section:
- Change the email addresses in `from` and `to`
- Set `auth_username` and `auth_identity` to the email address from which the mail needs to be sent
- Set `auth_password` to the password authentication password related to the 'from' account
- Set `require_tls` to `true` => `require_tls: true`
- Set `smarthost` to `'smtp-mail.outlook.com:587'`
# 2. Sending Alerts with Gmail Account
To send alerts using a Gmail account, replace the specific fields in `alertmanager.yml` with the following values:
In the `global` section:
- `smtp_require_tls` to `false` => `smtp_require_tls: false`
In the `receivers` section:
- Change the email addresses in `from` and `to`
- Set `auth_username` and `auth_identity` to the email address from which the mail needs to be sent
- Set `auth_password` to the password authentication password related to the 'from' account
- Set `require_tls` to `false` => `require_tls: false`
- Set `smarthost` to `'smtp.gmail.com:465'`

Ensure that the `from`, `auth_username`, `auth_identity`, and `From` (in the `headers` section) contain the same email address that will be used to send the mail notifications.

# Below are the steps to run the project
docker-compose up --build -d   (to run the project)
http://localhost:8000 to access FastAPI application
http://localhost:9090 to access Prometheus UI. Basic Authentication was implemented for prometheus UI so, it give prompt to enter username and password. 
Prometheus scrapes metrics from the application and make them available at http://localhost:8000/metrics 
http://localhost:9093 to access Alertmanager UI. Basic Authentication was implemented for Alertmanager UI so, it give prompt to enter username and password. 
