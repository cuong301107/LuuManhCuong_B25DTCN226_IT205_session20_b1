# 1. Lỗi IndexError: tuple index out of range xảy ra vì bản ghi của SofM chỉ có 2 phần tử, nên p[2] không tồn tại.
# 2. Khi sửa SofM, đến Optimus sẽ lỗi ValueError do "N/A" không thể ép kiểu sang số bằng int().
# 3. Lệnh print("Đang xử lý:", p) giúp xác định bản ghi nào gây lỗi trước khi chương trình sập.
# 4. Nên đổi tên: ds → player_records, p → record, t → name, m → matches, r → mmr, b → bonus.
# Dữ liệu từ API: (Tên, Số trận, MMR)

player_records = [
    ("Levi", 120, 2500),
    ("SofM", 150),           
    ("Optimus", 100, "N/A")
]

def calculate_bonus(matches, mmr):
    """Hàm tính tiền thưởng RP."""
    return (matches * 10) + (mmr * 0.5)

def process_bonus(player_records):
    print("--- BẢNG TÍNH THƯỞNG RP ---")
    
    for record in player_records:
        try:
            name = record[0]
            matches = record[1]
            mmr = record[2]  # Có thể gây IndexError

            bonus = calculate_bonus(matches, int(mmr))  # int(mmr) có thể gây ValueError
            print(f"Tuyển thủ {name} nhận được {bonus} RP")

        except IndexError:
            print(f"{record[0]}: Lỗi - Hồ sơ bị thiếu thông tin!")
            continue

        except ValueError:
            print(f"{record[0]}: Lỗi - Dữ liệu MMR không hợp lệ!")
            continue

process_bonus(player_records)
