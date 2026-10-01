# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# def reverse_list(head):
#     prev = None
#     current = head
    
#     while current:
#         next_node = current.next  # 1. Запоминаем следующий узел
#         current.next = prev        # 2. Разворачиваем указатель
#         prev = current             # 3. Двигаем prev вперед
#         current = next_node        # 4. Двигаем current вперед
        
#     return prev  # Новый head списка
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# reversed_head = reverse_list(head)
# print_list(reversed_head)
#