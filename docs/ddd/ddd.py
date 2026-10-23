
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

# ==========================================
# 1. تنظیم مسیر ذخیره‌سازی خروجی در ویندوز
# ==========================================

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"

# ساخت پوشه خروجی در صورت عدم وجود
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_PATH = OUTPUT_DIR / "monolithic_ecommerce_architecture.png"


# ==========================================
# 2. تنظیمات اولیه نمودار
# ==========================================

fig, ax = plt.subplots(figsize=(14, 10))

ax.set_xlim(0, 14)
ax.set_ylim(0, 12)
ax.axis("off")

fig.patch.set_facecolor("white")
ax.set_facecolor("white")


# ==========================================
# 3. تابع رسم کادرهای نمودار
# ==========================================

def draw_box(x, y, width, height, title, details,
             facecolor="#EAF2F8", edgecolor="#2874A6",
             title_size=11, detail_size=9):

    box = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle="round,pad=0.08",
        linewidth=1.5,
        edgecolor=edgecolor,
        facecolor=facecolor
    )

    ax.add_patch(box)

    ax.text(
        x + width / 2,
        y + height - 0.28,
        title,
        ha="center",
        va="center",
        fontsize=title_size,
        fontweight="bold",
        color="#17202A"
    )

    ax.text(
        x + width / 2,
        y + height / 2 - 0.12,
        details,
        ha="center",
        va="center",
        fontsize=detail_size,
        color="#273746",
        linespacing=1.5
    )


# ==========================================
# 4. عنوان نمودار
# ==========================================

ax.text(
    7,
    11.55,
    "Monolithic E-Commerce Architecture",
    ha="center",
    va="center",
    fontsize=17,
    fontweight="bold",
    color="#154360"
)

ax.text(
    7,
    11.15,
    "Single Application - Shared Database",
    ha="center",
    va="center",
    fontsize=11,
    color="#566573"
)


# ==========================================
# 5. کاربران و رابط کاربری
# ==========================================

draw_box(
    4.5, 9.6, 5, 0.9,
    "Users / Customers",
    "Browse products | Register | Login | Purchase",
    facecolor="#FCF3CF",
    edgecolor="#B7950B"
)

draw_box(
    4.5, 8.1, 5, 0.9,
    "Presentation Layer",
    "HTML | CSS | JavaScript | Web UI",
    facecolor="#D6EAF8",
    edgecolor="#2874A6"
)


# ==========================================
# 6. لایه اصلی برنامه مونولوتیک
# ==========================================

main_box = FancyBboxPatch(
    (1.0, 3.0),
    12.0,
    4.3,
    boxstyle="round,pad=0.12",
    linewidth=2.5,
    edgecolor="#1E8449",
    facecolor="#EAFAF1"
)

ax.add_patch(main_box)

ax.text(
    7,
    6.95,
    "Monolithic Application",
    ha="center",
    va="center",
    fontsize=15,
    fontweight="bold",
    color="#196F3D"
)


# ==========================================
# 7. زیرسیستم‌های دامنه فروشگاه
# ==========================================

draw_box(
    1.5, 5.0, 2.4, 1.35,
    "User Management",
    "Registration\nAuthentication\nCustomer Profile",
    facecolor="#FDEDEC",
    edgecolor="#C0392B",
    title_size=10,
    detail_size=8
)

draw_box(
    4.3, 5.0, 2.4, 1.35,
    "Product Catalog",
    "Products\nCategories\nInventory",
    facecolor="#EBDEF0",
    edgecolor="#7D3C98",
    title_size=10,
    detail_size=8
)

draw_box(
    7.1, 5.0, 2.4, 1.35,
    "Order Management",
    "Shopping Cart\nOrders\nOrder Status",
    facecolor="#D5F5E3",
    edgecolor="#239B56",
    title_size=10,
    detail_size=8
)

draw_box(
    9.9, 5.0, 2.4, 1.35,
    "Payment",
    "Payment Requests\nTransactions\nPayment Status",
    facecolor="#D6EAF8",
    edgecolor="#2471A3",
    title_size=10,
    detail_size=8
)


# ==========================================
# 8. زیرسیستم‌های تکمیلی
# ==========================================

draw_box(
    3.0, 3.45, 3.3, 0.9,
    "Shipping & Delivery",
    "Address | Shipment | Tracking",
    facecolor="#FCF3CF",
    edgecolor="#B7950B",
    title_size=10,
    detail_size=8
)

draw_box(
    7.0, 3.45, 3.3, 0.9,
    "Notification & Reporting",
    "Email | Reports | Sales Statistics",
    facecolor="#F5EEF8",
    edgecolor="#884EA0",
    title_size=10,
    detail_size=8
)


# ==========================================
# 9. پایگاه داده مشترک
# ==========================================

draw_box(
    3.0, 0.9, 8.0, 1.2,
    "Shared Database",
    "Users | Products | Inventory | Orders | Payments | Shipments",
    facecolor="#D4E6F1",
    edgecolor="#1F618D",
    title_size=13,
    detail_size=9
)


# ==========================================
# 10. تابع رسم پیکان‌ها
# ==========================================

def draw_arrow(start, end, color="#566573"):
    ax.annotate(
        "",
        xy=end,
        xytext=start,
        arrowprops=dict(
            arrowstyle="->",
            linewidth=1.5,
            color=color,
            shrinkA=3,
            shrinkB=3
        )
    )


# کاربران به رابط کاربری
draw_arrow((7, 9.6), (7, 9.0))

# رابط کاربری به برنامه
draw_arrow((7, 8.1), (7, 7.3))

# زیرسیستم‌ها به پایگاه داده مشترک
draw_arrow((2.7, 5.0), (4.2, 2.1))
draw_arrow((5.5, 5.0), (5.5, 2.1))
draw_arrow((8.3, 5.0), (8.3, 2.1))
draw_arrow((11.1, 5.0), (9.8, 2.1))

# زیرسیستم‌های تکمیلی به پایگاه داده
draw_arrow((4.65, 3.45), (5.0, 2.1))
draw_arrow((8.65, 3.45), (8.8, 2.1))


# ==========================================
# 11. توضیح ویژگی معماری
# ==========================================

ax.text(
    7,
    0.35,
    "All modules run within one application and are deployed together.",
    ha="center",
    va="center",
    fontsize=9,
    style="italic",
    color="#566573"
)


# ==========================================
# 12. ذخیره نمودار در فایل PNG
# ==========================================

try:
    fig.savefig(
        OUTPUT_PATH,
        dpi=180,
        bbox_inches="tight",
        facecolor="white"
    )

    print("=" * 55)
    print("Architecture diagram created successfully.")
    print(f"Output file: {OUTPUT_PATH}")
    print("=" * 55)

except OSError as error:
    print(f"Error saving the image: {error}")

finally:
    plt.close(fig)
