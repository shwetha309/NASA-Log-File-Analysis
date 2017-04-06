<h1> Insight Coding Data Challenge</h1>
<p>The detailed description of the coding problem can be found in the Instructions document.</p>
<h3> Instructions to run the file and additional libraries</h3>
<li> The code has been developed in Python (2.7) and uses Pandas (0.17.1 and higher). This version of Pandas was chosen as it has maximum efficiency for sorting based on indices which is essential for Feature 3
<li> To install higher version of pandas in Ubuntu "pip install --upgrade pandas"
<li> Run the "run.sh" file. The input folder and file name is explicitly specified in the "run.sh" file. The output folder is specified.
<li> The Unit Test cases have been written in "unit_test_cases.py" file
<li> The run time is also printed when you execute the "run.sh" file.

<h3>Assumptions</h3>
<l1>For Feature 2, the URL's have been parsed and the "GET/POST/HTTP" version parameters have been removed before finding their bandwidth. <li>The "/" file in the output is probabaly an extension to the base URL. So it hasn't been removed. 

<h3>Overview</h3>
<p>Using the dataset provided for analysis we are able get a bird’s eye-view of the subject web-site whose files have been provided. From data extracted using the features, we can reasonably surmise about traffic, most visited pages and any fraudulent attempt to use the site. The four features together will help team to decide about future needs of bandwidth, content and server capacity to handle the traffic as well as additional security features that need to be in place.</p>

<h3> Additional Feature Description </h3>
<p>The three new features suggested by me will add value to the analysis by way of knowing any repeated attempts to break the security (Feature 5 -blocked_users.txt), pages which have problems in getting loaded (Feature 6-load_failed_pages.txt) and also know the most popular resources/pages and add more relevant content to these (Feature 7-top_hit_pages.txt).</p>
<h5> Feature 5 - Blocked Users</h5>
<p> Extending the Blocked User Logs of Feature 4, it is essential to also find the hosts who frequently try to make unauthorized access to the website. Filename: blocked-users.txt</p>
<h5> Feature 6 - Pages which Failed to Load
<p> Certain pages are very frequently accessed but fail to load. Fixing these pages may be essential for users to access them.
Filename: load_failed_pages.txt
<h5> Feature 7 - Top Hit Pages </h5>
<p> Certain pages are more frequently accesses by the users during a specific period. So these details can help NASA engineers in understanding the traffic flow.</p>

<p> However a much deeper analysis can be done by identifying, analysis of the originating country/location of Host/IP Address in spite of masking and correlate them with IP addresses of Blocked and failed attempts. </p>

<h3>Implementation</h3>
<p>The code has been developed in Python and used Pandas (0.17.1 and higher). I have used lambda functions internally and implemented priority queues for tuples. This has reduced the run time and space by almost 70%. Pandas library was used for grouping together the timestamps for Feature 3. This was used because it gave the shortest run time when compared to other data structures for the larger dataset.  </p>

 
