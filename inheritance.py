class Prospect: #create a prospect for intial stage of sales engagment
    name = 'No name Provided'
    email = 'Unknown '
    phone_number = 'Unknown'
    company= 'Unknown'
print("\nName: {}\nEmail Address: {}\nPhone Number: {}\nCompany {}".format(Prospect.name, Prospect.email, Prospect.phone_number, Prospect.company))


class Lead(Prospect):#once a prospect is qualified, it will become a lead, and will requie a lead status and lead score
    lead_status = 'Unkonwn'
    lead_score= 0.00

class Contact(Prospect):#a qulaified lead will be converted to a cntact, and each contact will have a salesrep assigned\
    contact_owner = 'Salesrep Name'#as a contact owner. Ann opportunity can be created and linked to a contact.
    opportunity_created = False
    
    
