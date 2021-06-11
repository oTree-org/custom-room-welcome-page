Here is how to customize the "Welcome" page that says "please enter your participant label".

Clone this repo, then customize the file `RoomInputLabel.html`.
You must customize the `action` parameter to point to your oTree server & room name.

Then, deploy to Heroku with:

```
heroku create
git push heroku master
heroku open
```

Give your participants the URL to this site. They will enter their participant label, then it will redirect them to
your oTree site, where they should then see the "waiting for your session to begin".