<strong> Post Mortem </strong>
<hr>

<strong>Issue Summary</strong> <br>
On September 11th, 2022 from 9:39 AM to 9:49 AM GMT, the company's website was down for ten minutes. <br>
100% of users experienced a 500 internal server error caused by a mispelled filename in a configuration file. <br>

<strong>Timeline</strong><br>
9:39 AM Sitewide update deployed; outage begins <br>
9:40 AM Error logs checked by DevOps team <br>
9:43 AM Configuration updated to log extra errors<br>
9:45 AM Filename error caught in config file <br>
9:47 AM Execute Puppet manifest across all company servers <br>
9:49 AM 100% restored and back online

<strong>Root Cause and Resolution</strong> <br>
After a small sitewide update was deployed without first being tested, outage to the site began. When no errors were found in our 'error.log' files we <br> modified our configuration file to allow for more erorr logging. With the help of 'strace,' it appeared an accidental filename mispelling triggered errors<br> when the site was requested. The server was attempting to locate the file as normal procedure but failed to find the file ending in ".phpp" when it should be looking for ".php" After changing this line in the '/var/www/html/wp-settings.php' file, tests suceeded to show the site. A puppet manifest<br> was written and executed across all company servers immediately after to restore service.

<strong>Corrective and Preventative Measures</strong><br>
After a discussion it has been decided we can prevent this in the future by:

Modifying configuration files for more error logging to quicken response times<br>
Test before deploying on all servers no matter how small an update This is only a small incident so we are doing great! Thanks for your patience and your<br> continued confidence in us.
