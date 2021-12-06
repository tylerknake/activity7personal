# NAME: Tyler Knake
# DATE: 12/5/2021
# COURSE: ISQA 3900 Web Application Development

class Customer:
    def __init__(self, cust_num, fname, lname, company, street, city, state, zipcode):
        self.cust_num = cust_num
        self.fname = fname
        self.lname = lname
        self.company = company
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

    # Returns the fullname plus the full address
    def __str__(self):
        return('{}\n{}'.format(self.cust_name(), self.cust_fullAddress()))

    # Returns customer full name
    def cust_name(self):
        return('{} {}'.format(self.fname, self.lname))

    # Returns customer full address, whether there is a company name or not
    def cust_fullAddress(self):
        if self.company.strip():
            return('{}\n{}\n{}, {} {}'.format(self.company, self.street, self.city, self.state, self.zipcode))
        else:
            return('{}\n{}, {} {}'.format(self.street, self.city, self.state, self.zipcode))

    # Returns the customer id or number
    def cust_ID(self):
        return(self.cust_num)

    # Returns the company name if present otherwise None
    def cust_company(self):
        if self.company.strip():
            return self.company.strip()
        else:
            return None
    