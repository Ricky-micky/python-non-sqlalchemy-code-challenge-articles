class Article:
    all = []# Class attribute to store all created Article instances.


    def __init__(self, author, magazine, title):
        self.author = author# Set the article's author.
        self.magazine = magazine# Set the article's author.
        self.title = title  # Set the article's title.
        type(self).all.append(self)# Add the current instance to the 'all' list.


    @property
    def title(self):  # Return the title's value.

        return self._title

    @title.setter
    def title(self, title):
        if (
            isinstance(title, str) # Check if the title is a string.
            and 5 <= len(title) <= 50# Ensure title length is between 5 and 50
            and not hasattr(self, "title") # Ensure the title isn't already set.
        ):
            self._title = title # Set the private attribute '_title'.
        else:
            return None # Return None if validation fails.

           
    @property
    def author(self):
        return self._author # Return the article's author.

    @author.setter
    def author(self, author):
        if isinstance(author, Author):# Ensure the author is an instance of `Author`.
            self._author = author # Set the private attribute '_author'.
        else:
            return None# Return None if validation fails.
  
    @property
    def magazine(self):
        return self._magazine # Return the associated magazine.

    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):# Ensure it's an instance of `Magazine`.
            self._magazine = magazine # Set the private attribute '_magazine'
        else:
            return None# Return None if validation fails.
           

class Author:
    def __init__(self, name):
        self.name = name# Set the author's name.

    @property
    def name(self):
        return self._name # Return the author's name.

    @name.setter
    def name(self, name):
        if isinstance(name, str) and name and not hasattr(self, "name"):
            self._name = name # Set the private attribute '_name' if valid.
        else:
            return None  # Return None if validation fails.
            
 # Return a list of articles written by the current author.
    def articles(self):
        return [article for article in Article.all if article.author is self]
 # Return a list of unique magazines the author has written for
    def magazines(self):
        return list({article.magazine for article in self.articles()})
    # Create and return a new Article instance.
    def add_article(self, magazine, title):
        return Article(self, magazine, title)
 
 # Return unique categories of magazines the author has written for.
    def topic_areas(self):
        return (
            list({magazine.category for magazine in self.magazines()})
            if self.magazines()
            else None
        )


class Magazine:
    # Class attribute storing all magazine instances.
    all = []

    def __init__(self, name, category):
        self.name = name # Set the magazine's name.
        self.category = category#set  the magazines category
        type(self).all.append(self) # Add the current instance to the 'all' list.


    @property
    def name(self):
        return self._name # Return the magazine's name.

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name# Set the private attribute '_name'.
        else:
            return None # Return None if validation fails.

            # Return the magazine's category.
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and category:
            self._category = category # Set the private attribute '_category'.
        else:
            return None # Return None if validation fails.
          
    def articles(self):
        return [article for article in Article.all if article.magazine is self]

  # Return a list of articles published in the magazine.
    def contributors(self):
        return list({article.author for article in self.articles()})
    
  # Return a list of article titles if articles exist, else return None.
    def article_titles(self):
        return (
            [article.title for article in self.articles()] if self.articles() else None
        )


 # Return authors with more than two articles in the magazine.
    def contributing_authors(self):
        non_unique_authors = [article.author for article in self.articles()]
        if unique_contributors := list(
            {
                author
                for author in non_unique_authors
                if non_unique_authors.count(author) > 2
            }
        ):
            return unique_contributors
        else:
            None


#Create Authors
author1 = Author("Alice")
author2 = Author("Bob")  

#Create Magazines
magazine1 = Magazine("Tech Daily", "Technology")
magazine2 = Magazine("Gourmet Magazine", "Food")  

#Add Articles
author1.add_article(magazine1, "The Rise of Quantum Computing")
author1.add_article(magazine2, "Best Cooking Tips")
author2.add_article(magazine1, "Future of AI")  

#Display Information
print("Authors:")
print(author1)  # Alice's info
print(author2)  # Bob's info  

print("\nMagazines:")
print(magazine1)  # Tech Daily info
print(magazine2)  # Gourmet Magazine info  

print("\nArticles:")  

#Show all articles directly
for article in Article.all:
    print(article)
