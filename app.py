# Danh sách để lưu các công việc
tasks = []
def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append(task_name)
    print(f"Đã thêm công việc: '{task_name}'")

def list_task(tasks):
    for i in tasks:
        if i["completed"] == "True":
            print(f'[x] {i["name"]}')
        else:
            print(f'[ ] {i["name"]}')

def complete_task(task_index):
    if 0 <= task_index <= len(tasks):
        for i in range(len(tasks)):
            if (task_index - 1 == i):
                tasks[i]["completed"] = "True"
                print('Đã hoàn thành công việc!!!')
    else:
        print('Chỉ số không hợp lệ, không thể hoàn thành')

def delete_task(task_index):
    if 0 <= task_index <= len(tasks):
        for i in range(len(tasks)):
            if task_index - 1 == i:
                del tasks[task_index-1]
                print(f'Đã xóa công việc!!!')
    else:
        print('Chỉ số không hợp lệ, không thể xóa')


# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    n = int(input('Nhập số công việc cần ghi chú: '))
    for i in range(n):
        name = input('Nhập tên công việc: ')
        completed = input('Nhập trạng thái hoàn thành: ')

        dic = {"name" : name, "completed" : completed}
        add_task(dic)
    
    index_1 = int(input('Nhập vị trí hoàn thành công việc: '))
    complete_task(index_1)
    print('Danh sách công việc:')
    list_task(tasks)

    index_2 = int(input('Nhập vị trí công việc cần xóa: '))
    delete_task(index_2)
    print('Danh sách công việc sau khi xóa')
    list_task(tasks)




