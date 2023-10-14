from BaseClasses import Item, ItemClassification, MultiWorld
import typing

from .Options import get_option_value, RequiredTactics
from .MissionTables import SC2Mission, SC2Race, SC2Campaign, campaign_mission_table
from . import ItemNames

class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    type: str
    number: int
    race: SC2Race
    classification: ItemClassification = ItemClassification.useful
    quantity: int = 1
    parent_item: typing.Optional[str] = None
    origin: typing.Set[str] = {"wol"}


class StarcraftItem(Item):
    game: str = "Starcraft 2"


def get_full_item_list():
    return item_table


SC2WOL_ITEM_ID_OFFSET = 1000
SC2HOTS_ITEM_ID_OFFSET = SC2WOL_ITEM_ID_OFFSET + 900

item_table = {
    # WoL
    ItemNames.MARINE: ItemData(0 + SC2WOL_ITEM_ID_OFFSET, "Unit", 0, SC2Race.TERRAN, classification=ItemClassification.progression),
    ItemNames.MEDIC: ItemData(1 + SC2WOL_ITEM_ID_OFFSET, "Unit", 1, SC2Race.TERRAN, classification=ItemClassification.progression),
    ItemNames.FIREBAT: ItemData(2 + SC2WOL_ITEM_ID_OFFSET, "Unit", 2, SC2Race.TERRAN, classification=ItemClassification.progression),
    ItemNames.MARAUDER: ItemData(3 + SC2WOL_ITEM_ID_OFFSET, "Unit", 3, SC2Race.TERRAN, classification=ItemClassification.progression),
    ItemNames.REAPER: ItemData(4 + SC2WOL_ITEM_ID_OFFSET, "Unit", 4, SC2Race.TERRAN, classification=ItemClassification.progression),
    ItemNames.HELLION: ItemData(5 + SC2WOL_ITEM_ID_OFFSET, "Unit", 5, SC2Race.TERRAN, classification=ItemClassification.progression),
    ItemNames.VULTURE: ItemData(6 + SC2WOL_ITEM_ID_OFFSET, "Unit", 6, SC2Race.TERRAN, classification=ItemClassification.progression),
    ItemNames.GOLIATH: ItemData(7 + SC2WOL_ITEM_ID_OFFSET, "Unit", 7, SC2Race.TERRAN, classification=ItemClassification.progression),
    ItemNames.DIAMONDBACK: ItemData(8 + SC2WOL_ITEM_ID_OFFSET, "Unit", 8, SC2Race.TERRAN, classification=ItemClassification.progression),
    ItemNames.SIEGE_TANK: ItemData(9 + SC2WOL_ITEM_ID_OFFSET, "Unit", 9, SC2Race.TERRAN, classification=ItemClassification.progression),
    ItemNames.MEDIVAC: ItemData(10 + SC2WOL_ITEM_ID_OFFSET, "Unit", 10, SC2Race.TERRAN, classification=ItemClassification.progression),
    ItemNames.WRAITH: ItemData(11 + SC2WOL_ITEM_ID_OFFSET, "Unit", 11, SC2Race.TERRAN, classification=ItemClassification.progression),
    ItemNames.VIKING: ItemData(12 + SC2WOL_ITEM_ID_OFFSET, "Unit", 12, SC2Race.TERRAN, classification=ItemClassification.progression),
    ItemNames.BANSHEE: ItemData(13 + SC2WOL_ITEM_ID_OFFSET, "Unit", 13, SC2Race.TERRAN, classification=ItemClassification.progression),
    ItemNames.BATTLECRUISER: ItemData(14 + SC2WOL_ITEM_ID_OFFSET, "Unit", 14, SC2Race.TERRAN, classification=ItemClassification.progression),
    ItemNames.GHOST: ItemData(15 + SC2WOL_ITEM_ID_OFFSET, "Unit", 15, SC2Race.TERRAN, classification=ItemClassification.progression),
    ItemNames.SPECTRE: ItemData(16 + SC2WOL_ITEM_ID_OFFSET, "Unit", 16, SC2Race.TERRAN, classification=ItemClassification.progression),
    ItemNames.THOR: ItemData(17 + SC2WOL_ITEM_ID_OFFSET, "Unit", 17, SC2Race.TERRAN, classification=ItemClassification.progression),
    # EE units
    ItemNames.LIBERATOR: ItemData(18 + SC2WOL_ITEM_ID_OFFSET, "Unit", 18, SC2Race.TERRAN, classification=ItemClassification.progression, origin={"nco", "ext"}),
    ItemNames.VALKYRIE: ItemData(19 + SC2WOL_ITEM_ID_OFFSET, "Unit", 19, SC2Race.TERRAN, classification=ItemClassification.progression, origin={"bw"}),
    ItemNames.WIDOW_MINE: ItemData(20 + SC2WOL_ITEM_ID_OFFSET, "Unit", 20, SC2Race.TERRAN, classification=ItemClassification.progression, origin={"ext"}),
    ItemNames.CYCLONE: ItemData(21 + SC2WOL_ITEM_ID_OFFSET, "Unit", 21, SC2Race.TERRAN, classification=ItemClassification.progression, origin={"ext"}),

    # Some other items are moved to Upgrade group because of the way how the bot message is parsed
    ItemNames.PROGRESSIVE_TERRAN_INFANTRY_WEAPON: ItemData(100 + SC2WOL_ITEM_ID_OFFSET, "Upgrade", 0, SC2Race.TERRAN, quantity=3),
    ItemNames.PROGRESSIVE_TERRAN_INFANTRY_ARMOR: ItemData(102 + SC2WOL_ITEM_ID_OFFSET, "Upgrade", 2, SC2Race.TERRAN, quantity=3),
    ItemNames.PROGRESSIVE_TERRAN_VEHICLE_WEAPON: ItemData(103 + SC2WOL_ITEM_ID_OFFSET, "Upgrade", 4, SC2Race.TERRAN, quantity=3),
    ItemNames.PROGRESSIVE_TERRAN_VEHICLE_ARMOR: ItemData(104 + SC2WOL_ITEM_ID_OFFSET, "Upgrade", 6, SC2Race.TERRAN, quantity=3),
    ItemNames.PROGRESSIVE_TERRAN_SHIP_WEAPON: ItemData(105 + SC2WOL_ITEM_ID_OFFSET, "Upgrade", 8, SC2Race.TERRAN, quantity=3),
    ItemNames.PROGRESSIVE_TERRAN_SHIP_ARMOR: ItemData(106 + SC2WOL_ITEM_ID_OFFSET, "Upgrade", 10, SC2Race.TERRAN, quantity=3),
    # Upgrade bundle 'number' values are used as indices to get affected 'number's
    ItemNames.PROGRESSIVE_TERRAN_WEAPON_UPGRADE: ItemData(107 + SC2WOL_ITEM_ID_OFFSET, "Upgrade", 0, SC2Race.TERRAN, quantity=3),
    ItemNames.PROGRESSIVE_TERRAN_ARMOR_UPGRADE: ItemData(108 + SC2WOL_ITEM_ID_OFFSET, "Upgrade", 1, SC2Race.TERRAN, quantity=3),
    ItemNames.PROGRESSIVE_TERRAN_INFANTRY_UPGRADE: ItemData(109 + SC2WOL_ITEM_ID_OFFSET, "Upgrade", 2, SC2Race.TERRAN, quantity=3),
    ItemNames.PROGRESSIVE_TERRAN_VEHICLE_UPGRADE: ItemData(110 + SC2WOL_ITEM_ID_OFFSET, "Upgrade", 3, SC2Race.TERRAN, quantity=3),
    ItemNames.PROGRESSIVE_TERRAN_SHIP_UPGRADE: ItemData(111 + SC2WOL_ITEM_ID_OFFSET, "Upgrade", 4, SC2Race.TERRAN, quantity=3),
    ItemNames.PROGRESSIVE_TERRAN_WEAPON_ARMOR_UPGRADE: ItemData(112 + SC2WOL_ITEM_ID_OFFSET, "Upgrade", 5, SC2Race.TERRAN, quantity=3),

    ItemNames.BUNKER_PROJECTILE_ACCELERATOR: ItemData(200 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 0, SC2Race.TERRAN, parent_item="Bunker"),
    ItemNames.BUNKER_NEOSTEEL_BUNKER: ItemData(201 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 1, SC2Race.TERRAN, parent_item="Bunker"),
    ItemNames.MISSILE_TURRET_TITANIUM_HOUSING: ItemData(202 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 2, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Missile Turret"),
    ItemNames.MISSILE_TURRET_HELLSTORM_BATTERIES: ItemData(203 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 3, SC2Race.TERRAN, parent_item="Missile Turret"),
    ItemNames.SCV_ADVANCED_CONSTRUCTION: ItemData(204 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 4, SC2Race.TERRAN),
    ItemNames.SCV_DUAL_FUSION_WELDERS: ItemData(205 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 5, SC2Race.TERRAN),
    ItemNames.BUILDING_FIRE_SUPPRESSION_SYSTEM: ItemData(206 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 6, SC2Race.TERRAN),
    ItemNames.BUILDING_ORBITAL_COMMAND: ItemData(207 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 7, SC2Race.TERRAN),
    ItemNames.MARINE_PROGRESSIVE_STIMPACK: ItemData(208 + SC2WOL_ITEM_ID_OFFSET, "Progressive Upgrade", 0, SC2Race.TERRAN, parent_item="Marine", quantity=2),
    ItemNames.MARINE_COMBAT_SHIELD: ItemData(209 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 9, SC2Race.TERRAN, classification=ItemClassification.progression, parent_item="Marine"),
    ItemNames.MEDIC_ADVANCED_MEDIC_FACILITIES: ItemData(210 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 10, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Medic"),
    ItemNames.MEDIC_STABILIZER_MEDPACKS: ItemData(211 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 11, SC2Race.TERRAN, classification=ItemClassification.progression, parent_item="Medic"),
    ItemNames.FIREBAT_INCINERATOR_GAUNTLETS: ItemData(212 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 12, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Firebat"),
    ItemNames.FIREBAT_JUGGERNAUT_PLATING: ItemData(213 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 13, SC2Race.TERRAN, parent_item="Firebat"),
    ItemNames.MARAUDER_CONCUSSIVE_SHELLS: ItemData(214 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 14, SC2Race.TERRAN, parent_item="Marauder"),
    ItemNames.MARAUDER_KINETIC_FOAM: ItemData(215 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 15, SC2Race.TERRAN, parent_item="Marauder"),
    ItemNames.REAPER_U238_ROUNDS: ItemData(216 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 16, SC2Race.TERRAN, parent_item="Reaper"),
    ItemNames.REAPER_G4_CLUSTERBOMB: ItemData(217 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 17, SC2Race.TERRAN, classification=ItemClassification.progression, parent_item="Reaper"),
    # Items from EE
    ItemNames.CYCLONE_MAG_FIELD_ACCELERATORS: ItemData(218 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 18, SC2Race.TERRAN, parent_item="Cyclone", origin={"ext"}),
    ItemNames.CYCLONE_MAG_FIELD_LAUNCHERS: ItemData(219 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 19, SC2Race.TERRAN, parent_item="Cyclone", origin={"ext"}),
    # Items from new mod
    ItemNames.MARINE_LASER_TARGETING_SYSTEM: ItemData(220 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 8, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Marine", origin={"nco"}), # Freed slot from Stimpack
    ItemNames.MARINE_MAGRAIL_MUNITIONS: ItemData(221 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 20, SC2Race.TERRAN, parent_item="Marine", origin={"nco"}),
    ItemNames.MARINE_OPTIMIZED_LOGISTICS: ItemData(222 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 21, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Marine", origin={"nco"}),
    ItemNames.MEDIC_RESTORATION: ItemData(223 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 22, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Medic", origin={"bw"}),
    ItemNames.MEDIC_OPTICAL_FLARE: ItemData(224 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 23, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Medic", origin={"bw"}),
    ItemNames.MEDIC_OPTIMIZED_LOGISTICS: ItemData(225 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 24, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Medic", origin={"bw"}),
    ItemNames.FIREBAT_PROGRESSIVE_STIMPACK: ItemData(226 + SC2WOL_ITEM_ID_OFFSET, "Progressive Upgrade", 6, SC2Race.TERRAN, parent_item="Firebat", quantity=2, origin={"bw"}),
    ItemNames.FIREBAT_OPTIMIZED_LOGISTICS: ItemData(227 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 25, SC2Race.TERRAN, parent_item="Firebat", origin={"bw"}),
    ItemNames.MARAUDER_PROGRESSIVE_STIMPACK: ItemData(228 + SC2WOL_ITEM_ID_OFFSET, "Progressive Upgrade", 8, SC2Race.TERRAN, parent_item="Marauder", quantity=2, origin={"nco"}),
    ItemNames.MARAUDER_LASER_TARGETING_SYSTEM: ItemData(229 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 26, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Marauder", origin={"nco"}),
    ItemNames.MARAUDER_MAGRAIL_MUNITIONS: ItemData(230 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 27, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Marauder", origin={"nco"}),
    ItemNames.MARAUDER_INTERNAL_TECH_MODULE: ItemData(231 + SC2WOL_ITEM_ID_OFFSET, "Armory 1", 28, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Marauder", origin={"nco"}),

    # Items from new mod
    ItemNames.REAPER_PROGRESSIVE_STIMPACK: ItemData(250 + SC2WOL_ITEM_ID_OFFSET, "Progressive Upgrade", 10, SC2Race.TERRAN, parent_item="Reaper", quantity=2, origin={"nco"}),
    ItemNames.REAPER_LASER_TARGETING_SYSTEM: ItemData(251 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 0, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Reaper", origin={"nco"}),
    ItemNames.REAPER_ADVANCED_CLOAKING_FIELD: ItemData(252 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 1, SC2Race.TERRAN, parent_item="Reaper", origin={"nco"}),
    ItemNames.REAPER_SPIDER_MINES: ItemData(253 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 2, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Reaper", origin={"nco"}),
    ItemNames.REAPER_COMBAT_DRUGS: ItemData(254 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 3, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Reaper", origin={"ext"}),
    ItemNames.HELLION_HELLBAT_ASPECT: ItemData(255 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 4, SC2Race.TERRAN, parent_item="Hellion", origin={"nco"}),
    ItemNames.HELLION_SMART_SERVOS: ItemData(256 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 5, SC2Race.TERRAN, parent_item="Hellion", origin={"nco"}),
    ItemNames.HELLION_OPTIMIZED_LOGISTICS: ItemData(257 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 6, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Hellion", origin={"nco"}),
    ItemNames.HELLION_JUMP_JETS: ItemData(258 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 7, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Hellion", origin={"nco"}),
    ItemNames.HELLION_PROGRESSIVE_STIMPACK: ItemData(259 + SC2WOL_ITEM_ID_OFFSET, "Progressive Upgrade", 12, SC2Race.TERRAN, parent_item="Hellion", quantity=2, origin={"nco"}),
    ItemNames.VULTURE_ION_THRUSTERS: ItemData(260 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 8, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Vulture", origin={"bw"}),
    ItemNames.VULTURE_AUTO_LAUNCHERS: ItemData(261 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 9, SC2Race.TERRAN, parent_item="Vulture", origin={"bw"}),
    ItemNames.SPIDER_MINE_HIGH_EXPLOSIVE_MUNITION: ItemData(262 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 10, SC2Race.TERRAN, origin={"bw"}),
    ItemNames.GOLIATH_JUMP_JETS: ItemData(263 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 11, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Goliath", origin={"nco"}),
    ItemNames.GOLIATH_OPTIMIZED_LOGISTICS: ItemData(264 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 12, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Goliath", origin={"nco"}),
    ItemNames.DIAMONDBACK_HYPERFLUXOR: ItemData(265 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 13, SC2Race.TERRAN, parent_item="Diamondback", origin={"ext"}),
    ItemNames.DIAMONDBACK_BURST_CAPACITORS: ItemData(266 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 14, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Diamondback", origin={"ext"}),
    ItemNames.DIAMONDBACK_OPTIMIZED_LOGISTICS: ItemData(267 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 15, SC2Race.TERRAN, parent_item="Diamondback", origin={"ext"}),
    ItemNames.SIEGE_TANK_JUMP_JETS: ItemData(268 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 16, SC2Race.TERRAN, parent_item="Siege Tank", origin={"nco"}),
    ItemNames.SIEGE_TANK_SPIDER_MINES: ItemData(269 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 17, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Siege Tank", origin={"nco"}),
    ItemNames.SIEGE_TANK_SMART_SERVOS: ItemData(270 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 18, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Siege Tank", origin={"nco"}),
    ItemNames.SIEGE_TANK_GRADUATING_RANGE: ItemData(271 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 19, SC2Race.TERRAN, classification=ItemClassification.progression, parent_item="Siege Tank", origin={"ext"}),
    ItemNames.SIEGE_TANK_LASER_TARGETING_SYSTEM: ItemData(272 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 20, SC2Race.TERRAN, parent_item="Siege Tank", origin={"nco"}),
    ItemNames.SIEGE_TANK_ADVANCED_SIEGE_TECH: ItemData(273 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 21, SC2Race.TERRAN, parent_item="Siege Tank", origin={"ext"}),
    ItemNames.SIEGE_TANK_INTERNAL_TECH_MODULE: ItemData(274 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 22, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Siege Tank", origin={"nco"}),
    ItemNames.PREDATOR_OPTIMIZED_LOGISTICS: ItemData(275 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 23, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Predator", origin={"ext"}),
    ItemNames.MEDIVAC_EXPANDED_HULL: ItemData(276 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 24, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Medivac", origin={"ext"}),
    ItemNames.MEDIVAC_AFTERBURNERS: ItemData(277 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 25, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Medivac", origin={"ext"}),
    ItemNames.WRAITH_ADVANCED_LASER_TECHNOLOGY: ItemData(278 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 26, SC2Race.TERRAN, classification=ItemClassification.progression, parent_item="Wraith", origin={"ext"}),
    ItemNames.VIKING_SMART_SERVOS: ItemData(279 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 27, SC2Race.TERRAN, parent_item="Viking", origin={"ext"}),
    ItemNames.VIKING_MAGRAIL_MUNITIONS: ItemData(280 + SC2WOL_ITEM_ID_OFFSET, "Armory 3", 28, SC2Race.TERRAN, parent_item="Viking", origin={"ext"}),

    ItemNames.HELLION_TWIN_LINKED_FLAMETHROWER: ItemData(300 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 0, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Hellion"),
    ItemNames.HELLION_THERMITE_FILAMENTS: ItemData(301 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 1, SC2Race.TERRAN, parent_item="Hellion"),
    ItemNames.SPIDER_MINE_CERBERUS_MINE: ItemData(302 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 2, SC2Race.TERRAN, classification=ItemClassification.filler),
    ItemNames.VULTURE_REPLENISHABLE_MAGAZINE: ItemData(303 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 3, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Vulture"),
    ItemNames.GOLIATH_MULTI_LOCK_WEAPONS_SYSTEM: ItemData(304 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 4, SC2Race.TERRAN, parent_item="Goliath"),
    ItemNames.GOLIATH_ARES_CLASS_TARGETING_SYSTEM: ItemData(305 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 5, SC2Race.TERRAN, parent_item="Goliath"),
    ItemNames.DIAMONDBACK_TRI_LITHIUM_POWER_CELL: ItemData(306 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 6, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Diamondback"),
    ItemNames.DIAMONDBACK_SHAPED_HULL: ItemData(307 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 7, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Diamondback"),
    ItemNames.SIEGE_TANK_MAELSTROM_ROUNDS: ItemData(308 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 8, SC2Race.TERRAN, classification=ItemClassification.progression, parent_item="Siege Tank"),
    ItemNames.SIEGE_TANK_SHAPED_BLAST: ItemData(309 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 9, SC2Race.TERRAN, parent_item="Siege Tank"),
    ItemNames.MEDIVAC_RAPID_DEPLOYMENT_TUBE: ItemData(310 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 10, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Medivac"),
    ItemNames.MEDIVAC_ADVANCED_HEALING_AI: ItemData(311 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 11, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Medivac"),
    ItemNames.WRAITH_TOMAHAWK_POWER_CELLS: ItemData(312 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 12, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Wraith"),
    ItemNames.WRAITH_DISPLACEMENT_FIELD: ItemData(313 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 13, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Wraith"),
    ItemNames.VIKING_RIPWAVE_MISSILES: ItemData(314 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 14, SC2Race.TERRAN, parent_item="Viking"),
    ItemNames.VIKING_PHOBOS_CLASS_WEAPONS_SYSTEM: ItemData(315 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 15, SC2Race.TERRAN, parent_item="Viking"),
    ItemNames.BANSHEE_PROGRESSIVE_CROSS_SPECTRUM_DAMPENERS: ItemData(316 + SC2WOL_ITEM_ID_OFFSET, "Progressive Upgrade", 2, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Banshee", quantity=2),
    ItemNames.BANSHEE_SHOCKWAVE_MISSILE_BATTERY: ItemData(317 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 17, SC2Race.TERRAN, parent_item="Banshee"),
    ItemNames.BATTLECRUISER_MISSILE_PODS: ItemData(318 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 18, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Battlecruiser"),
    ItemNames.BATTLECRUISER_DEFENSIVE_MATRIX: ItemData(319 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 19, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Battlecruiser"),
    ItemNames.GHOST_OCULAR_IMPLANTS: ItemData(320 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 20, SC2Race.TERRAN, parent_item="Ghost"),
    ItemNames.GHOST_CRIUS_SUIT: ItemData(321 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 21, SC2Race.TERRAN, parent_item="Ghost"),
    ItemNames.SPECTRE_PSIONIC_LASH: ItemData(322 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 22, SC2Race.TERRAN, classification=ItemClassification.progression, parent_item="Spectre"),
    ItemNames.SPECTRE_NYX_CLASS_CLOAKING_MODULE: ItemData(323 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 23, SC2Race.TERRAN, parent_item="Spectre"),
    ItemNames.THOR_330MM_BARRAGE_CANNON: ItemData(324 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 24, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Thor"),
    ItemNames.THOR_IMMORTALITY_PROTOCOL: ItemData(325 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 25, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Thor"),
    # Items from EE
    ItemNames.LIBERATOR_ADVANCED_BALLISTICS: ItemData(326 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 26, SC2Race.TERRAN, parent_item="Liberator", origin={"ext"}),
    ItemNames.LIBERATOR_RAID_ARTILLERY: ItemData(327 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 27, SC2Race.TERRAN, classification=ItemClassification.progression, parent_item="Liberator", origin={"nco"}),
    ItemNames.WIDOW_MINE_DRILLING_CLAWS: ItemData(328 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 28, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Widow Mine", origin={"ext"}),
    ItemNames.WIDOW_MINE_CONCEALMENT: ItemData(329 + SC2WOL_ITEM_ID_OFFSET, "Armory 2", 29, SC2Race.TERRAN, classification=ItemClassification.progression, parent_item="Widow Mine", origin={"ext"}),

    #Items from new mod
    ItemNames.BANSHEE_HYPERFLIGHT_ROTORS: ItemData(350 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 0, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Banshee", origin={"ext"}),
    ItemNames.BANSHEE_LASER_TARGETING_SYSTEM: ItemData(351 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 1, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Banshee", origin={"nco"}),
    ItemNames.BANSHEE_INTERNAL_TECH_MODULE: ItemData(352 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 2, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Banshee", origin={"nco"}),
    ItemNames.BATTLECRUISER_TACTICAL_JUMP: ItemData(353 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 3, SC2Race.TERRAN, parent_item="Battlecruiser", origin={"nco", "ext"}),
    ItemNames.BATTLECRUISER_CLOAK: ItemData(354 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 4, SC2Race.TERRAN, parent_item="Battlecruiser", origin={"nco"}),
    ItemNames.BATTLECRUISER_ATX_LASER_BATTERY: ItemData(355 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 5, SC2Race.TERRAN, classification=ItemClassification.progression, parent_item="Battlecruiser", origin={"nco"}),
    ItemNames.BATTLECRUISER_OPTIMIZED_LOGISTICS: ItemData(356 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 6, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Battlecruiser", origin={"ext"}),
    ItemNames.BATTLECRUISER_INTERNAL_TECH_MODULE: ItemData(357 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 7, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Battlecruiser", origin={"nco"}),
    ItemNames.GHOST_EMP_ROUNDS: ItemData(358 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 8, SC2Race.TERRAN, parent_item="Ghost", origin={"ext"}),
    ItemNames.GHOST_LOCKDOWN: ItemData(359 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 9, SC2Race.TERRAN, parent_item="Ghost", origin={"bw"}),
    ItemNames.SPECTRE_IMPALER_ROUNDS: ItemData(360 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 10, SC2Race.TERRAN, parent_item="Spectre", origin={"ext"}),
    ItemNames.THOR_PROGRESSIVE_HIGH_IMPACT_PAYLOAD: ItemData(361 + SC2WOL_ITEM_ID_OFFSET, "Progressive Upgrade", 14, SC2Race.TERRAN, parent_item="Thor", quantity=2, origin={"ext"}),  # L2 is Smart Servos
    ItemNames.RAVEN_BIO_MECHANICAL_REPAIR_DRONE: ItemData(363 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 13, SC2Race.TERRAN, parent_item="Raven", origin={"nco"}),
    ItemNames.RAVEN_SPIDER_MINES: ItemData(364 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 14, SC2Race.TERRAN, parent_item="Raven", origin={"nco"}),
    ItemNames.RAVEN_RAILGUN_TURRET: ItemData(365 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 15, SC2Race.TERRAN, parent_item="Raven", origin={"nco"}),
    ItemNames.RAVEN_HUNTER_SEEKER_WEAPON: ItemData(366 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 16, SC2Race.TERRAN, parent_item="Raven", origin={"nco"}),
    ItemNames.RAVEN_INTERFERENCE_MATRIX: ItemData(367 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 17, SC2Race.TERRAN, parent_item="Raven", origin={"ext"}),
    ItemNames.RAVEN_ANTI_ARMOR_MISSILE: ItemData(368 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 18, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Raven", origin={"ext"}),
    ItemNames.RAVEN_INTERNAL_TECH_MODULE: ItemData(369 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 19, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Raven", origin={"nco"}),
    ItemNames.SCIENCE_VESSEL_EMP_SHOCKWAVE: ItemData(370 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 20, SC2Race.TERRAN, parent_item="Science Vessel", origin={"bw"}),
    ItemNames.SCIENCE_VESSEL_DEFENSIVE_MATRIX: ItemData(371 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 21, SC2Race.TERRAN, parent_item="Science Vessel", origin={"bw"}),
    ItemNames.CYCLONE_TARGETING_OPTICS: ItemData(372 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 22, SC2Race.TERRAN, parent_item="Cyclone", origin={"ext"}),
    ItemNames.CYCLONE_RAPID_FIRE_LAUNCHERS: ItemData(373 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 23, SC2Race.TERRAN, parent_item="Cyclone", origin={"ext"}),
    ItemNames.LIBERATOR_CLOAK: ItemData(374 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 24, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Liberator", origin={"nco"}),
    ItemNames.LIBERATOR_LASER_TARGETING_SYSTEM: ItemData(375 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 25, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Liberator", origin={"ext"}),
    ItemNames.LIBERATOR_OPTIMIZED_LOGISTICS: ItemData(376 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 26, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Liberator", origin={"nco"}),
    ItemNames.WIDOW_MINE_BLACK_MARKET_LAUNCHERS: ItemData(377 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 27, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Widow Mine", origin={"ext"}),
    ItemNames.WIDOW_MINE_EXECUTIONER_MISSILES: ItemData(378 + SC2WOL_ITEM_ID_OFFSET, "Armory 4", 28, SC2Race.TERRAN, parent_item="Widow Mine", origin={"ext"}),

    # Just lazy to create a new group for one unit
    ItemNames.VALKYRIE_ENHANCED_CLUSTER_LAUNCHERS: ItemData(379 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 17, SC2Race.TERRAN, parent_item="Valkyrie", origin={"ext"}),
    ItemNames.VALKYRIE_SHAPED_HULL: ItemData(380 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 20, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Valkyrie", origin={"ext"}),
    ItemNames.VALKYRIE_BURST_LASERS: ItemData(381 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 21, SC2Race.TERRAN, parent_item="Valkyrie", origin={"ext"}),
    ItemNames.VALKYRIE_AFTERBURNERS: ItemData(382 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 22, SC2Race.TERRAN, classification=ItemClassification.filler, parent_item="Valkyrie", origin={"ext"}),

    ItemNames.BUNKER: ItemData(400 + SC2WOL_ITEM_ID_OFFSET, "Building", 0, SC2Race.TERRAN, classification=ItemClassification.progression),
    ItemNames.MISSILE_TURRET: ItemData(401 + SC2WOL_ITEM_ID_OFFSET, "Building", 1, SC2Race.TERRAN, classification=ItemClassification.progression),
    ItemNames.SENSOR_TOWER: ItemData(402 + SC2WOL_ITEM_ID_OFFSET, "Building", 2, SC2Race.TERRAN),

    ItemNames.WAR_PIGS: ItemData(500 + SC2WOL_ITEM_ID_OFFSET, "Mercenary", 0, SC2Race.TERRAN, classification=ItemClassification.progression),
    ItemNames.DEVIL_DOGS: ItemData(501 + SC2WOL_ITEM_ID_OFFSET, "Mercenary", 1, SC2Race.TERRAN, classification=ItemClassification.filler),
    ItemNames.HAMMER_SECURITIES: ItemData(502 + SC2WOL_ITEM_ID_OFFSET, "Mercenary", 2, SC2Race.TERRAN),
    ItemNames.SPARTAN_COMPANY: ItemData(503 + SC2WOL_ITEM_ID_OFFSET, "Mercenary", 3, SC2Race.TERRAN, classification=ItemClassification.progression),
    ItemNames.SIEGE_BREAKERS: ItemData(504 + SC2WOL_ITEM_ID_OFFSET, "Mercenary", 4, SC2Race.TERRAN),
    ItemNames.HELS_ANGEL: ItemData(505 + SC2WOL_ITEM_ID_OFFSET, "Mercenary", 5, SC2Race.TERRAN, classification=ItemClassification.progression),
    ItemNames.DUSK_WINGS: ItemData(506 + SC2WOL_ITEM_ID_OFFSET, "Mercenary", 6, SC2Race.TERRAN),
    ItemNames.JACKSONS_REVENGE: ItemData(507 + SC2WOL_ITEM_ID_OFFSET, "Mercenary", 7, SC2Race.TERRAN),

    ItemNames.ULTRA_CAPACITORS: ItemData(600 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 0, SC2Race.TERRAN),
    ItemNames.VANADIUM_PLATING: ItemData(601 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 1, SC2Race.TERRAN),
    ItemNames.ORBITAL_DEPOTS: ItemData(602 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 2, SC2Race.TERRAN),
    ItemNames.MICRO_FILTERING: ItemData(603 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 3, SC2Race.TERRAN),
    ItemNames.AUTOMATED_REFINERY: ItemData(604 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 4, SC2Race.TERRAN),
    ItemNames.COMMAND_CENTER_REACTOR: ItemData(605 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 5, SC2Race.TERRAN),
    ItemNames.RAVEN: ItemData(606 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 6, SC2Race.TERRAN),
    ItemNames.SCIENCE_VESSEL: ItemData(607 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 7, SC2Race.TERRAN, classification=ItemClassification.progression),
    ItemNames.TECH_REACTOR: ItemData(608 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 8, SC2Race.TERRAN),
    ItemNames.ORBITAL_STRIKE: ItemData(609 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 9, SC2Race.TERRAN),
    ItemNames.BUNKER_SHRIKE_TURRET: ItemData(610 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 10, SC2Race.TERRAN, parent_item="Bunker"),
    ItemNames.BUNKER_FORTIFIED_BUNKER: ItemData(611 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 11, SC2Race.TERRAN, parent_item="Bunker"),
    ItemNames.PLANETARY_FORTRESS: ItemData(612 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 12, SC2Race.TERRAN, classification=ItemClassification.progression),
    ItemNames.PERDITION_TURRET: ItemData(613 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 13, SC2Race.TERRAN, classification=ItemClassification.progression),
    ItemNames.PREDATOR: ItemData(614 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 14, SC2Race.TERRAN, classification=ItemClassification.filler),
    ItemNames.HERCULES: ItemData(615 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 15, SC2Race.TERRAN, classification=ItemClassification.progression),
    ItemNames.CELLULAR_REACTOR: ItemData(616 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 16, SC2Race.TERRAN),
    ItemNames.PROGRESSIVE_REGENERATIVE_BIO_STEEL: ItemData(617 + SC2WOL_ITEM_ID_OFFSET, "Progressive Upgrade", 4, SC2Race.TERRAN, quantity=2),
    ItemNames.HIVE_MIND_EMULATOR: ItemData(618 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 18, SC2Race.TERRAN, ItemClassification.progression),
    ItemNames.PSI_DISRUPTER: ItemData(619 + SC2WOL_ITEM_ID_OFFSET, "Laboratory", 19, SC2Race.TERRAN, classification=ItemClassification.progression),

    ItemNames.ZEALOT: ItemData(700 + SC2WOL_ITEM_ID_OFFSET, "Unit", 0, SC2Race.PROTOSS, classification=ItemClassification.progression),
    ItemNames.STALKER: ItemData(701 + SC2WOL_ITEM_ID_OFFSET, "Unit", 1, SC2Race.PROTOSS, classification=ItemClassification.progression),
    ItemNames.HIGH_TEMPLAR: ItemData(702 + SC2WOL_ITEM_ID_OFFSET, "Unit", 2, SC2Race.PROTOSS, classification=ItemClassification.progression),
    ItemNames.DARK_TEMPLAR: ItemData(703 + SC2WOL_ITEM_ID_OFFSET, "Unit", 3, SC2Race.PROTOSS, classification=ItemClassification.progression),
    ItemNames.IMMORTAL: ItemData(704 + SC2WOL_ITEM_ID_OFFSET, "Unit", 4, SC2Race.PROTOSS, classification=ItemClassification.progression),
    ItemNames.COLOSSUS: ItemData(705 + SC2WOL_ITEM_ID_OFFSET, "Unit", 5, SC2Race.PROTOSS),
    ItemNames.PHOENIX: ItemData(706 + SC2WOL_ITEM_ID_OFFSET, "Unit", 6, SC2Race.PROTOSS, classification=ItemClassification.filler),
    ItemNames.VOID_RAY: ItemData(707 + SC2WOL_ITEM_ID_OFFSET, "Unit", 7, SC2Race.PROTOSS, classification=ItemClassification.progression),
    ItemNames.CARRIER: ItemData(708 + SC2WOL_ITEM_ID_OFFSET, "Unit", 8, SC2Race.PROTOSS, classification=ItemClassification.progression),

    # Filler items to fill remaining spots
    ItemNames.STARTING_MINERALS: ItemData(800 + SC2WOL_ITEM_ID_OFFSET, "Minerals", 15, SC2Race.ANY, quantity=0, classification=ItemClassification.filler),
    ItemNames.STARTING_VESPENE: ItemData(801 + SC2WOL_ITEM_ID_OFFSET, "Vespene", 15, SC2Race.ANY, quantity=0, classification=ItemClassification.filler),
    # This Filler item isn't placed by the generator yet unless plando'd
    ItemNames.STARTING_SUPPLY: ItemData(802 + SC2WOL_ITEM_ID_OFFSET, "Supply", 2, SC2Race.ANY, quantity=0, classification=ItemClassification.filler),
    # This item is used to "remove" location from the game. Never placed unless plando'd
    ItemNames.NOTHING: ItemData(803 + SC2WOL_ITEM_ID_OFFSET, "Nothing Group", 2, SC2Race.ANY, quantity=0, classification=ItemClassification.trap),

    # ItemNames.KEYSTONE_PIECE: ItemData(850 + SC2WOL_ITEM_ID_OFFSET, "Goal", 0, quantity=0, classification=ItemClassification.progression_skip_balancing)

    # HotS
    ItemNames.ZERGLING: ItemData(0 + SC2HOTS_ITEM_ID_OFFSET, "Unit", 0, SC2Race.ZERG, classification=ItemClassification.progression, origin={"hots"}),
    ItemNames.SWARM_QUEEN: ItemData(1 + SC2HOTS_ITEM_ID_OFFSET, "Unit", 1, SC2Race.ZERG, classification=ItemClassification.progression, origin={"hots"}),
    ItemNames.ROACH: ItemData(2 + SC2HOTS_ITEM_ID_OFFSET, "Unit", 2, SC2Race.ZERG, classification=ItemClassification.progression, origin={"hots"}),
    ItemNames.HYDRALISK: ItemData(3 + SC2HOTS_ITEM_ID_OFFSET, "Unit", 3, SC2Race.ZERG, classification=ItemClassification.progression, origin={"hots"}),
    ItemNames.BANELING: ItemData(4 + SC2HOTS_ITEM_ID_OFFSET, "Unit", 4, SC2Race.ZERG, classification=ItemClassification.progression, origin={"hots"}),
    ItemNames.ABERRATION: ItemData(5 + SC2HOTS_ITEM_ID_OFFSET, "Unit", 5, SC2Race.ZERG, classification=ItemClassification.progression, origin={"hots"}),
    ItemNames.MUTALISK: ItemData(6 + SC2HOTS_ITEM_ID_OFFSET, "Unit", 6, SC2Race.ZERG, classification=ItemClassification.progression, origin={"hots"}),
    ItemNames.SWARM_HOST: ItemData(7 + SC2HOTS_ITEM_ID_OFFSET, "Unit", 7, SC2Race.ZERG, classification=ItemClassification.progression, origin={"hots"}),
    ItemNames.INFESTOR: ItemData(8 + SC2HOTS_ITEM_ID_OFFSET, "Unit", 8, SC2Race.ZERG, classification=ItemClassification.progression, origin={"hots"}),
    ItemNames.ULTRALISK: ItemData(9 + SC2HOTS_ITEM_ID_OFFSET, "Unit", 9, SC2Race.ZERG, classification=ItemClassification.progression, origin={"hots"}),
    ItemNames.SPORE_CRAWLER: ItemData(10 + SC2HOTS_ITEM_ID_OFFSET, "Unit", 10, SC2Race.ZERG, classification=ItemClassification.progression, origin={"hots"}),
    ItemNames.SPINE_CRAWLER: ItemData(11 + SC2HOTS_ITEM_ID_OFFSET, "Unit", 11, SC2Race.ZERG, classification=ItemClassification.progression, origin={"hots"}),
    
    ItemNames.PROGRESSIVE_ZERG_MELEE_ATTACK: ItemData(100 + SC2HOTS_ITEM_ID_OFFSET, "Upgrade", 0, SC2Race.ZERG, quantity=3, origin={"hots"}),
    ItemNames.PROGRESSIVE_ZERG_MISSILE_ATTACK: ItemData(101 + SC2HOTS_ITEM_ID_OFFSET, "Upgrade", 2, SC2Race.ZERG, quantity=3, origin={"hots"}),
    ItemNames.PROGRESSIVE_ZERG_GROUND_CARAPACE: ItemData(102 + SC2HOTS_ITEM_ID_OFFSET, "Upgrade", 4, SC2Race.ZERG, quantity=3, origin={"hots"}),
    ItemNames.PROGRESSIVE_ZERG_FLYER_ATTACK: ItemData(103 + SC2HOTS_ITEM_ID_OFFSET, "Upgrade", 6, SC2Race.ZERG, quantity=3, origin={"hots"}),
    ItemNames.PROGRESSIVE_ZERG_FLYER_CARAPACE: ItemData(104 + SC2HOTS_ITEM_ID_OFFSET, "Upgrade", 8, SC2Race.ZERG, quantity=3, origin={"hots"}),
    # Upgrade bundle 'number' values are used as indices to get affected 'number's
    ItemNames.PROGRESSIVE_ZERG_WEAPON_UPGRADE: ItemData(105 + SC2HOTS_ITEM_ID_OFFSET, "Upgrade", 6, SC2Race.ZERG, quantity=3, origin={"hots"}),
    ItemNames.PROGRESSIVE_ZERG_ARMOR_UPGRADE: ItemData(106 + SC2HOTS_ITEM_ID_OFFSET, "Upgrade", 7, SC2Race.ZERG, quantity=3, origin={"hots"}),
    ItemNames.PROGRESSIVE_ZERG_GROUND_UPGRADE: ItemData(107 + SC2HOTS_ITEM_ID_OFFSET, "Upgrade", 8, SC2Race.ZERG, quantity=3, origin={"hots"}),
    ItemNames.PROGRESSIVE_ZERG_FLYER_UPGRADE: ItemData(108 + SC2HOTS_ITEM_ID_OFFSET, "Upgrade", 9, SC2Race.ZERG, quantity=3, origin={"hots"}),
    ItemNames.PROGRESSIVE_ZERG_WEAPON_ARMOR_UPGRADE: ItemData(109 + SC2HOTS_ITEM_ID_OFFSET, "Upgrade", 10, SC2Race.ZERG, quantity=3, origin={"hots"}),

    ItemNames.ZERGLING_HARDENED_CARAPACE: ItemData(200 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 0, SC2Race.ZERG, parent_item="Zergling", origin={"hots"}),
    ItemNames.ZERGLING_ADRENAL_OVERLOAD: ItemData(201 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 1, SC2Race.ZERG, parent_item="Zergling", origin={"hots"}),
    ItemNames.ZERGLING_METABOLIC_BOOST: ItemData(202 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 2, SC2Race.ZERG, parent_item="Zergling", origin={"hots"}, classification=ItemClassification.filler),
    ItemNames.ROACH_HYDRIODIC_BILE: ItemData(203 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 3, SC2Race.ZERG, parent_item="Roach", origin={"hots"}),
    ItemNames.ROACH_ADAPTIVE_PLATING: ItemData(204 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 4, SC2Race.ZERG, parent_item="Roach", origin={"hots"}),
    ItemNames.ROACH_TUNNELING_CLAWS: ItemData(205 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 5, SC2Race.ZERG, parent_item="Roach", origin={"hots"}, classification=ItemClassification.filler),
    ItemNames.HYDRALISK_FRENZY: ItemData(206 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 6, SC2Race.ZERG, parent_item="Hydralisk", origin={"hots"}),
    ItemNames.HYDRALISK_ANCILLARY_CARAPACE: ItemData(207 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 7, SC2Race.ZERG, parent_item="Hydralisk", origin={"hots"}, classification=ItemClassification.filler),
    ItemNames.HYDRALISK_GROOVED_SPINES: ItemData(208 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 8, SC2Race.ZERG, parent_item="Hydralisk", origin={"hots"}),
    ItemNames.BANELING_CORROSIVE_ACID: ItemData(209 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 9, SC2Race.ZERG, parent_item="Baneling", origin={"hots"}),
    ItemNames.BANELING_RUPTURE: ItemData(210 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 10, SC2Race.ZERG, parent_item="Baneling", origin={"hots"}, classification=ItemClassification.filler),
    ItemNames.BANELING_REGENERATIVE_ACID: ItemData(211 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 11, SC2Race.ZERG, parent_item="Baneling", origin={"hots"}, classification=ItemClassification.filler),
    ItemNames.MUTALISK_VICIOUS_GLAVE: ItemData(212 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 12, SC2Race.ZERG, parent_item="Mutalisk", origin={"hots"}),
    ItemNames.MUTALISK_RAPID_REGENERATION: ItemData(213 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 13, SC2Race.ZERG, parent_item="Mutalisk", origin={"hots"}),
    ItemNames.MUTALISK_SUNDERING_GLAVE: ItemData(214 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 14, SC2Race.ZERG, parent_item="Mutalisk", origin={"hots"}),
    ItemNames.SWARM_HOST_BURROW: ItemData(215 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 15, SC2Race.ZERG, parent_item="Swarm Host", origin={"hots"}, classification=ItemClassification.filler),
    ItemNames.SWARM_HOST_RAPID_INCUBATION: ItemData(216 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 16, SC2Race.ZERG, parent_item="Swarm Host", origin={"hots"}),
    ItemNames.SWARM_HOST_PRESSURIZED_GLANDS: ItemData(217 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 17, SC2Race.ZERG, parent_item="Swarm Host", origin={"hots"}, classification=ItemClassification.progression),
    ItemNames.ULTRALISK_BURROW_CHARGE: ItemData(218 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 18, SC2Race.ZERG, parent_item="Ultralisk", origin={"hots"}),
    ItemNames.ULTRALISK_TISSUE_ANIMATION: ItemData(219 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 19, SC2Race.ZERG, parent_item="Ultralisk", origin={"hots"}),
    ItemNames.ULTRALISK_MONARCH_BLADES: ItemData(220 + SC2HOTS_ITEM_ID_OFFSET, "Mutation", 20, SC2Race.ZERG, parent_item="Ultralisk", origin={"hots"}),
    
    ItemNames.ZERGLING_RAPTOR_STRAIN: ItemData(300 + SC2HOTS_ITEM_ID_OFFSET, "Strain", 0, SC2Race.ZERG, parent_item="Zergling", origin={"hots"}),
    ItemNames.ZERGLING_SWARMLING_STRAIN: ItemData(301 + SC2HOTS_ITEM_ID_OFFSET, "Strain", 1, SC2Race.ZERG, parent_item="Zergling", origin={"hots"}),
    ItemNames.ROACH_VILE_STRAIN: ItemData(302 + SC2HOTS_ITEM_ID_OFFSET, "Strain", 2, SC2Race.ZERG, parent_item="Roach", origin={"hots"}),
    ItemNames.ROACH_CORPSER_STRAIN: ItemData(303 + SC2HOTS_ITEM_ID_OFFSET, "Strain", 3, SC2Race.ZERG, parent_item="Roach", origin={"hots"}),
    ItemNames.HYDRALISK_IMPALER_STRAIN: ItemData(304 + SC2HOTS_ITEM_ID_OFFSET, "Strain", 4, SC2Race.ZERG, parent_item="Hydralisk", origin={"hots"}, classification=ItemClassification.progression),
    ItemNames.HYDRALISK_LURKER_STRAIN: ItemData(305 + SC2HOTS_ITEM_ID_OFFSET, "Strain", 5, SC2Race.ZERG, parent_item="Hydralisk", origin={"hots"}, classification=ItemClassification.progression),
    ItemNames.BANELING_SPLITTER_STRAIN: ItemData(306 + SC2HOTS_ITEM_ID_OFFSET, "Strain", 6, SC2Race.ZERG, parent_item="Baneling", origin={"hots"}),
    ItemNames.BANELING_HUNTER_STRAIN: ItemData(307 + SC2HOTS_ITEM_ID_OFFSET, "Strain", 7, SC2Race.ZERG, parent_item="Baneling", origin={"hots"}),
    ItemNames.MUTALISK_BROOD_LORD_STRAIN: ItemData(308 + SC2HOTS_ITEM_ID_OFFSET, "Strain", 8, SC2Race.ZERG, parent_item="Mutalisk", origin={"hots"}, classification=ItemClassification.progression),
    ItemNames.MUTALISK_VIPER_STRAIN: ItemData(309 + SC2HOTS_ITEM_ID_OFFSET, "Strain", 9, SC2Race.ZERG, parent_item="Mutalisk", origin={"hots"}, classification=ItemClassification.progression),
    ItemNames.SWARM_HOST_CARRION_STRAIN: ItemData(310 + SC2HOTS_ITEM_ID_OFFSET, "Strain", 10, SC2Race.ZERG, parent_item="Swarm Host", origin={"hots"}),
    ItemNames.SWARM_HOST_CREEPER_STRAIN: ItemData(311 + SC2HOTS_ITEM_ID_OFFSET, "Strain", 11, SC2Race.ZERG, parent_item="Swarm Host", origin={"hots"}, classification=ItemClassification.filler),
    ItemNames.ULTRALISK_NOXIOUS_STRAIN: ItemData(312 + SC2HOTS_ITEM_ID_OFFSET, "Strain", 12, SC2Race.ZERG, parent_item="Ultralisk", origin={"hots"}, classification=ItemClassification.filler),
    ItemNames.ULTRALISK_TORRASQUE_STRAIN: ItemData(313 + SC2HOTS_ITEM_ID_OFFSET, "Strain", 13, SC2Race.ZERG, parent_item="Ultralisk", origin={"hots"}),
    
    ItemNames.KERRIGAN_KINETIC_BLAST: ItemData(400 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 0, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.progression),
    ItemNames.KERRIGAN_HEROIC_FORTITUDE: ItemData(401 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 1, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.progression),
    ItemNames.KERRIGAN_LEAPING_STRIKE: ItemData(402 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 2, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.progression),
    ItemNames.KERRIGAN_CRUSHING_GRIP: ItemData(403 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 3, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.progression),
    ItemNames.KERRIGAN_CHAIN_REACTION: ItemData(404 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 4, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.progression),
    ItemNames.KERRIGAN_PSIONIC_SHIFT: ItemData(405 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 5, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.progression),
    ItemNames.KERRIGAN_ZERGLING_RECONSTITUTION: ItemData(406 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 6, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.filler),
    ItemNames.KERRIGAN_IMPROVED_OVERLORDS: ItemData(407 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 7, SC2Race.ZERG, origin={"hots"}),
    ItemNames.KERRIGAN_AUTOMATED_EXTRACTORS: ItemData(408 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 8, SC2Race.ZERG, origin={"hots"}),
    ItemNames.KERRIGAN_WILD_MUTATION: ItemData(409 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 9, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.progression),
    ItemNames.KERRIGAN_SPAWN_BANELINGS: ItemData(410 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 10, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.progression),
    ItemNames.KERRIGAN_MEND: ItemData(411 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 11, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.progression),
    ItemNames.KERRIGAN_TWIN_DRONES: ItemData(412 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 12, SC2Race.ZERG, origin={"hots"}),
    ItemNames.KERRIGAN_MALIGNANT_CREEP: ItemData(413 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 13, SC2Race.ZERG, origin={"hots"}),
    ItemNames.KERRIGAN_VESPENE_EFFICIENCY: ItemData(414 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 14, SC2Race.ZERG, origin={"hots"}),
    ItemNames.KERRIGAN_INFEST_BROODLINGS: ItemData(415 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 15, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.progression),
    ItemNames.KERRIGAN_FURY: ItemData(416 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 16, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.progression),
    ItemNames.KERRIGAN_ABILITY_EFFICIENCY: ItemData(417 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 17, SC2Race.ZERG, origin={"hots"}),
    ItemNames.KERRIGAN_APOCALYPSE: ItemData(418 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 18, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.progression),
    ItemNames.KERRIGAN_SPAWN_LEVIATHAN: ItemData(419 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 19, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.progression),
    ItemNames.KERRIGAN_DROP_PODS: ItemData(420 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 20, SC2Race.ZERG, origin={"hots"}, classification=ItemClassification.progression),
    # Handled separately from other abilities
    ItemNames.KERRIGAN_PRIMAL_FORM: ItemData(421 + SC2HOTS_ITEM_ID_OFFSET, "Ability", 0, SC2Race.ZERG, origin={"hots"}),
    
    ItemNames.KERRIGAN_LEVELS_10: ItemData(500 + SC2HOTS_ITEM_ID_OFFSET, "Level", 10, SC2Race.ZERG, origin={"hots"}, quantity=0),
    ItemNames.KERRIGAN_LEVELS_9: ItemData(501 + SC2HOTS_ITEM_ID_OFFSET, "Level", 9, SC2Race.ZERG, origin={"hots"}, quantity=0),
    ItemNames.KERRIGAN_LEVELS_8: ItemData(502 + SC2HOTS_ITEM_ID_OFFSET, "Level", 8, SC2Race.ZERG, origin={"hots"}, quantity=0),
    ItemNames.KERRIGAN_LEVELS_7: ItemData(503 + SC2HOTS_ITEM_ID_OFFSET, "Level", 7, SC2Race.ZERG, origin={"hots"}, quantity=0),
    ItemNames.KERRIGAN_LEVELS_6: ItemData(504 + SC2HOTS_ITEM_ID_OFFSET, "Level", 6, SC2Race.ZERG, origin={"hots"}, quantity=0),
    ItemNames.KERRIGAN_LEVELS_5: ItemData(505 + SC2HOTS_ITEM_ID_OFFSET, "Level", 5, SC2Race.ZERG, origin={"hots"}, quantity=0),
    ItemNames.KERRIGAN_LEVELS_4: ItemData(506 + SC2HOTS_ITEM_ID_OFFSET, "Level", 4, SC2Race.ZERG, origin={"hots"}, quantity=0, classification=ItemClassification.filler),
    ItemNames.KERRIGAN_LEVELS_3: ItemData(507 + SC2HOTS_ITEM_ID_OFFSET, "Level", 3, SC2Race.ZERG, origin={"hots"}, quantity=0, classification=ItemClassification.filler),
    ItemNames.KERRIGAN_LEVELS_2: ItemData(508 + SC2HOTS_ITEM_ID_OFFSET, "Level", 2, SC2Race.ZERG, origin={"hots"}, quantity=0, classification=ItemClassification.filler),
    ItemNames.KERRIGAN_LEVELS_1: ItemData(509 + SC2HOTS_ITEM_ID_OFFSET, "Level", 1, SC2Race.ZERG, origin={"hots"}, quantity=0, classification=ItemClassification.filler),
    ItemNames.KERRIGAN_LEVELS_14: ItemData(510 + SC2HOTS_ITEM_ID_OFFSET, "Level", 14, SC2Race.ZERG, origin={"hots"}, quantity=0),
    ItemNames.KERRIGAN_LEVELS_35: ItemData(511 + SC2HOTS_ITEM_ID_OFFSET, "Level", 35, SC2Race.ZERG, origin={"hots"}, quantity=0),
    ItemNames.KERRIGAN_LEVELS_70: ItemData(512 + SC2HOTS_ITEM_ID_OFFSET, "Level", 70, SC2Race.ZERG, origin={"hots"}, quantity=0),
}

def get_item_table(multiworld: MultiWorld, player: int):
    return item_table

basic_units = {
    SC2Race.TERRAN: {
        ItemNames.MARINE,
        ItemNames.MARAUDER,
        ItemNames.GOLIATH,
        ItemNames.HELLION,
        ItemNames.VULTURE,
    },
    SC2Race.ZERG: {
        ItemNames.ZERGLING,
        ItemNames.SWARM_QUEEN,
        ItemNames.ROACH,
        ItemNames.HYDRALISK,
    },
    # TODO Placeholder for Prophecy
    SC2Race.PROTOSS: {
        ItemNames.ZEALOT,
        ItemNames.STALKER,
    }
}

advanced_basic_units = {
    SC2Race.TERRAN: basic_units[SC2Race.TERRAN].union({
        ItemNames.REAPER,
        ItemNames.DIAMONDBACK,
        ItemNames.VIKING,
    }),
    SC2Race.ZERG: basic_units[SC2Race.ZERG].union({
        ItemNames.INFESTOR,
        ItemNames.ABERRATION,
    }),
    SC2Race.PROTOSS: basic_units[SC2Race.PROTOSS].union({
        ItemNames.DARK_TEMPLAR,
    })
}


def get_basic_units(multiworld: MultiWorld, player: int, race: SC2Race) -> typing.Set[str]:
    if get_option_value(multiworld, player, 'required_tactics') != RequiredTactics.option_standard:
        return advanced_basic_units[race]
    else:
        return basic_units[race]


item_name_group_names = {
    # WoL
    "Armory 1", "Armory 2", "Armory 3",
    "Armory 4", "Laboratory", "Progressive Upgrade",
    # HotS
    "Ability", "Strain", "Mutation"
}
item_name_groups: typing.Dict[str, typing.List[str]] = {}
for item, data in get_full_item_list().items():
    item_name_groups.setdefault(data.type, []).append(item)
    if data.type in item_name_group_names and '(' in item:
        short_name = item[:item.find(' (')]
        item_name_groups[short_name] = [item]
item_name_groups["Missions"] = ["Beat " + mission.mission_name for mission in SC2Mission]
item_name_groups["WoL Missions"] = ["Beat " + mission.mission_name for mission in campaign_mission_table[SC2Campaign.WOL]] + \
                                   ["Beat " + mission.mission_name for mission in campaign_mission_table[SC2Campaign.PROPHECY]]


# Items that can be placed before resources if not already in
# General upgrades and Mercs
# TODO needs zerg items
second_pass_placeable_items: typing.Tuple[str, ...] = (
    # Buildings without upgrades
    ItemNames.SENSOR_TOWER,
    ItemNames.HIVE_MIND_EMULATOR,
    ItemNames.PSI_DISRUPTER,
    ItemNames.PERDITION_TURRET,
    # General upgrades without any dependencies
    ItemNames.SCV_ADVANCED_CONSTRUCTION,
    ItemNames.SCV_DUAL_FUSION_WELDERS,
    ItemNames.BUILDING_FIRE_SUPPRESSION_SYSTEM,
    ItemNames.BUILDING_ORBITAL_COMMAND,
    ItemNames.ULTRA_CAPACITORS,
    ItemNames.VANADIUM_PLATING,
    ItemNames.ORBITAL_DEPOTS,
    ItemNames.MICRO_FILTERING,
    ItemNames.AUTOMATED_REFINERY,
    ItemNames.COMMAND_CENTER_REACTOR,
    ItemNames.TECH_REACTOR,
    ItemNames.PLANETARY_FORTRESS,
    ItemNames.CELLULAR_REACTOR,
    ItemNames.PROGRESSIVE_REGENERATIVE_BIO_STEEL,  # Place only L1
    # Mercenaries
    ItemNames.WAR_PIGS,
    ItemNames.DEVIL_DOGS,
    ItemNames.HAMMER_SECURITIES,
    ItemNames.SPARTAN_COMPANY,
    ItemNames.SIEGE_BREAKERS,
    ItemNames.HELS_ANGEL,
    ItemNames.DUSK_WINGS,
    ItemNames.JACKSONS_REVENGE,
)


filler_items: typing.Tuple[str, ...] = (
    ItemNames.STARTING_MINERALS,
    ItemNames.STARTING_VESPENE,
)

# Defense rating table
# Commented defense ratings are handled in LogicMixin
defense_ratings = {
    ItemNames.SIEGE_TANK: 5,
    # "Maelstrom Rounds": 2,
    ItemNames.PLANETARY_FORTRESS: 3,
    # Bunker w/ Marine/Marauder: 3,
    ItemNames.PERDITION_TURRET: 2,
    ItemNames.MISSILE_TURRET: 2,
    ItemNames.VULTURE: 2,
    ItemNames.LIBERATOR: 2,
    ItemNames.WIDOW_MINE: 2,
    # "Concealment (Widow Mine)": 1
}
zerg_defense_ratings = {
    ItemNames.PERDITION_TURRET: 2,
    # Bunker w/ Firebat: 2,
    ItemNames.HIVE_MIND_EMULATOR: 3,
    ItemNames.PSI_DISRUPTER: 3,
}

spider_mine_sources = {
    ItemNames.VULTURE,
    ItemNames.REAPER_SPIDER_MINES,
    ItemNames.SIEGE_TANK_SPIDER_MINES,
    ItemNames.RAVEN_SPIDER_MINES,
}

progressive_if_nco = {
    ItemNames.MARINE_PROGRESSIVE_STIMPACK,
    ItemNames.FIREBAT_PROGRESSIVE_STIMPACK,
    ItemNames.BANSHEE_PROGRESSIVE_CROSS_SPECTRUM_DAMPENERS,
    ItemNames.PROGRESSIVE_REGENERATIVE_BIO_STEEL,
}

kerrigan_actives: typing.List[typing.Set[str]] = [
    {ItemNames.KERRIGAN_KINETIC_BLAST, ItemNames.KERRIGAN_LEAPING_STRIKE},
    {ItemNames.KERRIGAN_CRUSHING_GRIP, ItemNames.KERRIGAN_PSIONIC_SHIFT},
    set(),
    {ItemNames.KERRIGAN_WILD_MUTATION, ItemNames.KERRIGAN_SPAWN_BANELINGS, ItemNames.KERRIGAN_MEND},
    set(),
    set(),
    {ItemNames.KERRIGAN_APOCALYPSE, ItemNames.KERRIGAN_SPAWN_LEVIATHAN, ItemNames.KERRIGAN_DROP_PODS},
]

kerrigan_passives: typing.List[typing.Set[str]] = [
    {ItemNames.KERRIGAN_HEROIC_FORTITUDE},
    {ItemNames.KERRIGAN_CHAIN_REACTION},
    {ItemNames.KERRIGAN_ZERGLING_RECONSTITUTION, ItemNames.KERRIGAN_IMPROVED_OVERLORDS, ItemNames.KERRIGAN_AUTOMATED_EXTRACTORS},
    set(),
    {ItemNames.KERRIGAN_TWIN_DRONES, ItemNames.KERRIGAN_MALIGNANT_CREEP, ItemNames.KERRIGAN_VESPENE_EFFICIENCY},
    {ItemNames.KERRIGAN_INFEST_BROODLINGS, ItemNames.KERRIGAN_FURY, ItemNames.KERRIGAN_ABILITY_EFFICIENCY},
    set(),
]

kerrigan_only_passives = {
    ItemNames.KERRIGAN_HEROIC_FORTITUDE, ItemNames.KERRIGAN_CHAIN_REACTION,
    ItemNames.KERRIGAN_INFEST_BROODLINGS, ItemNames.KERRIGAN_FURY, ItemNames.KERRIGAN_ABILITY_EFFICIENCY,
}

# 'number' values of upgrades for upgrade bundle items
upgrade_numbers = [
    # Terran
    {0, 4, 8}, # Weapon
    {2, 6, 10}, # Armor
    {0, 2}, # Infantry
    {4, 6}, # Vehicle
    {8, 10}, # Starship
    {0, 2, 4, 6, 8, 10}, # All
    # Zerg
    {0, 2, 6}, # Weapon
    {4, 8}, # Armor
    {0, 2, 4}, # Ground
    {6, 8}, # Flyer
    {0, 2, 4, 6, 8}, # All
]
# 'upgrade_numbers' indices for all upgrades
upgrade_numbers_all = {
    SC2Race.TERRAN: 5,
    SC2Race.ZERG: 10,
}

# Names of upgrades to be included for different options
upgrade_included_names = [
    { # Individual Items
        ItemNames.PROGRESSIVE_TERRAN_INFANTRY_WEAPON,
        ItemNames.PROGRESSIVE_TERRAN_INFANTRY_ARMOR,
        ItemNames.PROGRESSIVE_TERRAN_VEHICLE_WEAPON,
        ItemNames.PROGRESSIVE_TERRAN_VEHICLE_ARMOR,
        ItemNames.PROGRESSIVE_TERRAN_SHIP_WEAPON,
        ItemNames.PROGRESSIVE_TERRAN_SHIP_ARMOR,
        ItemNames.PROGRESSIVE_ZERG_MELEE_ATTACK,
        ItemNames.PROGRESSIVE_ZERG_MISSILE_ATTACK,
        ItemNames.PROGRESSIVE_ZERG_GROUND_CARAPACE,
        ItemNames.PROGRESSIVE_ZERG_FLYER_ATTACK,
        ItemNames.PROGRESSIVE_ZERG_FLYER_CARAPACE,
    },
    { # Bundle Weapon And Armor
        ItemNames.PROGRESSIVE_TERRAN_WEAPON_UPGRADE,
        ItemNames.PROGRESSIVE_TERRAN_ARMOR_UPGRADE,
        ItemNames.PROGRESSIVE_ZERG_WEAPON_UPGRADE,
        ItemNames.PROGRESSIVE_ZERG_ARMOR_UPGRADE,
    },
    { # Bundle Unit Class
        ItemNames.PROGRESSIVE_TERRAN_INFANTRY_UPGRADE,
        ItemNames.PROGRESSIVE_TERRAN_VEHICLE_UPGRADE,
        ItemNames.PROGRESSIVE_TERRAN_SHIP_UPGRADE,
        ItemNames.PROGRESSIVE_ZERG_GROUND_UPGRADE,
        ItemNames.PROGRESSIVE_ZERG_FLYER_UPGRADE,
    },
    { # Bundle All
        ItemNames.PROGRESSIVE_TERRAN_WEAPON_ARMOR_UPGRADE,
        ItemNames.PROGRESSIVE_ZERG_WEAPON_ARMOR_UPGRADE,
    }
]

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in get_full_item_list().items() if
                                            data.code}

# Map type to expected int
type_flaggroups: typing.Dict[SC2Race, typing.Dict[str, int]] = {
    SC2Race.ANY: {
        "Minerals": 0,
        "Vespene": 1,
        "Supply": 2,
        "Goal": 3,
        "Nothing Group": 4,
    },
    SC2Race.TERRAN: {
        "Unit": 0,
        "Upgrade": 1,  # Weapon / Armor upgrades
        "Armory 1": 2,  # Unit upgrades
        "Armory 2": 3,  # Unit upgrades
        "Building": 4,
        "Mercenary": 5,
        "Laboratory": 6,
        "Armory 3": 7,  # Unit upgrades
        "Armory 4": 8,  # Unit upgrades
        "Progressive Upgrade": 9,  # Unit upgrades that exist multiple times (Stimpack / Super Stimpack)
    },
    SC2Race.ZERG: {
        "Unit": 0,
        "Upgrade": 1,
        "Mutation": 2,
        "Strain": 3,
        "Ability": 4,
        "Level": 5,
    },
    SC2Race.PROTOSS: {
        "Unit": 0,
    }
}
