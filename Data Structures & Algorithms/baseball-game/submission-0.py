class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record = []
        for e in operations:
            if e.isnumeric() or '-' in e:
                record.append(int(e))
            elif e == '+':
                record.append(record[-1]+record[-2])
            elif e == 'D':
                record.append(record[-1]*2)
            else:
                record.pop()
        return sum(record)