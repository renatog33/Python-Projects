class Prospect: #create a prospect for intial stage of sales engagment
    name = 'No name Provided'
    email = 'Unknown '
    phone_number = 'Unknown'
    company = 'Unknown'
    prospectid = '1'

    def search_id(self): #this method will display the propsect's name if the matching Prospect ID in inputted
        entry_prospectid = input ("Enter the prospect's id number: ")
        if (entry_prospectid == self.prospectid):
            print("The prospect's name is {}.".format(Prospect.name))
        else:
            print("The Prospect ID you entered does not match the prospect.")
                                   


class Lead(Prospect):#once a prospect is qualified, it will become a lead, and will requie a lead status and lead score
    lead_status = 'Unkonwn'
    lead_score = 0.00
    leadid = '100'

    def search_id(self): #this method will display the leads's name if the matching Lead ID in inputted this is the same method in the parent calss \
        entry_leadid = input ("Enter the lead's id number: ")#"Prospect", but instead of prospectid, we're using leadid.
        if (entry_leadid == self.leadid):
            print("The lead's name is {}.".format(Prospect.name))
        else:
            print("The Lead ID you entered does not match the lead.")


class Contact(Prospect):#a qulaified lead will be converted to a cntact, and each contact will have a salesrep assigned\
    contact_owner = 'Salesrep Name'#as a contact owner. Ann opportunity can be created and linked to a contact.
    opportunity_created = False
    contactid = '1000'

    def search_id(self): #this method will display the contact's name if the matching COntact ID in inputted this is the same method in the parent calss \
        entry_contactid = input ("Enter the contact's id number: ")#"Prospect", but instead of prospectid, we're using contactid.
        if (entry_contactid == self.contactid):
            print("The contact's name is {}.".format(Prospect.name))
        else:
            print("The Contact ID you entered does not match the contact.")


if __name__ == "__main__":
    p = Prospect()
    p.search_id()

    l = Lead()
    l.search_id()

    c = Contact()
    c.search_id()
    

    
