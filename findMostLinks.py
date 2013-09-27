# =============================================================================
# Crawl interwebs!!
#
# Author:           Max Graves
# Last Modified:    5-FEB-2013
# =============================================================================

import urllib as monkeys
import lxml.html as platypus
import pylab as pl
import random
from httplib2 import iri2uri

# =============================================================================
def linksToList(url,dom):
    """ Takes domain name and returns list of links. """
    links = []
    for link in dom.xpath('//a/@href'):
        if len(link)>0:     #wtf?
            if link[0:4] == 'http':
                links.append(link)
            elif ((link[0] != '/') and (url[-1] != '/')):
                links.append(url+'/'+link)
            elif (link[0] == '/' and url[-1] != '/'):
                links.append(url+link)
            elif (link[0] != '/' and url[-1] == '/'):
                links.append(url+link)

    return links

def iri_to_uri(iri):
    """Transform a unicode iri into a ascii uri."""
    if not isinstance(iri, unicode):
        raise TypeError('iri %r should be unicode.' % iri)
    return bytes(iri2uri(iri))

# =============================================================================
def main():

    # starting url.  Could be psuedo-randomized using random IP??  --Pete
    url1 = 'http://www.uvm.edu/~physics/?Page=gradstudents_current.html'
    #url1 = 'http://www.uvm.edu/~tjhoward/'
    numSweep = 200

    numLinks = pl.array([])
    
    # loop through urls
    for i in range(numSweep):

        print '----------------------------------------'
        print 'sweep num:   ',i+1
        print 'url1:        ',url1
        
        connection1 = monkeys.urlopen(url1)
        dom1 = platypus.fromstring(connection1.read())

        # list of links on current page
        links1 = []
        links1 = linksToList(url1,dom1)

        numLinks = pl.append(numLinks, len(links1))

        # choose random number, corresponds with next page to go to
        rand = random.randint(0,(len(links1)-1))
        print 'going to link number: ',rand
        url2 = links1[rand]
        if isinstance(url2, unicode):
            url2 = iri_to_uri(url2)
            print 'found UNICODE!!!!!!!!!!!!!!'
            raw_input("Press Enter to continue...")
        connection2 = monkeys.urlopen(url2)
        dom2 = platypus.fromstring(connection2.read())
        print 'url2:        ',url2
        
        # number of links on next page
        links2 = linksToList(url2,dom2)

        # Acceptance Ratio
        P = 1.0*len(links2)/(1.0*len(links1))

        print 'link1Nums:   ', len(links1)
        print 'link2Nums:   ', len(links2)
        print 'acceptance:  ',P

        # Metropolis Hastings
        if P >= 1.0:
            url1 = url2
            dom1 = dom2
            print 'Move Accepted!'
        else:
            r = random.random()
            print 'r:       ',r
            if r <= P:
                url1 = url2
                dom1 = dom2
                print 'Move Accepted!'
            else:
                print '...Move Declined.'
        print 'End of loop url1:    ',url1

# =============================================================================
if __name__=='__main__':
    main()
