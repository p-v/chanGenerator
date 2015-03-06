
**chanGenerator**
==========

Generates changelog for a github repository based on the closed issues. 

###**usage:** 


    chanGenerator <user> <repository> <options>
 
 ***Example:***
    
Generate changelog since tag v1.1.1

    chanGenerator <user> <repository> --show-categorized --tag v1.1.1
Generate changelog between 2015-01-01 and 2015-02-10

    chanGenerator <user> <repository> --time-range 2015-01-01 2015-02-10
Generate changelog since commit 75c9687

    chanGenerator <user> <repository> --commit 75c9687

