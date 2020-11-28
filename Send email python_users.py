# -*- coding: utf-8 -*-
"""
Created on Dec 21 2019
@author: Gal Inbar
"""

"""
This function send email to list of emails, after running a model to detect potential
users after "clustering". 
"""


import numpy as np

 
def sendEmail(to_list,run_output,users): # The function gets 1. list to send
                                         #                   2. run_output = if the process finished succsessfully ( "OK") else will be "not_OK". 
                                         #                   3. users = list of highly potential users for promotion.
    import smtplib

    def prompt(prompt):
        return input(prompt).strip()

    fromaddr = "model_name@name_of_domain.com" # name_of_domain = is the name of company domain ( ex : hp) 
    toaddrs  = to_list.split()

    # Add the From: and To: headers at the start!

    if(run_output=='OK'):
        if(users.shape[0] > 0):
            msg =("""\
                    Subject: model_name_output  
                    The process run  %s today.
                    The list of target users are : %s """ % (run_output, ", ".join(users)))
        else:
            msg =("""\
                            Subject: model_name_output  
                            The process run today without any targeted users. """)
    else:
        msg =("""\
                Subject: model_name_output  
                The process didnt run today !! Please check loger for more details """)

    print("Message length is", len(msg))

    try:
        server = smtplib.SMTP('mailhost.****.co.il') # hosting email of company ( ex: 'mailhost.google.com')
        server.set_debuglevel(1)
        server.sendmail(fromaddr, toaddrs, msg)

    except Exception as e:
        #Print any error messages to stdout
        print(e)
    finally:
        server.quit()
        
        
#Execute : (When we have list of users we want to promote something )
sendEmail(to_list = "gal.inbar@gmail.com",
           run_output = 'OK',
           users = np.array(['50123','5012314']))       
