public class Reverse
{
    static Node head;

    public static class Node {
        int data;
        Node next;

        public Node(int data) {
            this.data = data;
            this.next = null;
        }

        public static Node InsertNode(int data) {
            Node newNode = new Node(data);
            newNode.next = head;
            head = newNode;
            return newNode;
        }

        public static void PrintList() {
            Node curr = head;
            while (curr != null) {
                System.out.println(curr.data + " ");
                curr = curr.next;
            }
        }

        public static void ReverseNodes()
        {
            Node curr = Reverse.head;
            Node prev = null;

            while(curr != null)
            {
                Node nextTmp = curr.next;
                curr.next = prev;
                prev = curr;
                curr = nextTmp;
            }
            head = prev;
        }
    }
    
    public static void main(String[] args) {
        
        Reverse.head = Node.InsertNode(7);
        Node.InsertNode(9);
        Node.InsertNode(3);

        Node.PrintList();
        Node.ReverseNodes();
        System.out.println();

        Node.PrintList();
    }
}