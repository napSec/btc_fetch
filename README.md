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

If you added the fetch alias to your ~/.bashrc file or entered it in terminal

  In Terminal:
    $ fetch 

![image](https://user-images.githubusercontent.com/113065386/207973553-e69fbe61-f465-40d9-b7ec-c58ce4e132a7.png)







