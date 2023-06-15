import linked_list
import cmd 
import argparse 
file = 'PQ.txt'


class PQ(cmd.Cmd):
    ## sanitize file -- if doesn't exist create it 
    new_file = open(file, "r").readlines()
    new_file = [line.rstrip('\n') for line in new_file]
    ll = linked_list.LinkedList()
    queue = ll.from_file(new_file)



    def do_add(self, line):
        parser = argparse.ArgumentParser(description="add item to queue")
        parser.add_argument('value', nargs="+", help="item on the agenda")
        parser.add_argument('priority', type=int, help="priority of item")
        args = parser.parse_args(line.split())
        value = ' '.join(args.value)
        p = args.priority
        
        self.queue.add(value, p)
        self.queue.to_file(file)
        self.do_p_1_2("")
        return 
    
    def do_a(self, line):
        return self.do_add(line)

    
    def do_remove(self, number):
        if number:
            self.queue.remove(int(number))
            self.queue.to_file(file)
            self.do_p_1_2("")
            return 
        else:
            print("need number")
    
    def do_r(self, number):
        return self.do_remove(number)


    def do_p(self, line):
        arr = self.queue.print()
        for i in arr:
            print(i)
        print("")
        return 
    
    def do_p_1_2(self, line):
        arr = self.queue.print_1_2()
        for i in arr:
            print(i)
        print("")
        return 


    def do_pop(self, line):
        print(self.queue.pop())
        self.queue.to_file(file)
        self.do_p_1_2("")
        return
    
    def do_limit(self, line):
        ret = self.queue.head_pop(int(line))
        for i in ret:
            print(i)
        return 
    
    def do_l(self, line):
        self.do_limit(line)
        return 
    
    def do_pchange(self, line):
        parser = argparse.ArgumentParser(description="add item to queue")
        parser.add_argument('number', type=int, help="item on the agenda")
        parser.add_argument('priority', type=int, help="priority of item")
        args = parser.parse_args(line.split())

        if self.queue.change_priority(args.number, args.priority) != None:
            self.queue.to_file(file)
            self.do_p("")
            return 
        else:
            print("not a legitimate number")
            return 
    
    def do_rename(self, line):
        parser = argparse.ArgumentParser(description="add item to queue")
        parser.add_argument('number', type=int, help="item on the agenda")
        parser.add_argument('name', nargs="+", help="rename item on the agenda")

        args = parser.parse_args(line.split())
        name = ' '.join(args.name)
        print(args)
        self.queue.rename(args.number, name)
        self.do_p_1_2("")
        return 


    def do_clear(self, line):
        self.queue.clear(file)
        return 
    
    def do_EOF(self, line):
        return True
    
    def do_exit(self, line):
        return True
    
    def do_e(self, line):
        return True



    ## open file by creating the Q which will read it

    ## put the file into a priority Q

    ## the q should be a class and have methods

    ## do stuff -- every do stuff should have a save immediatly afterwards 
  
    
    ## exit


if __name__ == '__main__':
    PQ().cmdloop()

