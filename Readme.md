<h1> Insight Coding Data Challenge</h1>
<p>The detailed description of the coding problem can be found in the Instructions document.</p>
<h3> Instructions to run the file and additional libraries</h3>
<li> The code has been developed in Python and uses Pandas (0.14.1 and higher) 
<li> Run the "run.sh" file. The input folder and file name is explicitly specified in the "run.sh" file. The output folder is specified.
<li> The Unit Test cases have been written in "unit_test_cases.py" file

<h3>Overview</h3>
<p>Using the dataset provided for analysis we are able get a bird’s eye-view of the subject web-site whose files have been provided. From data extracted using the features, we can reasonably surmise about traffic, most visited pages and any fraudulent attempt to use the site. The four features together will help team to decide about future needs of bandwidth, content and server capacity to handle the traffic as well as additional security features that need to be in place.</p>

<h3> Additional Feature Description </h3>
<p>The three new features suggested by me will add value to the analysis by way of knowing any repeated attempts to break the security (Feature 5 -blocked_users.txt), pages which have problems in getting loaded (Feature 6-load_failed_pages.txt) and also know the most popular resources/pages and add more relevant content to these (Feature 7-top_hit_pages.txt).</p>
<p> However a much deeper analysis can be done by identifying, analysis of the originating country/location of Host/IP Address in spite of masking and correlate them with IP addresses of Blocked and failed attempts. </p>

<h3>Implementation</h3>
<p>The code has been developed in Python and used Pandas (0.14.1 and higher). I have used lambda functions internally and implemented priority queues for tuples. This has reduced the run time and space by almost 70%. </p>