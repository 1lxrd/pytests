import functions

def test_pulls():
    pulls = [] #list with pull urls
    github_link = 'https://api.github.com/repos/Fantomas42/django-blog-zinnia/pulls'

    answer = functions.getting(github_link)
    for i in answer:
        pulls.append(i["url"]) #adding pull url dict to the list

    pulls_counter = len(pulls) # how many links do we have
    assert pulls_counter == 9, "Amount of pulls should be = 9 "
    print(pulls_counter)
    

def test_branches():

    exp_list = ["dependabot/pip/docs/django-3.1.13", "dependabot/pip/docs/pillow-8.3.2", "develop", "master"] #expected list with branches
    branches = [] # list with branches
    github_link = 'https://api.github.com/repos/Fantomas42/django-blog-zinnia/branches'
    
    answer = functions.getting(github_link)
    print(answer) #print schema of response
    for i in answer:
        branches.append(i["name"]) #adding branch names to the list
    print("\n")

    exp_list.sort()
    branches.sort()
    assert exp_list == branches, "Branches list does not match expected list"

    for i in branches:
        print(i)

    

if __name__ == "__main__":
    test_pulls()
    print("\n")
    test_branches()
