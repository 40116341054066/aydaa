class Node:
    def init(self, coefficient, power):
        self.coefficient = coefficient
        self.power = power
        self.next = None

class LinkedList:
    def init(self):
        self.head = None

    def add_node(self, coefficient, power):
        new_node = Node(coefficient, power)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(f"{current.coefficient}x^{current.power}", end=" ")
            current = current.next
        print()

def add_polynomials(poly1, poly2):
    result = LinkedList()
    current1 = poly1.head
    current2 = poly2.head

    while current1 and current2:
        if current1.power > current2.power:
            result.add_node(current1.coefficient, current1.power)
            current1 = current1.next
        elif current1.power < current2.power:
            result.add_node(current2.coefficient, current2.power)
            current2 = current2.next
        else:
            result.add_node(current1.coefficient + current2.coefficient, current1.power)
            current1 = current1.next
            current2 = current2.next

    while current1:
        result.add_node(current1.coefficient, current1.power)
        current1 = current1.next

    while current2:
        result.add_node(current2.coefficient, current2.power)
        current2 = current2.next

    return result

def multiply_polynomials(poly1, poly2):
    result = LinkedList()
    current1 = poly1.head

    while current1:
        current2 = poly2.head
        while current2:
            coefficient = current1.coefficient * current2.coefficient
            power = current1.power + current2.power
            result.add_node(coefficient, power)
            current2 = current2.next
        current1 = current1.next

    return result

ساخت چند جمله‌ای اول
poly1 = LinkedList()
poly1.add_node(5, 2)
poly1.add_node(3, 1)
poly1.add_node(2, 0)

نمایش چند جمله‌ای اول
print("چند جمله‌ای اول:")
poly1.display()

ساخت چند جمله‌ای دوم
poly2 = LinkedList()
poly2.add_node(4, 2)
poly2.add_node(1, 0)

نمایش چند جمله‌ای دوم
print("چند جمله‌ای دوم:")
poly2.display()

جمع دو چند جمله‌ای
sum_poly = add_polynomials(poly1, poly2)
print("حاصل جمع دو چند جمله‌ای:")
sum_poly.display()

ضرب دو چند جمله‌ای
mul_poly = multiply_polynomials(poly1, poly2)
print("حاصل ضرب دو چند جمله‌ای:")
mul_poly.display()
