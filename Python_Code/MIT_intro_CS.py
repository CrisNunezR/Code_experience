"""This code was prepared as solutions to questions and exercises in the online
course "Introduction to Computer Science and Programmming in Python by MIT """

##########Exercise 1:
#Code solves a Towers of Hanoi problem to practice recursive calling    
"""This problem uses recursive calling to move a given number of 'rings' (n)
from one spike (fr) to another spike (to) using a third spike so that no 
ring is places over another one with a smaller 'size' """
def Towers(n, fr, to, spare):
    #this function simply prints out the instruction to move one ring from one spike to another
    def printMove(fr,to):
        print('move from', str(fr),'to',str(to))

    if n==1:                      #simplest problem (or terminal recursive case): just one ring 
        printMove(fr,to)
    else:                                             
        Towers(n-1, fr, spare,to) #really simplifies the problem by assuming I can move
                                  #an (n-1) tower alltogether from 1 spike (fr) to another
                                  #spike (spare). By using recursive calling we move 
                                  #that (n-1) tower from the initial spike (fr) to the spare spike

        Towers(1,fr,to, spare)   #Once moved the (n-1) tower, we move the remaining ring (the bottom ring)
                                 #from the initial spike (fr) to the destination spike (to)

        Towers(n-1,spare,to,fr)  #now, we use recursive calling again to move the (n-1) 
                                 #remaining tower (after placing the bottom ring on the 
                                 # 'to' spike) from the 'spare' spike (where we placed it
                                 # with the first recursive block) to the destination spike (to)


##########Exercise 2:
"""this code checks a text to validate if it reads the same forwards and backwards"""

##this supporting function includes only letter characters on the string, 
#omitting all chars that aren't
def clean_text(st):
    ans=''
    st=st.lower()
    for c in st:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            ans = ans + c
    return ans

#is_pali('Able was I, ere I saw Elba')
#is_pali('Are we not drawn onward, we few, drawn onward to new era?')
#is_pali('Abba')

#a more efficient way to do the palindrome code
def is_pali(s):

    s=clean_text(s) #first we clean the text to work just with lower case characters
    
    #then we use recursive calling, reviewing the text's 1st and last char and then 
    #call recursively with the remaining text (which excludes the 1st and last char)
    #notice that in order to return 'True' all recursive calls must return True
    if len(s)<=1:
        return True
    else:
        return (s[0]==s[-1] and is_pali(s[1:-1]))


##########Exercise 3: Search and Sorting

#Linear or simple search
#List in wich we search need not be sorted. Efficiency O(n)
def norm_search(L, x):
    res = False
    for i in L:
        #print(x, '=',i,'?')
        if i == x:
            res = True #notice that we continue reviewing the list even when we found a match
    return res


#ordered search
#This search needs to receive an ordered list. Notice that Sorting has O(nlogn) complexity.
#this must be added to the search (thus this can make sense if many searches are needed - with one ordering process)
def ordered_search(L,x):
    for i in L:
        if x == i:
            return True #this avoids reviewing the whole list
    return False

#bisection search
#notice that this algorithm also assumes the List is ordered
#it compares fewer elements which makes its sorting time O(log n)
#(without considering the time to sort the list)
def bisec_search(L,x):
    res = False
    if L[0] == x or L[-1] == x or x == L[int((len(L))/2)]:
        return True
    else:
        if x < L[int((0+len(L))/2)] and len(L)>2:
            res = bisec_search(L[0:int((len(L))/2)],x)
        else:
            if len(L)<=2:
                return False
            n = int((0+len(L))/2)
            res = bisec_search(L[n:len(L)],x)
    return res


#Sorting - Bubble sort
#This sorting algorithm takes the 1st element of a list and compares it to 
# every other element. If the element is larger than another value, we 'switch places'
# and continue. The algorith stops when we go through the list without switching
def bubble_sort(L):
    did_swap = False
    for i in range(len(L)-1):
        if L[i]>L[i+1]:
            buffer = L[i]
            L[i] = L[i+1]
            L[i+1] = buffer
            did_swap = True
            #print('swap',L[i],'for', L[i+1])
    
    if did_swap == True:
        bubble_sort(L)
        
    return L
        
#Merge-sort algorithm 
#This is a O(n*logn) algorithm and it is quite "memory consuming" since 
# we need to store many smaller sorted bits
def merge_sort(L):    

    """This function 'disects' a list in 2 equal parts (L1 and L2) and continue dividing 
    until we get a 1-element list (notice that a one element list is 'always ordered') using
    the recursive_merve function. This function calls itself recursively until arriving  at
    2 ordered sections (L1 and L2 angain... each one with size app L/2)
    
    To order the sections, I use function order_merge. This function begins by taking 
    2 1-element lists and ordering them into one merged list (at the limit of the recursion).
    After that, the function begins ordering and merging 2 lists by comparing the 1st element
    of the 2 lists (notice that each list is already ordered at this point) and then recursively
    calling the remainder of the list with the smallest element (ex: L[1:len(L1)]) with the other list"""
    def order_merge(L1,L2,merged):
        if L1[0]<L2[0]:
            #notice that we have both lists ordered so we are sure here L1[0] is the smallest element in the whole list
            merged.append(L1[0]) 
            #since I took an element from L1, I recursively call the function again 
            # with the remaining elements in L1 (L[1:len(L1)]) and L2
            if len(L1)>1:
                order_merge(L1[1:len(L1)],L2,merged)
            else:
                merged.extend(L2)   #If L1 has just 1 element, I can just add L2 since 
                                    #I know it's ordered and L1[0] < L2[0], so 
                                    #all elements in L2 are larger that the last element in L1
        else:
            #here we follow the same precedure but knowing that L2 has the smallest 1st element
            merged.append(L2[0])
            if len(L2)>1:
                order_merge(L1,L2[1:len(L2)], merged)
            else:
                merged.extend(L1)
        return merged
    
    #recursive call -- very elegant way to feed the blocks (source: MIT)
    def recursive_merge(L):
        #if i've devided the list up to single elements, return the element
        if len(L) < 2:          
            return L[:] #notice that a 1-element list is 'always ordered'
        else:
            middle = len(L)//2  #otherwise, keep recursively diving 
            L1 = recursive_merge(L[:middle])
            L2 = recursive_merge(L[middle:])
            return order_merge(L1,L2,[])
        
    return recursive_merge(L)








#main that executes the different solutions
def main():
    
    #runs Hanoi towers with 3 rings
    Towers(3, 'A', 'B', 'C')
    
    #runs validation of palindrome text 
    text = 'Abba'
    print("Checking text '" + text + "' for palindrome: " + str(is_pali('Abba')))


    #runs sorting and searching algorithms
    #first, let's define a list to search in
    L=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,256,23,42,245,23,31,58,3,2325,231,124,52,3,3,1342,523,34,23523,235,141,521341,13513,523531,13,14341]
    x = 23523
    print("We'll search in L:" + str(L))
    import time

    #runs normal/linear search 
    print("normal search:")
    t0 = time.perf_counter()
    print(("Is " + str(x) + " in L? " + str(norm_search(L, 14))))
    t1 = time.perf_counter()
    print("Time to execute: " + str(t1-t0))

    #runs an ordered search
    print("ordered search:")
    L = sorted(L)
    t0 = time.perf_counter()
    print(("Is " + str(x) + " in L? " + str(ordered_search(L,x))))
    t1 = time.perf_counter()
    print("Time to execute: " + str(t1-t0))

    #runs an ordered search
    print("binary search:")
    L = sorted(L)
    t0 = time.perf_counter()
    print(("Is " + str(x) + " in L? " + str(bisec_search(L,x))))
    t1 = time.perf_counter()
    print("Time to execute: " + str(t1-t0))

    #runs sorting algorith - bubble sort
    import random
    random.shuffle(L)
    bubble_sort(L)
    print(L)


if __name__ == "__main__":
    main()