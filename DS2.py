from collections import Counter # not loaded by default
def not_the_same(user, other_user):
 """two users are not the same if they have different ids"""
 return user["id"] != other_user["id"]
def not_friends(user, other_user):
 """other_user is not a friend if he's not in user["friends"];
 that is, if he's not_the_same as all the people in user["friends"]"""
 return all(not_the_same(friend, other_user)
 for friend in user["friends"])
def friends_of_friend_ids(user):
 return Counter(foaf["id"]
 for friend in user["friends"] # for each of my friends
 for foaf in friend["friends"] # count *their* friends
 if not_the_same(user, foaf) # who aren't me
 and not_friends(user, foaf)) # and aren't my friends
print friends_of_friend_ids(users[3]) # Counter({0: 2, 5: 1})