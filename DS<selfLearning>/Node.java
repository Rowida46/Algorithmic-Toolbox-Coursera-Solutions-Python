
package ds;

/**
 *
 * @author Rowida Nagah
 */
public class Node {
  int data ;
    Node nextNode;
    Node(int data){
    this.data = data;
    }
   
    void getNode(Node nextNode){
    this.nextNode = nextNode; 
    }
    
    void getdata(int data){
    this.data = data;
    }
    
    int setdata(){
    return data;}

    Node setNode(){
    return this.nextNode;
    }

    
  // to print data
    @Override
    public String toString(){
    
    return "node" +  this.data;
    } 


}
