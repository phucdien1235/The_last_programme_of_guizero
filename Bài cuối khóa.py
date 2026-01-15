from guizero import App, TextBox, Combo, PushButton, Text, info, Box, ListBox
dictionary_of_unit = {"mm": 1, "cm": 10, "dm": 100, "m": 1000, "km": 1000000, "g ": 1, "kg ": 1000, "(tấn)ton ": 1000000, "mL": 1, 
                      "L": 1000, "(khối)kL": 1000000, "m^2": 1, "hm^2": 10000, "km^2": 1000000, "cm^3": 1, "dm^3": 1000, "m^3": 1000000, "(giây)seconds": 1, 
                      "(phút)minutes": 60, "(giờ)hours": 3600, "MB": 1, "GB": 1024, "TB": 1048576}
def check_input_value():
    value_input = str(input_value.value).strip()
    if value_input == "":
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
def change_unit():
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
def change_output_value():
    output_value.value = ""
def clear_all_your_changes():
    lst_about_your_changes.clear()
    with open("Bài cuối khóa/calculate_file.txt", "w") as file:
        file.write("")
app = App(title = "Máy chuyển đổi đơn vị", width = 515, height = 500, bg = "lightyellow")
Text(app, text = "Chào mừng đã đến với máy chuyển đổi đơn vị!")
change_unit_box = Box(app, align = "top", height = 100, width = 515)
input_value = TextBox(change_unit_box, text = "", width = 12, height = 2, multiline = True, align = "left")
input_value.bg = "white"
input_unit = Combo(change_unit_box, options = ['mm', 'cm', 'dm', 'm', 'km', 'g ', 'kg ', '(tấn)ton ', 'mL', 'L', '(khối)kL', 'm^2', 'hm^2', 
                                   'km^2', 'cm^3', 'dm^3', 'm^3', '(giây)seconds', '(phút)minutes', '(giờ)hours', 'MB', 'GB', 'TB'], command = change_output_value, align = "left")
input_unit.bg = "white"
change_unit_button = PushButton(change_unit_box, text = "Chuyển đổi", width = 8, height = 2, command = change_unit, align = "left")
change_unit_button.bg = "lightblue"
output_value = TextBox(change_unit_box, text = "", width = 12, height = 2, multiline = True, align = "left")
output_value.bg = "white"
output_value.disable()
output_unit = Combo(change_unit_box, options = ['mm', 'cm', 'dm', 'm', 'km', 'g ', 'kg ', '(tấn)ton ', 'mL', 'L', '(khối)kL', 'm^2', 'hm^2', 
                                    'km^2', 'cm^3', 'dm^3', 'm^3', '(giây)seconds', '(phút)minutes', '(giờ)hours', 'MB', 'GB', 'TB'], command = change_output_value, align = "left")
output_unit.bg = "white"
your_changes_box = Box(app, width = 515, height = 400, align = "top")
lst_about_your_changes = ListBox(your_changes_box, items = [], width = 415, height = 400, align = "left", scrollbar = True)
lst_about_your_changes.bg = "#B4E6BC"
with open("Bài cuối khóa/calculate_file.txt", "r") as file:
    for x in file.readlines():
        lst_about_your_changes.append(x.removesuffix("\n"))
clear_button = PushButton(your_changes_box, width = 10, height = 2, align = "left", text = "Clear", command = clear_all_your_changes)
clear_button.bg = "lightblue"

app.display()