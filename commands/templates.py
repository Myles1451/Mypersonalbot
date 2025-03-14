import discord
from discord.ext import commands

import datetime, time

import config_selfbot
from utils import rpc, lang, log


class TemplatesCommands(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.templates_assets = rpc.get_raw_json("Sitois", "Nuclear-V2", "assets.json")
        self.today_date = datetime.datetime.today()

    @commands.command()
    async def use(self, ctx: commands.Context):
        choice = ctx.message.content.split()[1].lower()
        if choice == "hi":
            assets = {"large_image": self.templates_assets["hi"]["large_image"],
                      "large_text": "heyyy",
                      "small_image": self.templates_assets["hi"]["small_image"],
                      "small_text": "hiii"
                      }
            activity = discord.Activity(type=discord.ActivityType.playing,
                                        name="Hi !",
                                        details="hi !!!!!!",
                                        state=None,
                                        timestamps={"reset": time.time()},
                                        assets=assets,
                                        application_id=1193291951290712154,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

            try:
                await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                               activity=activity,
                                               afk=True,
                                               idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
            except Exception as e:
                try:
                    await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                                   activity=activity,
                                                   edit_settings=False)
                except Exception as e:
                    log.alert(f"{lang.text('error_rpc')}\n{e}\n{lang.text('error_rpc_two')}")
                    return

            await ctx.message.edit("👋 Template \"hi !\".", delete_after=config_selfbot.deltime)
        elif choice == "omori":
            assets = {"large_image": self.templates_assets["omori"]["large_image"],
                      "large_text": "Omori",
                      "small_image": self.templates_assets["omori"]["small_image"],
                      "small_text": "The bulb."
                      }
            activity = discord.Activity(type=discord.ActivityType.playing,
                                        name="Omori",
                                        details="In Game",
                                        state="Fighting a boss.",
                                        timestamps={"reset": time.time()},
                                        assets=assets,
                                        application_id=1193291951290712154,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

            try:
                await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                               activity=activity,
                                               afk=True,
                                               idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
            except Exception as e:
                try:
                    await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                                   activity=activity,
                                                   edit_settings=False)
                except Exception as e:
                    log.alert(f"{lang.text('error_rpc')}\n{e}\n{lang.text('error_rpc_two')}")
                    return

            await ctx.message.edit("💡 Template \"Omori\".", delete_after=config_selfbot.deltime)
        elif choice == "cod":
            assets = {"large_image": self.templates_assets["cod"]["large_image"],
                      "large_text": "Call Of Duty: MWIII",
                      "small_image": self.templates_assets["cod"]["small_image"],
                      "small_text": "Battle Pass level 21"
                      }
            activity = discord.Activity(type=discord.ActivityType.playing,
                                        name="Call Of Duty: MWIII",
                                        details=lang.text('rpc_cod_details'),
                                        state=lang.text('rpc_cod_state'),
                                        timestamps={"reset": time.time()},
                                        assets=assets,
                                        application_id=1193291951290712154,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
            try:
                await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                               activity=activity,
                                               afk=True,
                                               idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
            except Exception as e:
                try:
                    await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                                   activity=activity,
                                                   edit_settings=False)
                except Exception as e:
                    log.alert(f"{lang.text('error_rpc')}\n{e}\n{lang.text('error_rpc_two')}")
                    return

            await ctx.message.edit("🔫 Template \"Call Of Duty\".", delete_after=config_selfbot.deltime)
        elif choice == "youtube":
            assets = {"large_image": self.templates_assets["youtube"]["large_image"],
                      "large_text": "YouTube",
                      "small_image": self.templates_assets["youtube"]["small_image"],
                      "small_text": None
                      }
            activity = discord.Activity(type=discord.ActivityType.watching,
                                        name="YouTube",
                                        details="Watching Videos",
                                        state=None,
                                        timestamps={"reset": time.time()},
                                        assets=assets,
                                        application_id=1193291951290712154,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

            try:
                await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                               activity=activity,
                                               afk=True,
                                               idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
            except Exception as e:
                try:
                    await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                                   activity=activity,
                                                   edit_settings=False)
                except Exception as e:
                    log.alert(f"{lang.text('error_rpc')}\n{e}\n{lang.text('error_rpc_two')}")
                    return

            await ctx.message.edit("🎦 Template \"YouTube\".", delete_after=config_selfbot.deltime)
        elif choice == "car":
            assets = {"large_image": self.templates_assets["car"]["large_image"],
                      "large_text": "Drift Car",
                      "small_image": self.templates_assets["car"]["small_image"],
                      "small_text": None
                      }
            activity = discord.Activity(type=discord.ActivityType.watching,
                                        name="Drift Car",
                                        details="Watching DriftCar",
                                        state=None,
                                        timestamps={"reset": time.time()},
                                        assets=assets,
                                        application_id=1193291951290712154,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
            
            try:
                await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                               activity=activity,
                                               afk=True,
                                               idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
            except Exception as e:
                try:
                    await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                                   activity=activity,
                                                   edit_settings=False)
                except Exception as e:
                    log.alert(f"{lang.text('error_rpc')}\n{e}\n{lang.text('error_rpc_two')}")
                    return

            await ctx.message.edit("🏎️ Template \"Car\".", delete_after=config_selfbot.deltime)
        elif choice == "js":
            assets = {"large_image": self.templates_assets["js"]["large_image"],
                      "large_text": "Editing a JAVASCRIPT file",
                      "small_image": self.templates_assets["js"]["small_image"],
                      "small_text": "Visual Studio Code"
                      }
            activity = discord.Activity(type=discord.ActivityType.playing,
                                        name="Visual Studio Code",
                                        details=f"🛠️ Editing Java script file (2743 lines)",
                                        state="📂 Workspace: ¿ Myles14511",
                                        timestamps={"reset": time.time()},
                                        assets=assets,
                                        application_id=1193291951290712154,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

            try:
                await self.bot.change_presence(status=discord.Status.idle,
                                               activity=activity,
                                               afk=True,
                                               idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
            except Exception as e:
                try:
                    await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                                   activity=activity,
                                                   edit_settings=False)
                except Exception as e:
                    log.alert(f"{lang.text('error_rpc')}\n{e}\n{lang.text('error_rpc_two')}")
                    return

            await ctx.message.edit("👨‍💻 Template \"JavaScript\".", delete_after=config_selfbot.deltime)
        elif choice == "python":
            assets = {"large_image": self.templates_assets["python"]["large_image"],
                      "large_text": "Editing a PYTHON file",
                      "small_image": self.templates_assets["python"]["small_image"],
                      "small_text": "Visual Studio Code"
                      }
            activity = discord.Activity(type=discord.ActivityType.playing,
                                        name="Visual Studio Code",
                                        details=f"🛠️ Editing 1875",
                                        state="📂 Workspace: ¿ Myles14511",
                                        timestamps={"reset": time.time()},
                                        assets=assets,
                                        application_id=1193291951290712154,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

            try:
                await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                               activity=activity,
                                               afk=True,
                                               idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
            except Exception as e:
                try:
                    await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                                   activity=activity,
                                                   edit_settings=False)
                except Exception as e:
                    log.alert(f"{lang.text('error_rpc')}\n{e}\n{lang.text('error_rpc_two')}")
                    return

            await ctx.message.edit("👨‍💻 Template \"Python\".", delete_after=config_selfbot.deltime)
        elif choice == "webdeck":
            assets = {"large_image": self.templates_assets["webdeck"]["large_image"],
                      "large_text": "WebDeck Icon",
                      "small_image": self.templates_assets["webdeck"]["small_image"],
                      "small_text": "Lenochxd"
                      }
            activity = discord.Activity(type=discord.ActivityType.playing,
                                        name="WebDeck",
                                        details="github.com/Lenochxd/WebDeck",
                                        state="Using a with Free StreamDeck!",
                                        timestamps={"reset": time.time()},
                                        assets=assets,
                                        application_id=1193291951290712154,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

            try:
                await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                               activity=activity,
                                               afk=True,
                                               idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
            except Exception as e:
                try:
                    await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                                   activity=activity,
                                                   edit_settings=False)
                except Exception as e:
                    log.alert(f"{lang.text('error_rpc')}\n{e}\n{lang.text('error_rpc_two')}")
                    return

            await ctx.message.edit("📱 Template \"WebDeck\".", delete_after=config_selfbot.deltime)
        elif choice == "nuclear":
            assets = {"large_image": self.templates_assets["nuclear"]["large_image"],
                      "large_text": "github.com/Sitois/Nuclear-V2",
                      "small_image": self.templates_assets["nuclear"]["small_image"],
                      "small_text": "On GitHub!"
                      }
            activity = discord.Activity(type=discord.ActivityType.streaming,
                                        name="Nuclear",
                                        details="Nuclear $B",
                                        state="Best free open-source $B!",
                                        assets=assets,
                                        url=config_selfbot.streaming_url,
                                        application_id=1193291951290712154,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

            try:
                await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                               activity=activity,
                                               afk=True,
                                               idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
            except Exception as e:
                try:
                    await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                                   activity=activity,
                                                   edit_settings=False)
                except Exception as e:
                    log.alert(f"{lang.text('error_rpc')}\n{e}\n{lang.text('error_rpc_two')}")
                    return

            await ctx.message.edit("🌌 Template \"Nuclear\".", delete_after=config_selfbot.deltime)
        elif choice == "dark":
            assets = {"large_image": self.templates_assets["dark"]["large_image"],
                      "large_text": "☄",
                      "small_image": self.templates_assets["dark"]["small_image"],
                      "small_text": None
                      }
            activity = discord.Activity(type=discord.ActivityType.competing,
                                        name="☄",
                                        details=None,
                                        state=None,
                                        assets=assets,
                                        application_id=1193291951290712154,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

            try:
                await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                               activity=activity,
                                               afk=True,
                                               idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
            except Exception as e:
                try:
                    await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                                   activity=activity,
                                                   edit_settings=False)
                except Exception as e:
                    log.alert(f"{lang.text('error_rpc')}\n{e}\n{lang.text('error_rpc_two')}")
                    return

            await ctx.message.edit("🖤 Template \"Dark\".", delete_after=config_selfbot.deltime)
        elif choice == "gta":
            assets = {"large_image": self.templates_assets["gta"]["large_image"],
                      "large_text": "Grand Theft Auto VI",
                      "small_image": self.templates_assets["gta"]["small_image"],
                      "small_text": None
                      }
            activity = discord.Activity(type=discord.ActivityType.playing,
                                        name="GTA V",
                                        details="Welcome to Los Santos",
                                        state="Playing Story",
                                        timestamps={"reset": time.time()},
                                        assets=assets,
                                        application_id=1193291951290712154,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

            try:
                await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                               activity=activity,
                                               afk=True,
                                               idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
            except Exception as e:
                try:
                    await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                                   activity=activity,
                                                   edit_settings=False)
                except Exception as e:
                    log.alert(f"{lang.text('error_rpc')}\n{e}\n{lang.text('error_rpc_two')}")
                    return

            await ctx.message.edit("🔫 Template \"Grand Theft Auto V\".", delete_after=config_selfbot.deltime)
        elif choice == "tiktok":
            assets = {"large_image": self.templates_assets["tiktok"]["large_image"],
                      "large_text": "TikTok",
                      "small_image": self.templates_assets["tiktok"]["small_image"],
                      "small_text": None
                      }
            activity = discord.Activity(type=discord.ActivityType.watching,
                                        name="TikTok",
                                        details="ForYou page",
                                        state=None,
                                        timestamps={"reset": time.time()},
                                        assets=assets,
                                        application_id=1193291951290712154,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

            try:
                await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                               activity=activity,
                                               afk=True,
                                               idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
            except Exception as e:
                try:
                    await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                                   activity=activity,
                                                   edit_settings=False)
                except Exception as e:
                    log.alert(f"{lang.text('error_rpc')}\n{e}\n{lang.text('error_rpc_two')}")
                    return

            await ctx.message.edit("📱 Template \"TikTok\".", delete_after=config_selfbot.deltime)
        elif choice == "reset":
            assets = {"large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
                      "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
                      "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
                      "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
                     }
            activity = discord.Activity(type=discord.ActivityType.playing,
                                        name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                        details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                        state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                        timestamps={"reset": time.time()},
                                        assets=assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"), config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])

            try:
                await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                               activity=activity,
                                               afk=True,
                                               idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
            except Exception as e:
                try:
                    await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                                   activity=activity,
                                                   edit_settings=False)
                except Exception as e:
                    log.alert(f"{lang.text('error_rpc')}\n{e}\n{lang.text('error_rpc_two')}")
                    return

            await ctx.message.edit("🔄️ RPC Reset.", delete_after=config_selfbot.deltime)
        elif choice == "default":
            activity = discord.Activity(type=discord.ActivityType.playing,
                                        name=config_selfbot.activity_name,
                                        details=config_selfbot.activity_details,
                                        state=config_selfbot.activity_state,
                                        timestamps={"reset": time.time()},
                                        assets=config_selfbot.assets,
                                        application_id=config_selfbot.application_id,
                                        buttons=[config_selfbot.activity_button_one, config_selfbot.activity_button_two])

            try:
                await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                               activity=activity,
                                               afk=True,
                                               idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
            except Exception as e:
                try:
                    await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                                   activity=activity,
                                                   edit_settings=False)
                except Exception as e:
                    log.alert(f"{lang.text('error_rpc')}\n{e}\n{lang.text('error_rpc_two')}")
                    return

            await ctx.message.edit("🔄️ RPC \"Default\".", delete_after=config_selfbot.deltime)
        elif choice == "clear":
            try:
                await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                               activity=None,
                                               afk=True,
                                               idle_since=datetime.datetime(self.today_date.year, self.today_date.month, self.today_date.day))
            except Exception as e:
                try:
                    await self.bot.change_presence(status=discord.Status.do_not_disturb,
                                                   activity=None,
                                                   edit_settings=False)
                except Exception as e:
                    log.alert(f"{lang.text('error_rpc')}\n{e}\n{lang.text('error_rpc_two')}")
                    return

            await ctx.message.edit("🚮 RPC \"Clear\".", delete_after=config_selfbot.deltime)
        else:
            await ctx.message.edit(f"❌ {lang.text('incorrect')}", delete_after=config_selfbot.deltime)

    @commands.command()
    async def reload(self, ctx: commands.Context):
        self.templates_assets = rpc.get_raw_json("Sitois", "Nuclear-V2", "assets.json")
        await ctx.message.edit(lang.text('template_reload'), delete_after=config_selfbot.deltime)
