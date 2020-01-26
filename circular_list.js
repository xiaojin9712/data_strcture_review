
class Node {
    constructor(data) {
      this.data = data;
      this.next = null;
    }
  }
  
  class CircularLinkedList {
    constructor() {
      this.head = null;
    }
    preappend(data) {
      let node = new Node(data);
      if (!this.head) {
          this.head = node;
          node.next = this.head;
      } else {
        let cur = this.head;
        while(cur.next != this.head) {
          cur = cur.next;
        }
        cur.next = node;
        node.next = this.head;
        this.head = node;
      }
    }
    append(data) {
      let node = new Node(data);
      if (!this.head) {
        this.head = node;
        node.next = this.head;
      } else {
        let cur = this.head;
        while(cur.next != this.head) {
          cur = cur.next;
        }
        cur.next = node;
        node.next = this.head;
      }
    }
    print() {
      let cur = this.head;
      if(cur) {
        console.log(cur.data);
        while(cur.next != this.head) {
          cur = cur.next;
          console.log(cur.data);
        }
      }
    }
    
    split_list() {
      let length = this.length()
      if (length == 0) {
        return null;
      }
      if (length == 1) {
        return this.head;
      }
      let prev = null;
      let cur = this.head;
      let mid = Math.floor(length / 2);
      let count = 0;
      while(cur && count < mid) {
        prev = cur;
        cur = cur.next;
        count += 1;
      }
      prev.next = this.head;
      let splited_list = new CircularLinkedList();
      splited_list.head = cur;
      while(cur.next != this.head) {
        cur = cur.next;
      }
      cur.next = splited_list.head;
      this.print();
      console.log("--split--")
      splited_list.print();
    }
  }
  
  CircularLinkedList.prototype.length = function circuitLength() {
    let cur = this.head
    let count = 0
    while(cur) {
      cur = cur.next;
      count++;
      if (cur == this.head) {
        break
      }
    }
    return count
  }
  
  let node = new Node(2);
  let nodeList = new CircularLinkedList();
  nodeList.append(1);
  nodeList.append(2);
  nodeList.append(3);
  nodeList.append(2);
  nodeList.preappend(0);
  
  // nodeList.print();
  nodeList.split_list();  