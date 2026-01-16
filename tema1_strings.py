raw_logs = [
    "  ERROR | Voltage too LOW | code=E12  ",
    " info | System started successfully ",
    " WARNING | High temperature detected | code=W07 ",
    " ERROR | Communication timeout | code=E99 ",
    " info | System shutdown complete "
]
for log in raw_logs:
    log = log.strip().lower()  # curățare
    parts = log.split("|")  # split

    level = parts[0].strip()

    print("LOG SUMMARY")
    print("----------")
    print("Errors   :", )
    print("Warnings :", )
    print("Info     :", )
    print()