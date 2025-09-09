import logging
import sqlite3
import requests
from datetime import datetime
from telegram import (
    Update, ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton
)
from telegram.ext import (
    Application, CommandHandler, MessageHandler,
    CallbackQueryHandler, ContextTypes, filters
)

# ================= CONFIG =================
BOT_TOKEN = "8481211232:AAHhnrG_xOcjlwJa_RH53EAp2a_ePF303sg"
ADMIN_ID = "7810784093"  # apni Telegram user ID yahan daalni hai
API_URL = "https://amaranthmagpie.onpella.app/api/number/lookup"
API_KEY = "1monthcyber"
FORCE_CHANNELS = ["@swapipy", "@adipython", "@brontzpy", "@ILLUMINATIHUBS", "@roxug","@team_senpieee","@pradumpyt","@permaera"]  
REQUIRED_CREDITS = 1
# ==========================================

# ================ LOGGING =================
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ================ DATABASE =================
conn = sqlite3.connect("bot.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    uid TEXT PRIMARY KEY,
    credits INTEGER DEFAULT 1,
    banned INTEGER DEFAULT 0,
    last_daily TEXT,
    referred_by TEXT
)
""")
cur.execute("""
CREATE TABLE IF NOT EXISTS redeems (
    code TEXT PRIMARY KEY,
    credits INTEGER,
    max_uses INTEGER,
    used_count INTEGER DEFAULT 0
)
""")
conn.commit()

# ================= UTILS =================
def get_user(uid):
    cur.execute("SELECT * FROM users WHERE uid=?", (str(uid),))
    row = cur.fetchone()
    if not row:
        cur.execute("INSERT INTO users (uid) VALUES (?)", (str(uid),))
        conn.commit()
        return get_user(uid)
    return {
        "uid": row[0],
        "credits": row[1],
        "banned": bool(row[2]),
        "last_daily": row[3],
        "referred_by": row[4]
    }

def save_user(user):
    cur.execute("""
    UPDATE users SET credits=?, banned=?, last_daily=?, referred_by=? WHERE uid=?
    """, (
        user["credits"], int(user["banned"]),
        user["last_daily"], user["referred_by"], user["uid"]
    ))
    conn.commit()

def is_admin(uid):
    return str(uid) == str(ADMIN_ID)

async def check_force_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    try:
        for channel in FORCE_CHANNELS:
            member = await context.bot.get_chat_member(channel, uid)
            if member.status not in ["member", "administrator", "creator"]:
                return False
    except:
        return False
    return True

# ================= MENUS =================
def main_menu(uid):
    buttons = [
        [KeyboardButton("🔍 Search Number")],
        [KeyboardButton("💎 Daily Bonus"), KeyboardButton("👥 Referral")],
        [KeyboardButton("👤 My Account"), KeyboardButton("💳 Redeem Code")],
        [KeyboardButton("❓ Help"), KeyboardButton("📞 Contact Admin")]
    ]
    if is_admin(uid):
        buttons.append([KeyboardButton("📢 Broadcast"), KeyboardButton("🛠 Create Redeem")])
        buttons.append([KeyboardButton("📊 Bot Stats")])
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)

# ================= HANDLERS =================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    user = get_user(uid)
    if user["banned"]:
        return await update.message.reply_text("🚫 You are banned.")

    if not await check_force_join(update, context):
        buttons = []
        for ch in FORCE_CHANNELS:
            if ch.startswith("@"):
                url = f"https://t.me/{ch[1:]}"
            else:
                url = f"https://t.me/{ch}"
            buttons.append([InlineKeyboardButton("🔗 Join", url=url)])  # only "Join"
        buttons.append([InlineKeyboardButton("✅ I Joined", callback_data="joined")])
        return await update.message.reply_text(
            "🔔 Please join all required channels first:",
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    await update.message.reply_text(
        f"👋 Hello {update.effective_user.first_name}!",
        reply_markup=main_menu(uid)
    )

async def check_joined_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    uid = query.from_user.id

    if not await check_force_join(update, context):
        await query.edit_message_text("❌ You still need to join all required channels.")
        return

    await query.edit_message_text("✅ Thank you for joining! You can now use the bot.")
    await context.bot.send_message(
        chat_id=uid,
        text="🔹 Main Menu:",
        reply_markup=main_menu(uid)
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "ℹ️ <b>Help Menu</b>\n\n"
        "🔹 Daily Bonus: +1 credit\n"
        "🔹 Referral: +2 credits per referral\n"
        "🔹 Each search costs 1 credit\n"
    )
    await update.message.reply_text(text, parse_mode="HTML")

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    user = get_user(uid)
    text = update.message.text

    if text == "👤 My Account":
        msg = (
            f"👤 <b>Your Account</b>\n"
            f"💎 Credits: <b>{user['credits']}</b>\n"
            f"🚫 Banned: <b>{user['banned']}</b>\n"
            f"👥 Referred By: <b>{user['referred_by'] or '-'}</b>"
        )
        return await update.message.reply_text(msg, parse_mode="HTML")

    elif text == "💎 Daily Bonus":
        today = datetime.now().strftime("%Y-%m-%d")
        if user["last_daily"] == today:
            return await update.message.reply_text("⚠️ Already claimed today.")
        user["credits"] += 1
        user["last_daily"] = today
        save_user(user)
        return await update.message.reply_text("🎉 Daily bonus claimed! +1 credit.")

    elif text == "👥 Referral":
        link = f"https://t.me/SwapiInfoBot?start={uid}"
        return await update.message.reply_text(f"👥 Your referral link:\n{link}\nYou earn 2 credits per referral!")

    elif text == "💳 Redeem Code":
        context.user_data["waiting_for_code"] = True
        return await update.message.reply_text("🔑 Enter redeem code:")

    elif text == "🔍 Search Number":
        context.user_data["waiting_for_number"] = True
        return await update.message.reply_text("📞 Send number to search:")

    elif text == "❓ Help":
        return await help_command(update, context)

    elif text == "📞 Contact Admin":
        return await update.message.reply_text("📩 Contact: @Swapibhai")

    # ================== ADMIN ==================
    elif text == "📢 Broadcast" and is_admin(uid):
        context.user_data["waiting_broadcast"] = True
        return await update.message.reply_text("📝 Send message to broadcast:")

    elif text == "🛠 Create Redeem" and is_admin(uid):
        context.user_data["waiting_redeem"] = True
        return await update.message.reply_text("🔑 Send code,credits,max_uses (e.g. TEST,5,10)")

    elif text == "📊 Bot Stats" and is_admin(uid):
        cur.execute("SELECT COUNT(*) FROM users")
        total = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM users WHERE banned=1")
        banned = cur.fetchone()[0]
        cur.execute("SELECT SUM(credits) FROM users")
        total_credits = cur.fetchone()[0] or 0
        msg = (
            f"📊 <b>Bot Stats</b>\n"
            f"👥 Total Users: <b>{total}</b>\n"
            f"🚫 Banned: <b>{banned}</b>\n"
            f"💰 Total Credits in System: <b>{total_credits}</b>"
        )
        return await update.message.reply_text(msg, parse_mode="HTML")

    # =============== INPUT HANDLERS ===============
    elif context.user_data.get("waiting_for_code"):
        context.user_data["waiting_for_code"] = False
        code = text.strip().upper()
        cur.execute("SELECT * FROM redeems WHERE code=?", (code,))
        row = cur.fetchone()
        if not row:
            return await update.message.reply_text("❌ Invalid code.")
        if row[3] >= row[2]:
            return await update.message.reply_text("⚠️ Code already fully used.")
        cur.execute("UPDATE redeems SET used_count=used_count+1 WHERE code=?", (code,))
        cur.execute("UPDATE users SET credits=credits+? WHERE uid=?", (row[1], uid))
        conn.commit()
        return await update.message.reply_text(f"🎉 Success! Added {row[1]} credits.")

    elif context.user_data.get("waiting_for_number"):
        context.user_data["waiting_for_number"] = False
        number = text.strip()
        if user["credits"] < REQUIRED_CREDITS:
            return await update.message.reply_text(f"❌ Not enough credits. Remaining: {user['credits']}")
        msg = await update.message.reply_text("⏳ Searching...")
        try:
            url = f"{API_URL}?number={number}&key={API_KEY}"
            resp = requests.get(url, timeout=15).json()

            if not resp or "data" not in resp or "data" not in resp["data"]:
                return await msg.edit_text("❌ No data found.")

            results = resp["data"]["data"]
            user["credits"] -= REQUIRED_CREDITS
            save_user(user)

            for idx, d in enumerate(results, 1):
                result_text = (
                    f"💠 ━━━ Result {idx} ━━━ 💠\n"
                    f"📱 Mobile: <b>{d.get('mobile','-')}</b>\n"
                    f"👤 Name: <b>{d.get('name','-')}</b>\n"
                    f"👨 Father: <b>{d.get('fname','-')}</b>\n"
                    f"🏠 Address: <b>{d.get('address','-')}</b>\n"
                    f"📞 Alt: <b>{d.get('alt','-')}</b>\n"
                    f"🌐 Circle: <b>{d.get('circle','-')}</b>\n"
                    f"🆔 ID: <b>{d.get('id','-')}</b>\n"
                    f"━━━━━━━━━━━━━━━━━━━━━"
                )
                await update.message.reply_text(result_text, parse_mode="HTML")

            await msg.edit_text(f"✅ Search complete. Remaining credits: {user['credits']}")
        except Exception as e:
            await msg.edit_text(f"⚠️ Error: {e}")

    elif context.user_data.get("waiting_broadcast") and is_admin(uid):
        context.user_data["waiting_broadcast"] = False
        cur.execute("SELECT uid FROM users")
        all_users = cur.fetchall()
        count = 0
        for u in all_users:
            try:
                await context.bot.send_message(u[0], text)
                count += 1
            except:
                continue
        return await update.message.reply_text(f"✅ Broadcast sent to {count} users.")

    elif context.user_data.get("waiting_redeem") and is_admin(uid):
        context.user_data["waiting_redeem"] = False
        try:
            code, credits, max_uses = text.split(",")
            cur.execute(
                "INSERT INTO redeems (code, credits, max_uses) VALUES (?,?,?)",
                (code.upper(), int(credits), int(max_uses))
            )
            conn.commit()
            return await update.message.reply_text(
                f"✅ Redeem code created: {code.upper()} ({credits} credits, {max_uses} uses)"
            )
        except Exception as e:
            return await update.message.reply_text(f"⚠️ Error: {e}")

# ================= MAIN =================
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
    app.add_handler(CallbackQueryHandler(check_joined_button, pattern="^joined$"))
    app.run_polling()

if __name__ == "__main__":
    main()
