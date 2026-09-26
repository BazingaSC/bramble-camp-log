# Bramble Camp Log

A camping log hosted by Bramble, an original cartoon bear in an orange beanie, and Pip, his cub sidekick. The app is a single `index.html` plus its icons, manifest and offline service worker.

- **Our Campsites:** log the places you've camped, rate them 1–5 picnic baskets, and note amenities, activities, gear and tips.
- **Find a Site:** search for campgrounds by ZIP code, distance, dates, price, activities and amenities.
- **Watch List:** track hard-to-get sites and the dates you want.

## Install as an app

Open the site on a phone and tap **Install app** (Android/desktop) or **Share → Add to Home Screen** (iPhone). It works offline, and **Back up my log** saves a file you can restore on any device.

## Editing

The app source is `../bramble-camp-log.html` (the Claude version). After editing it, run `python build.py` to regenerate `index.html`.

## Hosting notes

On GitHub Pages the app saves your log in your own browser (`localStorage`), so each device keeps its own copy.
Campground search and email alerts need Claude, so they only work in the Claude-hosted version of the app.
