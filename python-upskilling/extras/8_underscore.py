class Underscore:
    def map(self, iterable, callback):
        mapped_list = []
        for item in iterable:
            mapped_list.append(callback(item))
        return mapped_list
    
    def find(self, iterable, callback):
        for item in iterable:
            if callback(item):
                return item
        return None
    
    def filter(self, iterable, callback):
        filtered_list = []
        for item in iterable:
            if callback(item):
                filtered_list.append(item)
        return filtered_list
    
    def reject(self, iterable, callback):
        rejected_list = []
        for item in iterable:
            if not callback(item):
                rejected_list.append(item)
        return rejected_list

_ = Underscore()

mapped_result = _.map([1, 2, 3], lambda x: x * 2)
print("Mapped result:", mapped_result)
print("===================")

found_result = _.find([1, 2, 3, 4, 5, 6], lambda x: x > 4)
print("Found result:", found_result)
print("===================")

filtered_result = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print("Filtered result:", filtered_result)
print("===================")

rejected_result = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print("Rejected result:", rejected_result)
