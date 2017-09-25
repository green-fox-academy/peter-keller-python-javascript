class Blogpost(object):
    author_name = ""
    title = ""
    text = ""
    publication_date = ""

post1 = Blogpost()
post2 = Blogpost()
post3 = Blogpost()

post1.author_name = "John Doe"
post1.title = "Lorem Ipsum"
post1.text = "Lorem ipsum dolor sit amet."
post1.publication_date = "2000.05.04."

post2.author_name = "Tim Urban"
post2.title = "Wait but why"
post2.text = "A popular long-form, stick-figure-illustrated blog about almost everything."
post2.publication_date = "2010.10.10."

post3.author_name = "William Turton"
post3.title = "One Engineer Is Trying to Get IBM to Reckon With Trump"
post3.text = "Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing."
post3.publication_date = "2017.03.28."

print(post1.author_name, post1.title, post1.text, post1.publication_date)
print(post2.author_name, post2.title, post2.text, post2.publication_date)
print(post3.author_name, post3.title, post3.text, post3.publication_date)