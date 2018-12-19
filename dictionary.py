dict = {'Age': 22, 'Name': 'Tam'}
print("dict[Name]:", dict['Name'])
print("dict[Age]:", dict['Age'])

# Update value existing enties
dict['Age'] = 23
print("dict[Age]:", dict['Age'])
dict.clear()
print(dict)


# Remove all entries
dict.clear()

# Add new entries
dict['Company'] = 'Asian Tech'
print(dict)

# Không thể truy cập chỉ mục index giống list và tuple

# Đối với các kiểu dữ liệu danh sách, nếu không chứa dữ liệu thì giá trị của nó được đánh giá bằng False.
print(bool(0))
print(bool([]))
print(bool({}))
print(bool(""))
print(bool((())))
