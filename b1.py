# 1. Lỗi ZeroDivisionError xảy ra vì ShowMaker có Deaths = 0, phép chia cho 0 không hợp lệ.
# 2. Nếu xóa ShowMaker, Chovy gây lỗi ValueError do "ba" không thể ép kiểu sang số.
# 3. Nên đổi tên: ds → player_stats_list, x → player_stats, n → name, k → kills, d → deaths, a → assists.
# 4. Tách hàm calculate_kda() giúp tái sử dụng, dễ bảo trì và tránh lặp lại code (theo nguyên tắc DRY).

# Dữ liệu thống kê: (Tên tuyển thủ, Kills, Deaths, Assists)
player_stats_list = [
    ("Faker", "10", "2", "8"),      # Tuyển thủ 1: Dữ liệu bình thường
    ("ShowMaker", "15", "0", "10"), # Tuyển thủ 2: Không chết mạng nào (Deaths = 0)
    ("Chovy", "12", "ba", "5")      # Tuyển thủ 3: Lỗi API trả về chữ 'ba' thay vì số 3
]

def calculate_kda(kills, deaths, assists):
    """Tính toán chỉ số KDA theo công thức chuẩn."""
    return (kills + assists) / deaths

def process_player_stats(player_stats_list):
    print("--- BẢNG XẾP HẠNG KDA ---")
    for player_stats in player_stats_list:
        name = player_stats[0]
        kills_str = player_stats[1]
        deaths_str = player_stats[2]
        assists_str = player_stats[3]
        try:
            kills = int(kills_str)
            deaths = int(deaths_str)
            assists = int(assists_str)
            kda = calculate_kda(kills, deaths, assists)
            print(f"Tuyển thủ {name} có chỉ số KDA là: {kda}")
        except ZeroDivisionError:
            print(f"Tuyển thủ {name}: KDA Hoàn hảo (Perfect Game)!")
            continue  
        except ValueError:
            print(f"Tuyển thủ {name}: Lỗi dữ liệu không hợp lệ!")
            continue  
# Chạy hệ thống
process_player_stats(player_stats_list)
