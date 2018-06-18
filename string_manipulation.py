# starting string manipulation here

hello = "Gather the thieves of Alibaba"
print(hello.replace("a", "e"))

author = "Kafka"

def pirn():
    for x in range(len(author)):
        print(author[-x])


pirn()

toop = ["Ghana", "Nigeria", "Algeria", "Chicago"]
print(toop.count("Ghana"))


print("cat" + "in" + "hat")

print("\nSawyer" * 3)

print("we hold these truths...".upper())

print("William {}".format("Faulkner"))

auth = "William Faulkner"
year_born = "1897"

print("{} was born in {}.".format(auth, year_born))