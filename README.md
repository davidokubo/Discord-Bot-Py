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
- join
  
  Joins voice channel of user
  
  > E.G.: `!join`
 
- move
  
  Moves to voice channel of user
  
  > E.G.: `!move`
  
- play \<youtube URL\>
  
  Downloads youtube video audio and plays it
  
  >  E.G.: `!play https://www.youtube.com/`

- pause
  
  Pauses audio being played
  
  > E.G.: `!pause`

- resume
  
  Resumes paused audio
  
  > E.G.: `!resume`
 
- stop
  
  Disconnects from voice channel
  
  > E.G.: `!stop`
