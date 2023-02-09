<html>
<head>

</head>
<body>
  <h1>BTC Fetch</h1>
  <p>BTC_fetch is a commandline program that displays the transaction history of a bitcoin wallet address. BTC_fetch allows the user to enter a bitcoin wallet address and a custom date range and displays the transaction in JSON.</p>
  <h2>Requirements</h2>
  <ul>
    <li>python3</li>
  </ul>
  <h2>Installation</h2>
  <p>To install btc_fetch, follow these steps:</p>
  <ol>
    <li>Clone the repository:
      <pre>$ git clone https://github.com/napSec/btc_fetch</pre>
    </li>
    <li>Navigate to the repository directory:
      <pre>$ cd btc_fetch</pre>
    </li>
    <li>Run the program:
      <pre>$ python3 btc_fetch.py</pre>
    </li>
  </ol>
  <h2>Create Alias (optional but nice)</h2>
  <p>You can run the alias command for each terminal session:</p>
  <pre>$ alias fetch="python3 /your-path/btc_fetch.py</pre>
  <p>To use "fetch' command globally, add the alias command to your ~/.bashrc file:</p>
  <pre>$ nano ~/.bashrc</pre>
  <p>At the bottom of your ~/.bashrc, enter your path to where btc_fetch.py is saved</p>
</body>
</html>
