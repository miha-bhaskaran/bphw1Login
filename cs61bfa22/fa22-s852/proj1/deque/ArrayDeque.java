package deque;

public class ArrayDeque <T> {
    private T[] items;
    private int nextFirst;
    private int nextLast;
    private int size;
    private static final int DEFAULT_SIZE = 8;

    public ArrayDeque() {
        items = (T[]) new Object[DEFAULT_SIZE];
        nextFirst = 0;
        nextLast = 1;
        size = 0;
    }
    public void addFirst(T item) {
        if (size == items.length) {
            resizeUp();
        }

        items[nextFirst] = item;
        nextFirst = (nextFirst - 1 + items.length) % items.length;
        size++;


    }

    public void addLast(T item) {
        if (size == items.length) {
            resizeUp();
        }

        items[nextLast] = item;
        nextFirst = (nextFirst + 1) % items.length;
        size++;


    }
    private void resizeUp() {
        T[] newItems = (T[]) new Object[items.length *2];
        int sizeOfFront = items.length - nextLast;
        System.arraycopy(items,(nextFirst +1) % items.length
                ,newItems, 0, sizeOfFront);
        System.arraycopy(items, 0, newItems, sizeOfFront, items.length - sizeOfFront);

        items = newItems;
        nextFirst = items.length - 1;
        nextLast = size;
    }
    private void resizeDown() {
        T[] newItems = (T[]) new Object[items.length / 2];
        int sizeOfFront;
        if (nextLast > nextFirst) {
            sizeOfFront = nextLast - nextFirst -1;
        } else {
            sizeOfFront = items.length - nextFirst - 1;
        }

        System.arraycopy(items, (nextFirst + 1) % items.length, newItems, 0, sizeOfFront);
        System.arraycopy(items, 0, newItems, sizeOfFront, newItems.length - sizeOfFront);

        items = newItems;
        nextFirst = items.length - 1;
        nextLast = size;

    }

    public T removeFirst() {
       if (isEmpty()) {
           return null;
       }
       if (items.length > DEFAULT_SIZE && size <= 0.25 * items.length) {
           resizeDown();
       }

       int newFirst = (nextFirst + 1) % items.length;
       T item = items[newFirst];
       nextFirst = newFirst;
       size--;
       return item;



    }
    public T removeLast() {
        if (isEmpty()) {
            return null;
        }
        if (items.length > DEFAULT_SIZE && size <= 0.25 * items.length) {
            resizeDown();
        }

        int newLast = (nextLast - 1 + items.length) % items.length;
        T item = items[newLast];
        nextLast = newLast;
        size--;
        return item;

    }
    public boolean isEmpty() {
        return size == 0;

    }
    public int size(){
        return size;
    }
    public void printDeque() {
        for (int i = 0; i < items.length; i++) {
            System.out.println(get(i) + " ");
        }
    }
    public T get(int index) {
        return items[(nextFirst + 1 + index) % items.length];

    }
    public boolean equals(Object o) {
        if (!(o instanceof ArrayDeque)) {
            return false;
        }
        ArrayDeque<T> other = (ArrayDeque<T>) o;
        if (other.size != size()) {
            return false;
        }
        for (int i = 0; i <  size; i++) {
            if (!get(i).equals(other.get(i))) {
                return false;
            }
        }
        return true;



    }

}
