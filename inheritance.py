class Prospect: #create a prospect for intial stage of sales engagment
    name = 'No name Provided'
    email = ' '
    phone_number = ' '
    company= ' '

class Lead(Prospect):#once a prospect is qualified, it will become a lead, and will requie a lead status and lead score
    lead_status = ' '
    lead_score= 0.00

class Contact(Prospect):#a qulaified lead will be converted to a cntact, and each contact will have a salesrep assigned\
    contact_owner = ' '#as a contact owner. Ann opportunity can be created and linked to a contact.
    opportunity-created = False
    
    
