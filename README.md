Maximize InterWebs
==================

Metropolis-Hastings Monte Carlo algorithm that crawls the web and finds its way to the page with the most links.

This needs to be sandboxed!  DO NOT run this unless you know what you are doing, as it could have
some bad results.

This will start at one URL and will scrape all of the links off of the page, creating a list of all
of the N links.  Then, a random number integer (call it r) between 1 and N is (pseudo)randomly
generated and then the crawler 'goes' to the rth site if it has more links than the current page.
If it doesn't have more links than the current page then a uniformly distributed random number
between 0 and 1 is generated and compared to the ratio of links on new page to links on current
page.  If the new random number is smaller than said ratio then we go to the new page and if not
then we choose another of the numbers between 1 and N.

The security issues with this should be obvious, I just wanted to play with some of the Python
modules which allow one to scrape the web.

In the future, this could be parallelized (I never got around to this..other things take precedence)
such that we take ~5-10 steps through our web page "configuration space" and then split off one
"walker" into two.
