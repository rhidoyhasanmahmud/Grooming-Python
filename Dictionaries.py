studentId = {
    "101": "Hasan Mahmud",
    "102": "Mahmud Hasan"
}

print(studentId["101"])  # Hasan Mahmud
print(studentId.get("101"))  # Hasan Mahmud
print(studentId.get("103"))  # None
print(studentId.get("103", "Not a valid key"))  # Not a valid key
print(studentId.get("101", "Not a valid key"))  # Hasan Mahmud


