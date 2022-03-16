# Chamber

A Discord webhook app to notify you about your daily Valorant shop!

## Installing

After downloading the code, you need to make edits to `main.py` vars for the script to run.

`mention_for` is a list of skin ID's that. You can search for skin ID's in [this]() file.

`mention_who` is a text that should be printed when skin from `mention_for` pops in your daily shop. (To actually mention someone on discord you need to edit it to `<@USER_ID_HERE>` ex. `<@123456789012345678>`)

`login` and `password` are self explanatory.

`webhook` is your discord webhook link. To create a webhook for your server head to `Server Settings` > `Integrations` > `Webhooks` and create a new one.

## Usage

After setting up your vars, simply run the script:

```
> python3 main.py
```

Then you should be able to see a messege like this in your selected channel.
![example.png]()
