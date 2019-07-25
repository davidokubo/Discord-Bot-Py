# Discord-Bot-Py
Simple Discord Bot in Python
## Usage
The bot responds to commands starting with a '!'


## Commands
*User is the user who gave the text command in a discord Text Channel*
- hello

  Responds in chat to user with a Hello and their name
  
  > E.G.: `!hello`

- temp *optional* \<city name\>
  
  Uses openweather.api to get weather information and responds in chat with the temperature
  
  No input defaults to Corvallis, Oregon
  
  > E.G. 1: `!temp`
  
  > E.G. 2: `!temp Sacramento`

- roll \<number of dice\>d\<type of dice\>
  
  Calculates random number between 1 and the *type of dice* a number of times equal to the *number of dice*
  
  Responds in chat with a list of all the individual random numbers and the total
  
  > E.G.: `!roll 1d20`

- setMusic

  Creates a text-channel \[hooman-music\] to listen for music commands in
  
  Music commands can *only* be played in this channel
  
  > E.G.: `!setMusic`
  
 - play \<youtube URL\>
 
   Joins voice channel of user, creates music player, and plays audio of youtube video
   
   >  E.G.: `!play https://www.youtube.com/`
