# 📧 Email Generator
Using a trick that Gmail has, we can turn one email address into thousands in less than a second! <br>
Every single email created sends to the same inbox, however can be registered as it's own on a seperate site!

This trick can be used on most sites, in fact it is how I have 5 discord accounts under the same email! <br>
**NOTE:** This is only tested for Gmail. This may not work with other email providers.

---

# 🤔 How does it work?
This trick abuses two things about Gmail.

Gmail allows dots in the email name to be sent to the same one, e.g. `myemail@gmail.com` and `my.email@gmail.com` will both send to the same email. <br>
However, most sites recognize them as completely seperate emails and thus allow you to register with them. Pretty nifty, huh?

There is also another trick that can be used. Appending `+{number}` to the name has similar behavior. e.g. `mygmail@gmail.com` and `mygmail+1@gmail.com` are the same.
These are two methods I've found which allow for this to happen. 

---

To use it, install Python 3 and open main.py!

**Fun Fact:** The formula to get the number of combinations is as follows: `2^<Length of the email address excluding @ sign, domain and last letter> * 10` <br>
That means `myemail@gmail.com` becomes 640 emails in less than a second!
