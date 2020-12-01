# OmbiAdd
Built for interaction with Plex Autoscan. Allows marking of available when Plex Autoscan has updated the movie/show file.

# Installation
Clone the repo to destination of your choice.
```
git clone https://github.com/jolbol1/OmbiAdd.git
```
Ensure the file is executable
```
cd OmbiAdd
chmod u+x OmbiAdd.py
```
# Config
```
ombi:
  url: https://ombi.domain.com
  apikey: XXXXXXXXXXXXXXXXXXXXXXXXXXXx
  database_path: /opt/ombi/app/Ombi.db
```
* *url*: Please use the outward facing url. If using cloudbox this will be similar to the example.
* *apikey*: Got to `Ombi > Settings > Ombi` and copy the Api Key here.
* *database_path*: This is where ombi is installed. You are looking for the Ombi.db file. For cloudbox this will be the same as the above.

# Usage
Once installed you should be able to run the command. It will need 3 variables:
```
OmbiAdd.py Type Id config_path
```
* *Type*: Can be, TheMovieDB, IMDB, TheTVDB
  * NOTE: For TV Shows, only the TVDB id can be used.

* *Id*: The episode/movie id from the above sources (for example for 50 first date, you could use *tt0343660* for IMDB, *1824* for TMDB)

* *config_path*: This is the path to the config.yml folder, for example on my cloudbox its `/opt/OmbiAdd/config.yml`

# Plex Autoscan
To use this with [Plex Autoscan](https://github.com/l3uddz/plex_autoscan) you will need to replace Plex Autoscans plex.py file with [this one](https://raw.githubusercontent.com/jolbol1/plex_autoscan/master/plex.py) and ensure its executable.

Then edit the following in the Plex Autoscan config:
```
"RUN_COMMAND_AFTER_SCAN": "/opt/OmbiAdd/OmbiAdd.py $scan_lookup_type $scan_lookup_id /opt/OmbiAdd/config.yml",
```
The scan variables will be handled by plex Autoscan. Ensure the path to the script and path to the config are correct. The above is correct for a cloudbox install following the above steps.
