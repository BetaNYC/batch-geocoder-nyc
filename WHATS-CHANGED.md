# What's changed

This page lists the changes to the Batch geocoder for NYC that a reader would notice: new features, fixes, changes to the address lookup it uses, and corrections when we published something wrong. Newest first. Small updates to the code it runs on are not listed.

- **History begins:** 2020-04-19, the day the geocoder went live. Older entries cover only the bigger changes. Corrections made before this date may be missing.
- **Data refresh:** none. The geocoder keeps no data of its own. Every address you give it is looked up live in GeoSearch, NYC Planning's address search.

To report a bug in this site or ask for a new feature, open an issue at https://github.com/BetaNYC/batch-geocoder-nyc/issues.

## 2026-11-12: A page that lists what has changed

- **Tags:** Site
- **What changed:** This page is new. It lists the changes to the geocoder that a reader would notice, newest first, and both pages of the site link to it at the bottom.
- **More detail:** [The same list on GitHub](WHATS-CHANGED.md)

## 2026-10-16: The measuring tool on the street view page works again

- **Tags:** Site
- **What changed:** On the street view page, the button for measuring a distance in a street-level photo was not working. It now starts the measuring tool. The page's map also has a new background map.
- **Who it affects:** People who use the street view page.
- **More detail:** [Pull request](https://github.com/BetaNYC/batch-geocoder-nyc/pull/19)

## 2026-10-05: Pasted lists are read correctly, and there is a sample file

- **Tags:** Site
- **What changed:** A pasted or uploaded list can now separate its columns with commas, tabs, pipes or semicolons, and the geocoder works out which. A new link downloads a sample file to start from. The maps have a new background map, and the feedback link now goes to the project's GitHub issues.
- **More detail:** [Pull request](https://github.com/BetaNYC/batch-geocoder-nyc/pull/17)
- **Update 2026-10-07:** The background map now loads with a key from its provider. [Pull request](https://github.com/BetaNYC/batch-geocoder-nyc/pull/18)

## 2023-01-03: The geocoder moved to version 2 of GeoSearch

- **Tags:** Data, Site
- **What changed:** Addresses are now looked up in version 2 of GeoSearch, and the building number (BIN) and tax lot number (BBL) in the export are read from that version's answers. A new tip says to add a borough or ZIP code after a comma and to leave out apartment numbers. The street view page's map now credits OpenStreetMap.
- **More detail:** [The change](https://github.com/BetaNYC/batch-geocoder-nyc/commit/abddc43817283e8e5a05c97a8cb2f3d039a58c1b) · [GeoSearch's notes on version 2](https://github.com/NYCPlanning/labs-geosearch-docker/blob/master/MIGRATING.md) · [Credit to OpenStreetMap](https://github.com/BetaNYC/batch-geocoder-nyc/pull/15)

## 2022-04-24: A street view page

- **Tags:** Site
- **What changed:** A separate page, streetview.html, shows street-level photos from Cyclomedia for a point on a map. Give it a point in the web address, as lnglat or latlng. Later updates added zoom buttons.
- **More detail:** [The first version](https://github.com/BetaNYC/batch-geocoder-nyc/commit/96ca111396ff9c44e759fb6c626306c3e8d4e194) · [Zoom buttons](https://github.com/BetaNYC/batch-geocoder-nyc/commit/93151f6221462582c15b581783621d235a196586)

## 2020-08-21: The geocoder moved to www.geocoder.nyc and BetaNYC's GitHub

- **Tags:** Site
- **What changed:** The geocoder's web address became www.geocoder.nyc. Its code moved to BetaNYC's account on GitHub. From May 4, 2020 until then, its address had been geocode.dataguide.nyc.
- **More detail:** [The request to move it](https://github.com/BetaNYC/batch-geocoder-nyc/issues/1)

## 2020-04-20: Exports include the BIN and BBL

- **Tags:** Data, Site
- **What changed:** The exported file gained two columns for each address the geocoder found: the building number (BIN) and the tax lot number (BBL). The same day, a loading indicator, a feedback link, and plainer descriptions of the export were added.
- **More detail:** [The change](https://github.com/BetaNYC/batch-geocoder-nyc/commit/0a1e165afe7ae768dbedefca309501bbaee68b66)

## 2020-04-19: The geocoder went live

- **Tags:** Site, Data
- **What changed:** A free web tool to find many New York City addresses at once. Paste a list or upload a CSV, pick the columns that hold the address, check each match on a map and fix it by hand, then copy or download the results with latitude and longitude.
- **More detail:** [About the geocoder](readme.md) · [The first version](https://github.com/BetaNYC/batch-geocoder-nyc/commit/985e75a1f23b1422204118e01357e800a525acd4)
