# donationalerts_nightbot

<p align="center" width="100%">
    <img width="75%" src="https://i.imgur.com/WKIXwj9.png"> 
</p>


**Nightbot send new donation alerts to twitch , youtube , trovo chat!** - simple code on python 3.10

1) Get token from donationalerts.com.<br /> u can find your token here https://www.donationalerts.com/dashboard/general-settings/account
2) Get Nightbot auth token.<br /> how get Nightbot token read here https://community.nightdev.com/t/nightbot-alerts-in-chat/24059

Script create donate.json file and store last donate data, u can host donate.json on webserver and create nightbot !lastdonate command<br />

!lastdonate command example :<br />

```
$(eval j=decodeURIComponent("$(querystring $(urlfetch json https://YOUR-DOMAINNAME.COM/donate.json))");try{d=JSON.parse(j);`last donate: ${d.date_created} : ${d.amount_main} ${d.currency} from ${d.username} :message: ${d.message}`.slice(0,400)}catch(e){`Failed to parse donation info: ${e.message}: ${j}`.slice(0,400)})
```

<p align="center" width="100%">
    <img width="75%" src="https://i.imgur.com/InMBNjP.png"> 
</p>
