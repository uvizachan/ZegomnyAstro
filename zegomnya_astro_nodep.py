def calculate_constellation(position):
    constellations = [
        "Ashldru'cu", "Bharu'm", "Kitr'm", "Chast'tnai", "Mirighir'm",
        "Rhadr'm", "Wasy'm", "B'hustta", "Asch'chm", "M'hahm", "Faghl'm",
        "Fuhgum'm", "Ghastm'm", "Chyin'tte", "Sh'chatte", "Wyishuk'mu",
        "Ryidhntte", "Yieschtte", "Mulh'mu", "Aschtte", "Schadh'atte",
        "Ch'rvan'mu", "Yanu'shtte", "Chahabtte", "Bapra'm", "Praha'm",
        "Er'hatte"
    ]

    index = int(position / 13.33) % len(constellations)
    constellation = constellations[index]

    quarter = int((position % 90) / 22.5) + 1

    return constellation, quarter


def get_positions(hours, days, months, years):
    base_hour = 86400 / 27
    base_day = base_hour * 27
    base_month = base_day * 9 * 3
    base_year = base_month * 10

    time = hours * base_hour + days * base_day + months * 10 * base_day + years * base_year

    bhyianvua_orbits, bhyianvua_remainder = divmod(time, (27.025 * base_day * 10))
    bhyianvua_position = (360 * bhyianvua_remainder / (27.025 * base_day * 10)) % 360

    yindni_days, yindni_seconds = divmod(time, (27.01 * base_day))
    yindni_position = (360 * yindni_seconds / (27.01 * base_day)) % 360

    ruagdi_orbits, ruagdi_remainder = divmod(time, (2700.1 * base_day))
    ruagdi_position = (360 * ruagdi_remainder / (2700.1 * base_day)) % 360

    khyietdi_orbits, khyietdi_remainder = divmod(time, (2700.1 * base_day))
    khyietdi_position = (180 + (360 * khyietdi_remainder / (2700.1 * base_day))) % 360

    bhamhvaua_orbits, bhamhvaua_remainder = divmod(time, (40.73 * base_day))
    bhamhvaua_position = (360 * bhamhvaua_remainder / (40.73 * base_day)) % 360

    sumyiavdi_orbits, sumyiavdi_remainder = divmod(time, (27.04 * base_day))
    sumyiavdi_position = (360 * sumyiavdi_remainder / (27.04 * base_day)) % 360

    gyurvua_orbits, gyurvua_remainder = divmod(time, (81.02 * base_day))
    gyurvua_position = (360 * gyurvua_remainder / (81.02 * base_day)) % 360

    bhirguvni_orbits, bhirguvni_remainder = divmod(time, (40.55 * base_day))
    bhirguvni_position = (360 * bhirguvni_remainder / (40.55 * base_day)) % 360

    sthyirvni_orbits, sthyirvni_remainder = divmod(time, (81.04 * base_day))
    sthyirvni_position = (360 * sthyirvni_remainder / (81.04 * base_day)) % 360

    return (
        bhyianvua_position, yindni_position, ruagdi_position, khyietdi_position,
        bhamhvaua_position, sumyiavdi_position, gyurvua_position, bhirguvni_position, sthyirvni_position
    )


def display_constellations(hours, days, months, years):
    (
        bhyianvua_position, yindni_position, ruagdi_position, khyietdi_position,
        bhamhvaua_position, sumyiavdi_position, gyurvua_position, bhirguvni_position, sthyirvni_position
    ) = get_positions(hours, days, months, years)

    bhyianvua_constellation, bhyianvua_quarter = calculate_constellation(bhyianvua_position)
    yindni_constellation, yindni_quarter = calculate_constellation(yindni_position)
    ruagdi_constellation, ruagdi_quarter = calculate_constellation(ruagdi_position)
    khyietdi_constellation, khyietdi_quarter = calculate_constellation(khyietdi_position)
    bhamhvaua_constellation, bhamhvaua_quarter = calculate_constellation(bhamhvaua_position)
    sumyiavdi_constellation, sumyiavdi_quarter = calculate_constellation(sumyiavdi_position)
    gyurvua_constellation, gyurvua_quarter = calculate_constellation(gyurvua_position)
    bhirguvni_constellation, bhirguvni_quarter = calculate_constellation(bhirguvni_position)
    sthyirvni_constellation, sthyirvni_quarter = calculate_constellation(sthyirvni_position)

    table = [
        ["Body", "Position", "Quarter", "Constellation"],
        ["Bhyianv'ua", f"{bhyianvua_position:.2f}°", bhyianvua_quarter, bhyianvua_constellation],
        ["Yind'ni", f"{yindni_position:.2f}°", yindni_quarter, yindni_constellation],
        ["Ruag'di", f"{ruagdi_position:.2f}°", ruagdi_quarter, ruagdi_constellation],
        ["Khyiet'di", f"{khyietdi_position:.2f}°", khyietdi_quarter, khyietdi_constellation],
        ["Bhamh'vaua", f"{bhamhvaua_position:.2f}°", bhamhvaua_quarter, bhamhvaua_constellation],
        ["Sumyia'vdi", f"{sumyiavdi_position:.2f}°", sumyiavdi_quarter, sumyiavdi_constellation],
        ["Gyurv'ua", f"{gyurvua_position:.2f}°", gyurvua_quarter, gyurvua_constellation],
        ["Bhirg'uvni", f"{bhirguvni_position:.2f}°", bhirguvni_quarter, bhirguvni_constellation],
        ["Sthyirv'ni", f"{sthyirvni_position:.2f}°", sthyirvni_quarter, sthyirvni_constellation]
    ]

    # Generate the formatted table
    formatted_table = ""
    for row in table:
        formatted_row = " | ".join(str(cell).center(12) for cell in row)
        formatted_table += f"{formatted_row}\n"
    
    print(formatted_table)

def validate_input(prompt, min_value, max_value):
    while True:
        try:
            value = float(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_user_input():
    hours = validate_input("Enter the number of hours: ", 0, 26)
    days = validate_input("Enter the number of days: ", 0, 26)
    months = validate_input("Enter the number of months: ", 0, 9)
    years = validate_input("Enter the current year: ", 0, float('inf'))
    return hours, days, months, years

# Get user input for the time
hours, days, months, years = get_user_input()

# Display the constellations at the specified time
display_constellations(hours, days, months, years)
