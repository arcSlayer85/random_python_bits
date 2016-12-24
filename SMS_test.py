from twilio.rest import TwilioRestClient;

accountSID = 'MGe4b782e2067ac7d81c93c6348f0cbc9d';

authToken = '4bb25f3a8b5bff3c56ccf1970cbd07d1';

twilioCli = TwilioRestClient(accountSID, authToken);

myTwilioNumber = '+441315103478';

myPhone = '+447807017870';

msg = twilioCli.messages.create(
    body='Mr. Watson - Come here - I want to see you.',
    from_ = myTwilioNumber, to = myPhone);
