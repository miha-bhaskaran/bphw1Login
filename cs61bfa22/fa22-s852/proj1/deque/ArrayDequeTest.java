package deque;
import org.junit.Test;
import static org.junit.Assert.*;

public class ArrayDequeTest {
    @Test
    public void test() {
        ArrayDeque l = new ArrayDeque<>();
        for (int i = 0; i < 32; i++) {
            l.addLast(i);


        }
        for (int i = 0; i < 32; i++) {
            assertEquals(i, (int) l.removeFirst());
        }

    }
}
