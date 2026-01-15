from guizero import App, TextBox, Combo, PushButton, Text, info
dictionary_of_unit = {"mm": 1, "cm": 10, "dm": 100, "m": 1000, "km": 1000000, "g ": 1, "kg ": 1000, "(tấn)ton ": 1000000, "mL": 1, 
                      "L": 1000, "(khối)kL": 1000000, "m^2": 1, "hm^2": 10000, "km^2": 1000000, "cm^3": 1, "dm^3": 1000, "m^3": 1000000, "(giây)seconds": 1, 
                      "(phút)minutes": 60, "(giờ)hours": 3600, "MB": 1, "GB": 1024, "TB": 1048576}
def check_input_value():
    value_input = str(input_value.value).strip()
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
        value_input = input_value.value
        k = dictionary_of_unit[unit_input] / dictionary_of_unit[unit_output]
        output_value.value = k * float(value_input.removesuffix("\n"))
    else:
        info("Thông báo", "Không thể chuyển đổi! (Bạn nên nhập số lượng đơn vị cần chuyển đổi là số dương và cho cùng loại đơn vị)")
def change_output_value():
    output_value.value = ""
app = App(title = "Máy chuyển đổi đơn vị", width = 420, height = 100, bg = "lightyellow")
Text(app, text = "Chào mừng đã đến với máy chuyển đổi đơn vị!")
input_value = TextBox(app, text = "", width = 12, height = 2, align = "left", multiline = True)
input_value.bg = "white"
input_unit = Combo(app, options = ['mm', 'cm', 'dm', 'm', 'km', 'g ', 'kg ', '(tấn)ton ', 'mL', 'L', '(khối)kL', 'm^2', 'hm^2', 
                                   'km^2', 'cm^3', 'dm^3', 'm^3', '(giây)seconds', '(phút)minutes', '(giờ)hours', 'MB', 'GB', 'TB'], align = "left", command = change_output_value)
input_unit.bg = "white"
change_unit_button = PushButton(app, text = "Chuyển đổi", width = 8, height = 2, align = "left", command = change_unit)
change_unit_button.bg = "lightblue"
output_value = TextBox(app, text = "", width = 12, height = 2, align = "left", multiline = True)
output_value.bg = "white"
output_value.disable()
output_unit = Combo(app, options = ['mm', 'cm', 'dm', 'm', 'km', 'g ', 'kg ', '(tấn)ton ', 'mL', 'L', '(khối)kL', 'm^2', 'hm^2', 
                                    'km^2', 'cm^3', 'dm^3', 'm^3', '(giây)seconds', '(phút)minutes', '(giờ)hours', 'MB', 'GB', 'TB'], align = "left", command = change_output_value)
output_unit.bg = "white"

app.display()