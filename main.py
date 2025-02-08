import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  
intents.presences = True 
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ {bot.user} ist erfolgreich gestartet!")
    await bot.change_presence(activity=discord.Game(name="Admin System aktiv!"))

# 📌 USERINFO BEFEHL
@bot.command(name="userinfo")
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author  # Falls kein Mitglied angegeben, nutze den Befehlsersteller

    embed = discord.Embed(
        title=f"👤 Informationen über {member.display_name}",
        color=member.color,
        timestamp=ctx.message.created_at
    )

    # Avatar setzen (Kompatibilität mit älteren Versionen)
    embed.set_thumbnail(url=member.avatar_url)

    # 🔝 Wichtige Infos
    embed.add_field(name="🆔 Benutzer ID", value=member.id, inline=True)
    embed.add_field(name="📅 Konto erstellt am", value=member.created_at.strftime("%d.%m.%Y %H:%M:%S"), inline=True)
    embed.add_field(name="📌 Server beigetreten am", value=member.joined_at.strftime("%d.%m.%Y %H:%M:%S"), inline=True)

    # 🔒 Administratorrechte
    embed.add_field(name="🔒 Administrator", value="✅ Ja" if member.guild_permissions.administrator else "❌ Nein", inline=True)

    # 💬 Status & Aktivität
    status_emoji = {
        "online": "🟢 Online",
        "offline": "⚫ Offline",
        "idle": "🌙 Abwesend",
        "dnd": "⛔ Bitte nicht stören"
    }
    user_status = status_emoji.get(str(member.status), "❓ Unbekannt")
    activity = member.activity.name if member.activity else "Keine Aktivität"

    embed.add_field(name="💬 Status", value=user_status, inline=True)
    embed.add_field(name="🎮 Aktivität", value=activity, inline=True)

    # 📜 Rollen anzeigen (wichtige zuerst)
    special_roles = ["Admin", "Moderator", "Support", "VIP"]
    roles_list = sorted(
        [role for role in member.guild.roles if role.name != "@everyone"],
        key=lambda r: (r.name not in special_roles, r.position),
        reverse=True
    )

    roles_text = "\n".join([f"{role.name} {'✅' if role in member.roles else '❌'}" for role in roles_list])
    embed.add_field(name="📜 Rollen", value=roles_text if roles_list else "Keine Rollen", inline=False)

    # ℹ️ Footer mit Anforderer
    embed.set_footer(text=f"Angefordert von {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

# 🛠️ KICK-BEFEHL
@bot.command(name="kick")
@commands.has_permissions(kick_members=True)  # Erfordert Kick-Berechtigung
async def kick(ctx, member: discord.Member, *, reason="Kein Grund angegeben"):
    if ctx.author.top_role <= member.top_role:
        return await ctx.send("❌ Du kannst diesen Benutzer nicht kicken (Rang zu hoch).")

    await member.kick(reason=reason)
    embed = discord.Embed(
        title="👢 Benutzer gekickt",
        description=f"**{member}** wurde von **{ctx.author}** gekickt.\n\n**Grund:** {reason}",
        color=discord.Color.orange()
    )
    await ctx.send(embed=embed)

# ⛔ BAN-BEFEHL
@bot.command(name="ban")
@commands.has_permissions(ban_members=True)  # Erfordert Ban-Berechtigung
async def ban(ctx, member: discord.Member, *, reason="Kein Grund angegeben"):
    if ctx.author.top_role <= member.top_role:
        return await ctx.send("❌ Du kannst diesen Benutzer nicht bannen (Rang zu hoch).")

    await member.ban(reason=reason)
    embed = discord.Embed(
        title="⛔ Benutzer gebannt",
        description=f"**{member}** wurde von **{ctx.author}** gebannt.\n\n**Grund:** {reason}",
        color=discord.Color.red()
    )
    await ctx.send(embed=embed)

# Fehlermeldung, falls kein Admin ist
@kick.error
@ban.error
async def error_handler(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ Du hast nicht die benötigten Berechtigungen für diesen Befehl.")

# Bot starten
bot.run("YOUR_BOT_TOKEN")
