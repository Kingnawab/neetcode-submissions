class DynamicArray {
    private int length;
    private int capacity;
    private int [] array;
// this is a constructor that initalizes the dynamic array
    public DynamicArray(int capacity) {
        this.capacity = capacity;
        this.length = length;
        this.array = new int[this.capacity];

    }

    public int get(int i) {
        return array[i];

    }

    public void set(int i, int n) {
        array[i] = n;

    }
// this should insert the element at the last poisition of the array
    public void pushback(int n) {
        if(capacity == length){
            resize();
        }
        array[length] = n;
        length ++;

    }

    public int popback() {
        // this soft deletes the element in the end of the list
        if(length > 0){
            length --;
        }
        return array[length];
    }

    private void resize() {
        capacity = capacity * 2;
        int [] new_array = new int[capacity];
        for(int i = 0; i < length; i ++){
            new_array[i] = array[i];
        }
        array = new_array;


    }

    public int getSize() {
        return length;

    }

    public int getCapacity() {
        return capacity;

    }
}
