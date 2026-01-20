from guizero import App, TextBox, Combo, PushButton, Text, info, Box, ListBox, Window, Picture
dictionary_of_unit = {"mm": 1, "cm": 10, "dm": 100, "m": 1000, "km": 1000000, "g ": 1, "kg ": 1000, "(tấn)ton ": 1000000, "mL": 1, 
                      "L": 1000, "(khối)kL": 1000000, "m^2": 1, "hm^2": 10000, "km^2": 1000000, "cm^3": 1, "dm^3": 1000, "m^3": 1000000, "(giây)seconds": 1, 
                      "(phút)minutes": 60, "(giờ)hours": 3600, "MB": 1, "GB": 1024, "TB": 1048576}
page = 0
rules_window = ""
def check_input_value(): # Kiểm tra giá trị đầu vào có hợp lệ không
    value_input = str(input_value.value).strip()
    if value_input == "" or value_input[0] == "." or value_input[0] == ",":
        return False
    a = []
    for x in value_input:
        if (not x.isdigit()) and x != "," and x != ".":
            value_input = ""
            input_value.value = value_input
            output_value.value = ""
            return False
        if x != ",":
            a.append(x)
        if x == ",":
            a.append(".")
        value_input = "".join(a)
        input_value.value = value_input
    else:
        return True
def change_unit(): # Chuyển đổi đơn vị
    unit_input = input_unit.value
    unit_output = output_unit.value
    if unit_input[-1] == unit_output[-1] and check_input_value():
        value_input = str(input_value.value).strip()
        k = dictionary_of_unit[unit_input] / dictionary_of_unit[unit_output]
        value_output = round(k * float(value_input.removesuffix("\n")), 3)
        if len(str(value_output)) <= 15:
            output_value.value = value_output
            lst_about_your_changes.append(f"{value_input} {unit_input} = {value_output} {unit_output}")
            with open("Bài cuối khóa/calculate_file.txt", "a") as file:
                file.write(f"{value_input} {unit_input} = {value_output} {unit_output}\n")
        else:
            output_value.value = "It's really big"
            lst_about_your_changes.append(f"Error")
            with open("Bài cuối khóa/calculate_file.txt", "a") as file:
                file.write(f"Errorn\n")
    else:
        info("Thông báo", "Không thể chuyển đổi! (Bạn nên nhập số lượng đơn vị cần chuyển đổi là số dương và cho cùng loại đơn vị)")
def change_output_value(): # Đặt giá trị đầu ra thành rỗng
    output_value.value = ""
def clear_all_your_changes(): # Xóa sạch ListBox và file txt
    lst_about_your_changes.clear()
    with open("Bài cuối khóa/calculate_file.txt", "w") as file:
        file.write("")
def what_page(what_change): # Thay đổi trang và kiểm tra trang có hợp lệ
    global page
    page += what_change
    if page > 1:
        page = 1
    if page < 0:
        page = 0
    show_rules()
def show_rules(): # Hiển thị luật lệ
    global page, rules_window
    if page == 0:
        if rules_window != "":
            rules_window.destroy()
        rules_window = Window(app, title = "rule", width = 800)
        welcome_text = Text(rules_window, size = 15, color = "red", text = "Xin chào đến với trang luật của hệ thống chuyển đổi đơn vị!")
        box_rules = Box(rules_window, align = "top", width = 800, height = 450)
        box_text = Box(box_rules, align = "top", width = 800, height = 300)
        rules_text = Text(box_text, size = 15, color = "blue", text = "Đầu tiên là phần chính của cả chương trình, phần chuyển đổi\n" \
                        "đơn vị. Trong ô nhập ở bên trái, bạn sẽ nhập\n" \
                        "một số dương bất kỳ VD: 1; 2; 3; 1.2; 1,4; ... Tiếp theo, bạn\n" \
                        "có thể thấy một cái nút có đơn vị ở bên trên\n" \
                        ", bạn có thể chuyển đổi nó thành đơn vị mà bạn cần chuyển sang\n" \
                        "đơn vị khác. Sau đó, bạn cũng sẽ thấy một cái\n" \
                        "nút có đơn vị ở bên trên tương tự nhưng ở phía bên phải, nó\n" \
                        "chính là đơn vị đầu ra là đơn vị mà bạn cần\n" \
                        "chuyển đổi qua, lúc đó bạn chỉ cần thay đổi thành đơn vị đó\n" \
                        "sang đơn vị bạn muốn chuyển đổi. Nhiệm vụ cuối\n" \
                        "cùng của bạn là ấn vào nút chuyển đổi và chờ kết quả\n" \
                        "xuất hiện ở ô nhập phía bên phải!")
        box_picture = Box(box_rules, align = "top", width = 800, height = 150)
        what_picture = Picture(box_picture, image = "change_unit.png", align = "top")
        change_window_box = Box(box_picture, align = "top", width = 200, height = 100)
        previous_button = PushButton(change_window_box, align = "left", width = 10, height = 2, text = "Previous", command = what_page, args = [-1])
        next_button = PushButton(change_window_box, align = "left", width = 10, height = 2, text = "Next", command = what_page, args = [1])
    elif page == 1:
        if rules_window != "":
            rules_window.destroy()
        rules_window = Window(app, title = "rule", width = 700, height = 650)
        welcome_text = Text(rules_window, size = 15, color = "red", text = "Xin chào đến với trang luật của hệ thống chuyển đổi đơn vị!")
        box_rules = Box(rules_window, align = "top", width = 700, height = 600)
        box_text = Box(box_rules, align = "top", width = 700, height = 150)
        rules_text = Text(box_text, size = 15, color = "blue", text = "Đây là một danh sách lưu trữ lịch sử chuyển đổi đơn vị của\n" \
                    "bạn. Đóng vai trò để bạn không bị quên những\n" \
                    "đơn vị bản thân đã chuyển đổi. Bên cạnh đó, bạn cũng có\n" \
                    "thể thấy một nút clear với chức năng xóa mọi\n" \
                    "lần chuyển đổi đơn vị trước đó. Cuối cùng, hệ thống lưu trữ ra\n" \
                    "file cho phép lưu giữ các lần chuyển đổi trước đó!")
        box_picture = Box(box_rules, align = "top", width = 700, height = 450)
        what_picture = Picture(box_picture, image = "history_of_calculate.png", align = "left")
        unmain_picture = Picture(box_picture, image = "clear_button.png", align = "left")
        change_window_box = Box(box_picture, align = "bottom", width = 200, height = 100)
        previous_button = PushButton(change_window_box, align = "left", width = 10, height = 2, text = "Previous", command = what_page, args = [-1])
        next_button = PushButton(change_window_box, align = "left", width = 10, height = 2, text = "Next", command = what_page, args = [1])
app = App(title = "Máy chuyển đổi đơn vị", width = 515, height = 500, bg = "lightyellow")
Text(app, text = "Chào mừng đã đến với máy chuyển đổi đơn vị!")
change_unit_box = Box(app, align = "top", height = 100, width = 515)
input_value = TextBox(change_unit_box, text = "", width = 12, height = 2, multiline = True, align = "left")
input_value.bg = "white"
input_unit = Combo(change_unit_box, options = dictionary_of_unit.keys(), command = change_output_value, align = "left")
input_unit.bg = "white"
change_unit_button = PushButton(change_unit_box, text = "Chuyển đổi", width = 8, height = 2, command = change_unit, align = "left")
change_unit_button.bg = "lightblue"
output_value = TextBox(change_unit_box, text = "", width = 12, height = 2, multiline = True, align = "left")
output_value.bg = "white"
output_value.disable()
output_unit = Combo(change_unit_box, options = dictionary_of_unit.keys(), command = change_output_value, align = "left")
output_unit.bg = "white"
main_box = Box(app, width = 515, height = 400, align = "top")
your_changes_box = Box(main_box, width = 415, height = 400, align = "left")
lst_about_your_changes = ListBox(your_changes_box, items = [], width = 415, height = 400, align = "left", scrollbar = True)
lst_about_your_changes.bg = "#B4E6BC"
lst_about_your_changes.text_size = 20
with open("Bài cuối khóa/calculate_file.txt", "r") as file:
    for x in file.readlines():
        lst_about_your_changes.append(x.removesuffix("\n"))
box_tools = Box(main_box, width = 100, height = 120, align = "left")
rules_button = PushButton(box_tools, width = 10, height = 2, align = "top", text = "?", command = show_rules)
rules_button.bg = "#9CA7FE"
clear_button = PushButton(box_tools, width = 10, height = 2, align = "top", text = "Clear", command = clear_all_your_changes)
clear_button.bg = "lightblue"

app.display()