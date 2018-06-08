'''
This workflows monitors the acceleration data and detects motion.  If the device shakes past the impact threshold,
we send an email alert and SMS alert to the email and phone number listed. It will send maximum one alert 
per day.
'''
import Store
import FreeSMS
import Email
 
phone_number = "1234567890"
email_address = "demo@medium.one"
 
alert_message = 'Heads up!  Your device has moved!'
 
#threshold in G-force
impact_threshold =  2.25	# 1.5Gs
 
axis_max_list=[IONode.get_input('in1')['event_data']['value'] ** 2,
               IONode.get_input('in2')['event_data']['value'] ** 2,
               IONode.get_input('in3')['event_data']['value'] ** 2]
 
# This checks if there was impact, and if it has been more than 24 hours since sending 
# an alert for this device.
if (max(axis_max_list) > impact_threshold) and not Store.get('sent_alert'):
    email = Email.Email(sender='alerts@medium.one', display_name='Medium One Alerts',
                recipients=[email_address], subject='Alert: Motion Detected', message=alert_message, attachments=None)
    email.send()
    FreeSMS.sendSMS(phone_number, alert_message) 
    Store.set_data('sent_alert', 'true', ttl=86400) # 86400 seconds = 1 day

