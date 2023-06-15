import linked_list
def ll_print(ll):
    arr = ll.print()
    for i in arr:
        print(i)

def test1():
    ll = linked_list.LinkedList()
    ll.add("first", 0)
    ll.add("second", 1)
    ll.add("third", 1)
    ll.add("four", 0)
    ll.add("five", 2)
    ll.add("six", 4)
    ll_print(ll)
    print("")
    ll.pop()
    ll_print(ll)
    ll.remove(1)
    print("")
    ll_print(ll)
    ll.rename(3, "add new zones for redis")
    print("")
    ll_print(ll)
    print("")
    ll.change_priority(5, 2)
    ll_print(ll)
    
    

def main():
    test1()

if __name__ == '__main__':
    main()
