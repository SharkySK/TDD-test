class Tested:
    def comparing(first, second):
        for ele in first:  # for each element in first list
            if ele in second:  # is present in second list
                continue  # then continue with other elements
            return False  # ele present in first and not in second,return false
        return True


