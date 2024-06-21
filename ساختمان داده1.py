class Page:
    def init(self, content):
        self.content = content

    def get_element_at_index(self, i):
        if 0 <= i < len(self.content):
            return self.content[i]
        else:
            return "Index out of range"

مثال استفاده
my_page = Page(["Hello", "World", "Python", "is", "awesome"])
index = 2
element = my_page.get_element_at_index(index)
print(element)
