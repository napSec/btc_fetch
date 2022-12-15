# btc_fetch
btc_fetch will find bitcoin transactions of a wallet address during the time range specified by the user

# 

BTC_fetch is a commandline program that displays the transaction history of a bitcoin wallet address. BTC_fetch allows the user to enter a bitcoin wallet address and a custom date range and displays the transaction in JSON. 

This was created and successfully tested on macOS Ventura 13.0.1 (22A400) Debian GNU/Linux 10 
Requirements
  
  - python3 
  
  
Installation
  
 - install btc_fetch 
 
  $ git clone https://github.com/napSec/btc_fetch
  
  $ cd btc_fetch
  
  $ python3 btc_fetch.py

Create Alias (optional but nice)

You can run the alias command for each terminal session: 
  
  $ alias fetch="python3 /your-path/btc_fetch.py

To use "fetch' command globally, add the alias command to your ~/.bashrc file:
  
  $ nano ~/.bashrc 
  
  at the bottom of your ~/.bashrc, enter your path to where btc_fetch.py is saved
  
    alias fetch="python3 /your-path/btc_fetch.py

Usage 



  In Terminal:
    $ fetch 
![image](https://user-images.githubusercontent.com/113065386/207977420-3f4d77a0-87ab-4d2e-a650-22640fd8148e.png)

Next, enter the bitcoin wallet address that you want the transaction history:

  ![image](https://user-images.githubusercontent.com/113065386/207978267-ab0fcd3b-45aa-4642-bbee-00649fb89ba7.png)



Next, enter the start date:

  ![image](https://user-images.githubusercontent.com/113065386/207978103-41ce6850-b46b-47e0-af74-bcaea9529ede.png)

Then, enter the end date:

  ![image](https://user-images.githubusercontent.com/113065386/207978587-a71b5122-55f7-48b6-924c-d9ca22f5d70f.png)

The results 

![image](https://user-images.githubusercontent.com/113065386/207979655-c6b698f3-7548-4dfc-b319-76dd98262fc3.png)








