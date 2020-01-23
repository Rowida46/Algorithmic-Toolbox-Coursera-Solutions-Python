package ds;
/**
 *
 * @author Rowida Nagah
 */
public class linkedlist {
    Node head ;
   void addnewItem(int data){
     Node newNode  = new Node(data);
     newNode.getNode(this.head);
     this.head = newNode;
    }
    @Override
    public String toString(){
    Node current = this.head;
    String res = "";
    while(current != null){
    res+= current .toString() +" ,";
    current = current.setNode();
    }
    return res;
    } 
    // to return len odf the linked list
    public int len(){
    Node current = this.head;
    int len_list =0;
    while(current != null){
        len_list ++;
        current = current.setNode();
    }
    return len_list;
    } 
    // to delet and itm
    void pop(){
    this.head = this.head.setNode();
    }
    
    // to search
    public int search(int sr){
    Node current = this.head;
       int found =-1; 
       int len_list =0;
    while(current != null){
        if(sr == current.setdata()){
         found= current.setdata();
        }
       current = current.setNode();
       len_list++;
    }
    return found;
    }}
 
