import abc
import weakref


# Step 1. Create an abstract base class, called Media, that contains
#         a title and release_date attributes



# Step 2. Create a Movie class that inherits from Media.
#         In addition to the inherited properties, a Movie class also
#         provides a revenue, runtime, tagline, and budget attributes,
#         Note: you may want to handle any extra keywords passed into the constructor as well


# Step 3. Create a Descriptor class called ReadOnly (place it above the other two class definitions).
#         that have a __get__ and __set__ method.  The __set__ should not allow the title to be
#         changed once it is set.
#
#         One way to do this is to check if the title has ever been set.  If so, then
#         we disallow changes to it.  Perhaps something like the following:
#
#                 if not self.data.get(instance):
#                     self.data[instance] = value
#
#         This check if the title for the instance as ever been set, if not then set it.
#
#         Apply the descriptor to the Media class as learned in the discussions.
