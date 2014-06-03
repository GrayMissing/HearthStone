from cards import *
actionsdict = {
    'Abomination':Abomination,
    'Abusive Sergeant':Abusive_Sergeant,
    'Acidic Swamp Ooze':Acidic_Swamp_Ooze,
    'Acolyte of Pain':Acolyte_of_Pain,
    "Al'Akir the Windlord":AlAkir the Windlord,
    'Alarm-o-Bot':Alarm-o-Bot,
    'Aldor Peacekeeper':Aldor Peacekeeper,
    'Alexstrasza':Alexstrasza,
    'Amani Berserker':Amani Berserker,
    'Ancestral Healing':Ancestral Healing,
    'Ancestral Spirit':Ancestral Spirit,
    'Ancient Brewmaster':Ancient Brewmaster,
    'Ancient Mage':Ancient Mage,
    'Ancient of Lore':Ancient of Lore,
    'Ancient of War':Ancient of War,
    'Ancient Watcher':Ancient Watcher,
    'Angry Chicken':Angry Chicken,
    'Animal Companion':Animal Companion,
    'Arathi Weaponsmith':Arathi Weaponsmith,
    'Arcane Explosion':Arcane Explosion,
    'Arcane Golem':Arcane Golem,
    'Arcane Intellect':Arcane Intellect,
    'Arcane Missiles':Arcane Missiles,
    'Arcane Shot':Arcane Shot,
    'Arcanite Reaper':Arcanite Reaper,
    'Archmage':Archmage,
    'Archmage Antonidas':Archmage Antonidas,
    'Argent Commander':Argent Commander,
    'Argent Protector':Argent Protector,
    'Argent Squire':Argent Squire,
    'Armorsmith':Armorsmith,
    'Assassin's Blade':Assassin's Blade,
    'Assassinate':Assassinate,
    'Auchenai Soulpriest':Auchenai Soulpriest,
    'Avenging Wrath':Avenging Wrath,
    'Azure Drake':Azure Drake,
    'Backstab':Backstab,
    'Bane of Doom':Bane of Doom,
    'Baron Geddon':Baron Geddon,
    'Battle Rage':Battle Rage,
    'Bestial Wrath':Bestial Wrath,
    'Betrayal':Betrayal,
    'Big Game Hunter':Big Game Hunter,
    'Bite':Bite,
    'Blade Flurry':Blade Flurry,
    'Blessed Champion':Blessed Champion,
    'Blessing of Kings':Blessing of Kings,
    'Blessing of Might':Blessing of Might,
    'Blessing of Wisdom':Blessing of Wisdom,
    'Blizzard':Blizzard,
    'Blood Imp':Blood Imp,
    'Blood Knight':Blood Knight,
    'Bloodfen Raptor':Bloodfen Raptor,
    'Bloodlust':Bloodlust,
    'Bloodmage Thalnos':Bloodmage Thalnos,
    'Bloodsail Corsair':Bloodsail Corsair,
    'Bloodsail Raider':Bloodsail Raider,
    'Bluegill Warrior':Bluegill Warrior,
    'Booty Bay Bodyguard':Booty Bay Bodyguard,
    'Boulderfist Ogre':Boulderfist Ogre,
    'Brawl':Brawl,
    'Cabal Shadow Priest':Cabal Shadow Priest,
    'Cairne Bloodhoof':Cairne Bloodhoof,
    'Captain Greenskin':Captain Greenskin,
    "Captain's Parrot":Captains Parrot,
    'Cenarius':Cenarius,
    'Charge':Charge,
    'Chillwind Yeti':Chillwind Yeti,
    'Circle of Healing':Circle of Healing,
    'Claw':Claw,
    'Cleave':Cleave,
    'Cold Blood':Cold Blood,
    'Coldlight Oracle':Coldlight Oracle,
    'Coldlight Seer':Coldlight Seer,
    'Commanding Shout':Commanding Shout,
    'Conceal':Conceal,
    'Cone of Cold':Cone of Cold,
    'Consecration':Consecration,
    'Core Hound':Core Hound,
    'Corruption':Corruption,
    'Counterspell':Counterspell,
    'Crazed Alchemist':Crazed Alchemist,
    'Cruel Taskmaster':Cruel Taskmaster,
    'Cult Master':Cult Master,
    'Dalaran Mage':Dalaran Mage,
    'Dark Iron Dwarf':Dark Iron Dwarf,
    'Darkscale Healer':Darkscale Healer,
    'Deadly Poison':Deadly Poison,
    'Deadly Shot':Deadly Shot,
    'Deathwing':Deathwing,
    'Defender of Argus':Defender of Argus,
    'Defias Ringleader':Defias Ringleader,
    'Demolisher':Demolisher,
    'Demonfire':Demonfire,
    'Dire Wolf Alpha':Dire Wolf Alpha,
    'Divine Favor':Divine Favor,
    'Divine Spirit':Divine Spirit,
    'Doomguard':Doomguard,
    'Doomhammer':Doomhammer,
    'Doomsayer':Doomsayer,
    'Dragonling Mechanic':Dragonling Mechanic,
    'Drain Life':Drain Life,
    'Dread Corsair':Dread Corsair,
    'Dread Infernal':Dread Infernal,
    'Druid of the Claw':Druid of the Claw,
    'Dust Devil':Dust Devil,
    'Eaglehorn Bow':Eaglehorn Bow,
    'Earth Elemental':Earth Elemental,
    'Earth Shock':Earth Shock,
    'Earthen Ring Farseer':Earthen Ring Farseer,
    'Edwin VanCleef':Edwin VanCleef,
    'Elite Tauren Chieftain':Elite Tauren Chieftain,
    'Elven Archer':Elven Archer,
    'Emperor Cobra':Emperor Cobra,
    'Equality':Equality,
    'Ethereal Arcanist':Ethereal Arcanist,
    'Eviscerate':Eviscerate,
    'Execute':Execute,
    'Explosive Shot':Explosive Shot,
    'Explosive Trap':Explosive Trap,
    'Eye for an Eye':Eye for an Eye,
    'Faceless Manipulator':Faceless Manipulator,
    'Faerie Dragon':Faerie Dragon,
    'Fan of Knives':Fan of Knives,
    'Far Sight':Far Sight,
    'Felguard':Felguard,
    'Fen Creeper':Fen Creeper,
    'Feral Spirit':Feral Spirit,
    'Fiery War Axe':Fiery War Axe,
    'Fire Elemental':Fire Elemental,
    'Fireball':Fireball,
    'Flame Imp':Flame Imp,
    'Flamestrike':Flamestrike,
    'Flametongue Totem':Flametongue Totem,
    'Flare':Flare,
    'Flesheating Ghoul':Flesheating Ghoul,
    'Force of Nature':Force of Nature,
    'Forked Lightning':Forked Lightning,
    'Freezing Trap':Freezing Trap,
    'Frost Elemental':Frost Elemental,
    'Frost Nova':Frost Nova,
    'Frost Shock':Frost Shock,
    'Frostbolt':Frostbolt,
    'Frostwolf Grunt':Frostwolf Grunt,
    'Frostwolf Warlord':Frostwolf Warlord,
    'Frothing Berserker':Frothing Berserker,
    'Gadgetzan Auctioneer':Gadgetzan Auctioneer,
    'Gelbin Mekkatorque':Gelbin Mekkatorque,
    'Gladiator's Longbow':Gladiator's Longbow,
    'Gnomish Inventor':Gnomish Inventor,
    'Goldshire Footman':Goldshire Footman,
    'Gorehowl':Gorehowl,
    'Grimscale Oracle':Grimscale Oracle,
    'Grommash Hellscream':Grommash Hellscream,
    'Gruul':Gruul,
    'Guardian of Kings':Guardian of Kings,
    'Gurubashi Berserker':Gurubashi Berserker,
    'Hammer of Wrath':Hammer of Wrath,
    'Hand of Protection':Hand of Protection,
    'Harrison Jones':Harrison Jones,
    'Harvest Golem':Harvest Golem,
    'Headcrack':Headcrack,
    'Healing Touch':Healing Touch,
    'Hellfire':Hellfire,
    'Heroic Strike':Heroic Strike,
    'Hex':Hex,
    'Hogger':Hogger,
    'Holy Fire':Holy Fire,
    'Holy Light':Holy Light,
    'Holy Nova':Holy Nova,
    'Holy Smite':Holy Smite,
    'Holy Wrath':Holy Wrath,
    'Houndmaster':Houndmaster,
    'Humility':Humility,
    'Hungry Crab':Hungry Crab,
    'Hunter's Mark':Hunter's Mark,
    'Ice Barrier':Ice Barrier,
    'Ice Block':Ice Block,
    'Ice Lance':Ice Lance,
    'Illidan Stormrage':Illidan Stormrage,
    'Imp Master':Imp Master,
    'Injured Blademaster':Injured Blademaster,
    'Inner Fire':Inner Fire,
    'Inner Rage':Inner Rage,
    'Innervate':Innervate,
    'Ironbark Protector':Ironbark Protector,
    'Ironbeak Owl':Ironbeak Owl,
    'Ironforge Rifleman':Ironforge Rifleman,
    'Ironfur Grizzly':Ironfur Grizzly,
    'Jungle Panther':Jungle Panther,
    'Keeper of the Grove':Keeper of the Grove,
    'Kidnapper':Kidnapper,
    'Kill Command':Kill Command,
    'King Krush':King Krush,
    'King Mukla':King Mukla,
    'Kirin Tor Mage':Kirin Tor Mage,
    'Knife Juggler':Knife Juggler,
    'Kobold Geomancer':Kobold Geomancer,
    'Kor'kron Elite':Kor'kron Elite,
    'Lava Burst':Lava Burst,
    'Lay on Hands':Lay on Hands,
    'Leeroy Jenkins':Leeroy Jenkins,
    'Leper Gnome':Leper Gnome,
    'Light's Justice':Light's Justice,
    'Lightning Bolt':Lightning Bolt,
    'Lightning Storm':Lightning Storm,
    'Lightspawn':Lightspawn,
    'Lightwarden':Lightwarden,
    'Lightwell':Lightwell,
    'Loot Hoarder':Loot Hoarder,
    'Lord Jaraxxus':Lord Jaraxxus,
    'Lord of the Arena':Lord of the Arena,
    'Lorewalker Cho':Lorewalker Cho,
    'Mad Bomber':Mad Bomber,
    'Magma Rager':Magma Rager,
    'Malygos':Malygos,
    'Mana Addict':Mana Addict,
    'Mana Tide Totem':Mana Tide Totem,
    'Mana Wraith':Mana Wraith,
    'Mana Wyrm':Mana Wyrm,
    'Mark of Nature':Mark of Nature,
    'Mark of the Wild':Mark of the Wild,
    'Mass Dispel':Mass Dispel,
    'Master of Disguise':Master of Disguise,
    'Master Swordsmith':Master Swordsmith,
    'Millhouse Manastorm':Millhouse Manastorm,
    'Mind Blast':Mind Blast,
    'Mind Control':Mind Control,
    'Mind Control Tech':Mind Control Tech,
    'Mind Vision':Mind Vision,
    'Mindgames':Mindgames,
    'Mirror Entity':Mirror Entity,
    'Mirror Image':Mirror Image,
    'Misdirection':Misdirection,
    'Mogu'shan Warden':Mogu'shan Warden,
    'Molten Giant':Molten Giant,
    'Moonfire':Moonfire,
    'Mortal Coil':Mortal Coil,
    'Mortal Strike':Mortal Strike,
    'Mountain Giant':Mountain Giant,
    'Multi-Shot':Multi-Shot,
    'Murloc Raider':Murloc Raider,
    'Murloc Tidecaller':Murloc Tidecaller,
    'Murloc Tidehunter':Murloc Tidehunter,
    'Murloc Warleader':Murloc Warleader,
    'Nat Pagle':Nat Pagle,
    'Naturalize':Naturalize,
    'Nightblade':Nightblade,
    'Noble Sacrifice':Noble Sacrifice,
    'Northshire Cleric':Northshire Cleric,
    'Nourish':Nourish,
    'Novice Engineer':Novice Engineer,
    'Nozdormu':Nozdormu,
    'Oasis Snapjaw':Oasis Snapjaw,
    'Ogre Magi':Ogre Magi,
    'Old Murk-Eye':Old Murk-Eye,
    'Onyxia':Onyxia,
    'Patient Assassin':Patient Assassin,
    'Perdition's Blade':Perdition's Blade,
    'Pint-Sized Summoner':Pint-Sized Summoner,
    'Pit Lord':Pit Lord,
    'Polymorph':Polymorph,
    'Power of the Wild':Power of the Wild,
    'Power Overwhelming':Power Overwhelming,
    'Power Word: Shield':Power Word: Shield,
    'Preparation':Preparation,
    'Priestess of Elune':Priestess of Elune,
    'Prophet Velen':Prophet Velen,
    'Pyroblast':Pyroblast,
    'Questing Adventurer':Questing Adventurer,
    'Raging Worgen':Raging Worgen,
    'Ragnaros the Firelord':Ragnaros the Firelord,
    'Raid Leader':Raid Leader,
    'Rampage':Rampage,
    'Ravenholdt Assassin':Ravenholdt Assassin,
    'Razorfen Hunter':Razorfen Hunter,
    'Reckless Rocketeer':Reckless Rocketeer,
    'Redemption':Redemption,
    'Repentance':Repentance,
    'River Crocolisk':River Crocolisk,
    'Rockbiter Weapon':Rockbiter Weapon,
    'Sacrificial Pact':Sacrificial Pact,
    'Sap':Sap,
    'Savage Roar':Savage Roar,
    'Savagery':Savagery,
    'Savannah Highmane':Savannah Highmane,
    'Scarlet Crusader':Scarlet Crusader,
    'Scavenging Hyena':Scavenging Hyena,
    'Sea Giant':Sea Giant,
    'Secretkeeper':Secretkeeper,
    'Sen'jin Shieldmasta':Sen'jin Shieldmasta,
    'Sense Demons':Sense Demons,
    'Shadow Bolt':Shadow Bolt,
    'Shadow Madness':Shadow Madness,
    'Shadow Word: Death':Shadow Word: Death,
    'Shadow Word: Pain':Shadow Word: Pain,
    'Shadowflame':Shadowflame,
    'Shadowform':Shadowform,
    'Shadowstep':Shadowstep,
    'Shattered Sun Cleric':Shattered Sun Cleric,
    'Shield Block':Shield Block,
    'Shield Slam':Shield Slam,
    'Shieldbearer':Shieldbearer,
    'Shiv':Shiv,
    'SI:7 Agent':SI:7 Agent,
    'Silence':Silence,
    'Silver Hand Knight':Silver Hand Knight,
    'Silverback Patriarch':Silverback Patriarch,
    'Silvermoon Guardian':Silvermoon Guardian,
    'Sinister Strike':Sinister Strike,
    'Siphon Soul':Siphon Soul,
    'Slam':Slam,
    'Snake Trap':Snake Trap,
    'Snipe':Snipe,
    'Sorcerer's Apprentice':Sorcerer's Apprentice,
    'Soul of the Forest':Soul of the Forest,
    'Soulfire':Soulfire,
    'Southsea Captain':Southsea Captain,
    'Southsea Deckhand':Southsea Deckhand,
    'Spellbender':Spellbender,
    'Spellbreaker':Spellbreaker,
    'Spiteful Smith':Spiteful Smith,
    'Sprint':Sprint,
    'Stampeding Kodo':Stampeding Kodo,
    'Starfall':Starfall,
    'Starfire':Starfire,
    'Starving Buzzard':Starving Buzzard,
    'Stonetusk Boar':Stonetusk Boar,
    'Stormforged Axe':Stormforged Axe,
    'Stormpike Commando':Stormpike Commando,
    'Stormwind Champion':Stormwind Champion,
    'Stormwind Knight':Stormwind Knight,
    'Stranglethorn Tiger':Stranglethorn Tiger,
    'Succubus':Succubus,
    'Summoning Portal':Summoning Portal,
    'Sunfury Protector':Sunfury Protector,
    'Sunwalker':Sunwalker,
    'Swipe':Swipe,
    'Sword of Justice':Sword of Justice,
    'Sylvanas Windrunner':Sylvanas Windrunner,
    'Tauren Warrior':Tauren Warrior,
    'Temple Enforcer':Temple Enforcer,
    'The Beast':The Beast,
    'The Black Knight':The Black Knight,
    'Thoughtsteal':Thoughtsteal,
    'Thrallmar Farseer':Thrallmar Farseer,
    'Timber Wolf':Timber Wolf,
    'Tinkmaster Overspark':Tinkmaster Overspark,
    'Tirion Fordring':Tirion Fordring,
    'Totemic Might':Totemic Might,
    'Tracking':Tracking,
    'Truesilver Champion':Truesilver Champion,
    'Tundra Rhino':Tundra Rhino,
    'Twilight Drake':Twilight Drake,
    'Twisting Nether':Twisting Nether,
    'Unbound Elemental':Unbound Elemental,
    'Unleash the Hounds':Unleash the Hounds,
    'Upgrade!':Upgrade!,
    'Vanish':Vanish,
    'Vaporize':Vaporize,
    'Venture Co. Mercenary':Venture Co. Mercenary,
    'Violet Teacher':Violet Teacher,
    'Void Terror':Void Terror,
    'Voidwalker':Voidwalker,
    'Voodoo Doctor':Voodoo Doctor,
    'War Golem':War Golem,
    'Warsong Commander':Warsong Commander,
    'Water Elemental':Water Elemental,
    'Whirlwind':Whirlwind,
    'Wild Growth':Wild Growth,
    'Wild Pyromancer':Wild Pyromancer,
    'Windfury':Windfury,
    'Windfury Harpy':Windfury Harpy,
    'Windspeaker':Windspeaker,
    'Wisp':Wisp,
    'Wolfrider':Wolfrider,
    'Worgen Infiltrator':Worgen Infiltrator,
    'Wrath':Wrath,
    'Young Dragonhawk':Young Dragonhawk,
    'Young Priestess':Young Priestess,
    'Youthful Brewmaster':Youthful Brewmaster,
    'Ysera':Ysera,
    }       