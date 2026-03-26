from storage import read_data, write_data

MEMBER_FILE = "data/members.csv"

def add_member(member_id, name, age, contact):
    df = read_data(MEMBER_FILE)

    new = {
        "member_id": member_id,
        "name": name,
        "age": age,
        "contact": contact
    }

    df = df._append(new, ignore_index=True)
    write_data(MEMBER_FILE, df)

    return "Member added successfully"