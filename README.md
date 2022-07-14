# ddns-map-checker
The respository for the ddns map checker website.

By using the "get_status" function of <a href="https://github.com/VozdyxDev/pydustry" id ="link">pydustry</a>, we can use utilize that to get the current map on a server, read a file with all of the maps and if the file doesn't already contain the map then it'll add the map to the file. It is constantly doing this.

As for actually checking for the map, we use a html form that creates textbox that can then be accessed by <a href="https://github.com/pallets/flask" id="link">flask</a>. At which when the "submit" button is pressed, we then make the received data lowercase and check if it is in the maps file. It isn't too efficient of a way of checking, however it'll work for now seeing as I was in a small rush to get this done.

In order to use this, you'll have to include the color codes and have the spaces replaced with an underscore. Naturally, I would of made it so that it automatically converted spaces to underscores or vice versa and removed color codes, however as mentioned before I was in a small rush in order to get this complete. I will soon add a function that shows a complete list of the maps currently in cycle, however this may come after I upgrade the map database. Especially seeing as it is really only just a .txt file that holds all of the map names without any real orginization.
