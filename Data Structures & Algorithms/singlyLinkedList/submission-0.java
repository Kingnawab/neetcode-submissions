class List_Node{
    int value;
    List_Node next;
    public List_Node(int value){
        this(value, null);
    }
    // constructor sets next to null by default
    public List_Node(int value, List_Node next){
        this.value = value;
        this.next = next;
    }
}


class LinkedList {
    private List_Node head;
    private List_Node tail;

    public LinkedList() {
        this.head = new List_Node(-1); // creating a dummy node makes removing things easier
        this.tail = this.head;

    }

    public int get(int index) {
        List_Node curr = head.next;
        int i = 0;
        while (curr != null){
            if (i == index){
                return curr.value;
            }
            i++;
            curr = curr.next;
        }
        return -1; // index out of bound or list is empty  
    }

    public void insertHead(int value) {
        List_Node newNode = new List_Node(value);
        newNode.next = head.next;
        head.next = newNode;
        if(newNode.next == null){
            tail = newNode;
        }
        
    }

    public void insertTail(int value) {
        this.tail.next = new List_Node(value);
        this.tail = this.tail.next;
    }

    public boolean remove(int index) {
        int i = 0;
        List_Node curr = this.head;
        while(i < index && curr != null){
            i++;
            curr = curr.next;
        }
        if(curr != null && curr.next != null){
            if (curr.next == this.tail){
                this.tail = curr;
            }
            curr.next = curr.next.next;
            return true;
        }
        return false;
        
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> res = new ArrayList<>();
        List_Node curr = this.head.next;
        while(curr != null){
            res.add(curr.value);
            curr = curr.next;
        }
        return res;

    }
}
