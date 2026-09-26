# Bramble Camp Log

A camping log hosted by Bramble, an original cartoon bear in an orange beanie, and Pip, his cub sidekick.
The app is a single `index.html` plus its icons, manifest and offline service worker.

- **Our Campsites:** log the places you've camped, rate them 1–5 picnic baskets, and note amenities, activities, gear and tips.
- **Find a Site:** search for campgrounds by ZIP code, distance, dates, price, activities and amenities.
- **Watch List:** track hard-to-get sites, the dates you want, and their booking pages.

**Open the app:** https://bazingasc.github.io/bramble-camp-log/

## For friends

- **Install it:** tap **Install app** (Android / desktop) or **Share → Add to Home Screen** (iPhone). It works offline.
- **Your data is yours:** your log is saved on your device. Tap **Sign in with Google** to sync it to a private app folder in *your own* Google Drive, or use **Back up my log** to save a file.
- **Campground search** runs on Claude. Open the Claude version of the app while signed in to Claude, and searches use your own Claude account.

Nothing you do in the app is stored on, or billed to, anyone else's account.

## Editing

The app source is `../bramble-camp-log.html` (the owner's Claude version). After editing it, run `python build.py` to regenerate
`index.html` and the friends' Claude copy, then push to GitHub.

### Google sync setup (owner, one time)

Set `GOOGLE_CLIENT_ID` in the app source to an OAuth client ID (type "Web application") from a Google Cloud project with the
Google Drive API enabled, authorized JavaScript origin `https://bazingasc.github.io`, and the `drive.appdata` scope on its consent screen.
