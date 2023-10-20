"""
A complete collection of Starcraft 2 item names as strings.
Users of this data may make some assumptions about the structure of a name:
* The upgrade for a unit will end with the unit's name in parentheses
* Weapon / armor upgrades may may be grouped by a common prefix specified within this file
"""

# Terran Units
MARINE         = "Marine"
MEDIC          = "Medic"
FIREBAT        = "Firebat"
MARAUDER       = "Marauder"
REAPER         = "Reaper"
HELLION        = "Hellion"
VULTURE        = "Vulture"
GOLIATH        = "Goliath"
DIAMONDBACK    = "Diamondback"
SIEGE_TANK     = "Siege Tank"
MEDIVAC        = "Medivac"
WRAITH         = "Wraith"
VIKING         = "Viking"
BANSHEE        = "Banshee"
BATTLECRUISER  = "Battlecruiser"
GHOST          = "Ghost"
SPECTRE        = "Spectre"
THOR           = "Thor"
RAVEN          = "Raven"
SCIENCE_VESSEL = "Science Vessel"
PREDATOR       = "Predator"
HERCULES       = "Hercules"
# Extended units
LIBERATOR      = "Liberator"
VALKYRIE       = "Valkyrie"
WIDOW_MINE     = "Widow Mine"
CYCLONE        = "Cyclone"

# Terran Buildings
BUNKER                              = "Bunker"
MISSILE_TURRET                      = "Missile Turret"
SENSOR_TOWER                        = "Sensor Tower"
PLANETARY_FORTRESS                  = "Planetary Fortress"
PERDITION_TURRET                    = "Perdition Turret"
HIVE_MIND_EMULATOR                  = "Hive Mind Emulator"
PSI_DISRUPTER                       = "Psi Disrupter"

# Terran Weapon / Armor Upgrades
TERRAN_UPGRADE_PREFIX = "Progressive Terran"
TERRAN_INFANTRY_UPGRADE_PREFIX = f"{TERRAN_UPGRADE_PREFIX} Infantry"
TERRAN_VEHICLE_UPGRADE_PREFIX = f"{TERRAN_UPGRADE_PREFIX} Vehicle"
TERRAN_SHIP_UPGRADE_PREFIX = f"{TERRAN_UPGRADE_PREFIX} Ship"

PROGRESSIVE_TERRAN_INFANTRY_WEAPON      = f"{TERRAN_INFANTRY_UPGRADE_PREFIX} Weapon"
PROGRESSIVE_TERRAN_INFANTRY_ARMOR       = f"{TERRAN_INFANTRY_UPGRADE_PREFIX} Armor"
PROGRESSIVE_TERRAN_VEHICLE_WEAPON       = f"{TERRAN_VEHICLE_UPGRADE_PREFIX} Weapon"
PROGRESSIVE_TERRAN_VEHICLE_ARMOR        = f"{TERRAN_VEHICLE_UPGRADE_PREFIX} Armor"
PROGRESSIVE_TERRAN_SHIP_WEAPON          = f"{TERRAN_SHIP_UPGRADE_PREFIX} Weapon"
PROGRESSIVE_TERRAN_SHIP_ARMOR           = f"{TERRAN_SHIP_UPGRADE_PREFIX} Armor"
PROGRESSIVE_TERRAN_WEAPON_UPGRADE       = f"{TERRAN_UPGRADE_PREFIX} Weapon Upgrade"
PROGRESSIVE_TERRAN_ARMOR_UPGRADE        = f"{TERRAN_UPGRADE_PREFIX} Armor Upgrade"
PROGRESSIVE_TERRAN_INFANTRY_UPGRADE     = f"{TERRAN_INFANTRY_UPGRADE_PREFIX} Upgrade"
PROGRESSIVE_TERRAN_VEHICLE_UPGRADE      = f"{TERRAN_VEHICLE_UPGRADE_PREFIX} Upgrade"
PROGRESSIVE_TERRAN_SHIP_UPGRADE         = f"{TERRAN_SHIP_UPGRADE_PREFIX} Upgrade"
PROGRESSIVE_TERRAN_WEAPON_ARMOR_UPGRADE = f"{TERRAN_UPGRADE_PREFIX} Weapon/Armor Upgrade"

# Mercenaries
WAR_PIGS          = "War Pigs"
DEVIL_DOGS        = "Devil Dogs"
HAMMER_SECURITIES = "Hammer Securities"
SPARTAN_COMPANY   = "Spartan Company"
SIEGE_BREAKERS    = "Siege Breakers"
HELS_ANGELS       = "Hel's Angels"
DUSK_WINGS        = "Dusk Wings"
JACKSONS_REVENGE  = "Jackson's Revenge"
SKIBIS_ANGELS     = "Skibi's Angels"
DEATH_HEADS       = "Death Heads"
WINGED_NIGHTMARES = "Winged Nightmares"
RAID_LIBERATORS   = "Raid Liberators"
BRYNHILDS         = "Brynhilds"
BLACKHAMMER       = "Blackhammer"

# Lab / Global
ULTRA_CAPACITORS                    = "Ultra-Capacitors"
VANADIUM_PLATING                    = "Vanadium Plating"
ORBITAL_DEPOTS                      = "Orbital Depots"
MICRO_FILTERING                     = "Micro-Filtering"
AUTOMATED_REFINERY                  = "Automated Refinery"
COMMAND_CENTER_REACTOR              = "Command Center Reactor"
TECH_REACTOR                        = "Tech Reactor"
ORBITAL_STRIKE                      = "Orbital Strike"
CELLULAR_REACTOR                    = "Cellular Reactor"
PROGRESSIVE_REGENERATIVE_BIO_STEEL  = "Progressive Regenerative Bio-Steel"
PROGRESSIVE_FIRE_SUPPRESSION_SYSTEM = "Progressive Fire-Suppression System"
PROGRESSIVE_ORBITAL_COMMAND         = "Progressive Orbital Command"
STRUCTURE_ARMOR                     = "Structure Armor"
HI_SEC_AUTO_TRACKING                = "Hi-Sec Auto Tracking"
ADVANCED_OPTICS                     = "Advanced Optics"
ROGUE_FORCES                        = "Rogue Forces"

# Terran Unit Upgrades
BANSHEE_HYPERFLIGHT_ROTORS                         = "Hyperflight Rotors (Banshee)"
BANSHEE_INTERNAL_TECH_MODULE                       = "Internal Tech Module (Banshee)"
BANSHEE_LASER_TARGETING_SYSTEM                     = "Laser Targeting System (Banshee)"
BANSHEE_PROGRESSIVE_CROSS_SPECTRUM_DAMPENERS       = "Progressive Cross-Spectrum Dampeners (Banshee)"
BANSHEE_SHOCKWAVE_MISSILE_BATTERY                  = "Shockwave Missile Battery (Banshee)"
BANSHEE_SHAPED_HULL                                = "Shaped Hull (Banshee)"
BANSHEE_ADVANCED_TARGETING_OPTICS                  = "Advanced Targeting Optics (Banshee)"
BANSHEE_DISTORTION_BLASTERS                        = "Distortion Blasters (Banshee)"
BANSHEE_ROCKET_BARRAGE                             = "Rocket Barrage (Banshee)"
BATTLECRUISER_ATX_LASER_BATTERY                    = "ATX Laser Battery (Battlecruiser)"
BATTLECRUISER_CLOAK                                = "Cloak (Battlecruiser)"
BATTLECRUISER_PROGRESSIVE_DEFENSIVE_MATRIX         = "Progressive Defensive Matrix (Battlecruiser)"
BATTLECRUISER_INTERNAL_TECH_MODULE                 = "Internal Tech Module (Battlecruiser)"
BATTLECRUISER_MISSILE_PODS                         = "Missile Pods (Battlecruiser)"
BATTLECRUISER_OPTIMIZED_LOGISTICS                  = "Optimized Logistics (Battlecruiser)"
BATTLECRUISER_TACTICAL_JUMP                        = "Tactical Jump (Battlecruiser)"
BUNKER_NEOSTEEL_BUNKER                             = "Neosteel Bunker (Bunker)"
BUNKER_PROJECTILE_ACCELERATOR                      = "Projectile Accelerator (Bunker)"
BUNKER_SHRIKE_TURRET                               = "Shrike Turret (Bunker)"
BUNKER_FORTIFIED_BUNKER                            = "Fortified Bunker (Bunker)"
CYCLONE_MAG_FIELD_ACCELERATORS                     = "Mag-Field Accelerators (Cyclone)"
CYCLONE_MAG_FIELD_LAUNCHERS                        = "Mag-Field Launchers (Cyclone)"
CYCLONE_RAPID_FIRE_LAUNCHERS                       = "Rapid Fire Launchers (Cyclone)"
CYCLONE_TARGETING_OPTICS                           = "Targeting Optics (Cyclone)"
CYCLONE_RESOURCE_EFFICIENCY                        = "Resource Efficiency (Cyclone)"
CYCLONE_INTERNAL_TECH_MODULE                       = "Internal Tech Module (Cyclone)"
DIAMONDBACK_BURST_CAPACITORS                       = "Burst Capacitors (Diamondback)"
DIAMONDBACK_HYPERFLUXOR                            = "Hyperfluxor (Diamondback)"
DIAMONDBACK_RESOURCE_EFFICIENCY                    = "Resource Efficiency (Diamondback)"
DIAMONDBACK_SHAPED_HULL                            = "Shaped Hull (Diamondback)"
DIAMONDBACK_TRI_LITHIUM_POWER_CELL                 = "Tri-Lithium Power Cell (Diamondback)"
FIREBAT_INCINERATOR_GAUNTLETS                      = "Incinerator Gauntlets (Firebat)"
FIREBAT_JUGGERNAUT_PLATING                         = "Juggernaut Plating (Firebat)"
FIREBAT_RESOURCE_EFFICIENCY                        = "Resource Efficiency (Firebat)"
FIREBAT_PROGRESSIVE_STIMPACK                       = "Progressive Stimpack (Firebat)"
FIREBAT_INFERNAL_PRE_IGNITER                       = "Infernal Pre-Igniter (Firebat)"
FIREBAT_KINETIC_FOAM                               = "Kinetic Foam (Firebat)"
FIREBAT_NANO_PROJECTORS                            = "Nano Projectors (Firebat)"
GHOST_CRIUS_SUIT                                   = "Crius Suit (Ghost)"
GHOST_EMP_ROUNDS                                   = "EMP Rounds (Ghost)"
GHOST_LOCKDOWN                                     = "Lockdown (Ghost)"
GHOST_OCULAR_IMPLANTS                              = "Ocular Implants (Ghost)"
GHOST_RESOURCE_EFFICIENCY                          = "Resource Efficiency (Ghost)"
GOLIATH_ARES_CLASS_TARGETING_SYSTEM                = "Ares-Class Targeting System (Goliath)"
GOLIATH_JUMP_JETS                                  = "Jump Jets (Goliath)"
GOLIATH_MULTI_LOCK_WEAPONS_SYSTEM                  = "Multi-Lock Weapons System (Goliath)"
GOLIATH_OPTIMIZED_LOGISTICS                        = "Optimized Logistics (Goliath)"
GOLIATH_SHAPED_HULL                                = "Shaped Hull (Goliath)"
GOLIATH_RESOURCE_EFFICIENCY                        = "Resource Efficiency (Goliath)"
GOLIATH_INTERNAL_TECH_MODULE                       = "Internal Tech Module (Goliath)"
HELLION_HELLBAT_ASPECT                             = "Hellbat Aspect (Hellion)"
HELLION_JUMP_JETS                                  = "Jump Jets (Hellion)"
HELLION_OPTIMIZED_LOGISTICS                        = "Optimized Logistics (Hellion)"
HELLION_PROGRESSIVE_STIMPACK                       = "Progressive Stimpack (Hellion)"
HELLION_SMART_SERVOS                               = "Smart Servos (Hellion)"
HELLION_THERMITE_FILAMENTS                         = "Thermite Filaments (Hellion)"
HELLION_TWIN_LINKED_FLAMETHROWER                   = "Twin-Linked Flamethrower (Hellion)"
HELLION_INFERNAL_PLATING                           = "Infernal Plating (Hellion)"
HERCULES_INTERNAL_FUSION_MODULE                    = "Internal Fusion Module (Hercules)"
HERCULES_TACTICAL_JUMP                             = "Tactical Jump (Hercules)"
LIBERATOR_ADVANCED_BALLISTICS                      = "Advanced Ballistics (Liberator)"
LIBERATOR_CLOAK                                    = "Cloak (Liberator)"
LIBERATOR_LASER_TARGETING_SYSTEM                   = "Laser Targeting System (Liberator)"
LIBERATOR_OPTIMIZED_LOGISTICS                      = "Optimized Logistics (Liberator)"
LIBERATOR_RAID_ARTILLERY                           = "Raid Artillery (Liberator)"
LIBERATOR_SMART_SERVOS                             = "Smart Servos (Liberator)"
LIBERATOR_RESOURCE_EFFICIENCY                      = "Resource Efficiency (Liberator)"
MARAUDER_CONCUSSIVE_SHELLS                         = "Concussive Shells (Marauder)"
MARAUDER_INTERNAL_TECH_MODULE                      = "Internal Tech Module (Marauder)"
MARAUDER_KINETIC_FOAM                              = "Kinetic Foam (Marauder)"
MARAUDER_LASER_TARGETING_SYSTEM                    = "Laser Targeting System (Marauder)"
MARAUDER_MAGRAIL_MUNITIONS                         = "Magrail Munitions (Marauder)"
MARAUDER_PROGRESSIVE_STIMPACK                      = "Progressive Stimpack (Marauder)"
MARAUDER_JUGGERNAUT_PLATING                        = "Juggernaut Plating (Marauder)"
MARINE_COMBAT_SHIELD                               = "Combat Shield (Marine)"
MARINE_LASER_TARGETING_SYSTEM                      = "Laser Targeting System (Marine)"
MARINE_MAGRAIL_MUNITIONS                           = "Magrail Munitions (Marine)"
MARINE_OPTIMIZED_LOGISTICS                         = "Optimized Logistics (Marine)"
MARINE_PROGRESSIVE_STIMPACK                        = "Progressive Stimpack (Marine)"
MEDIC_ADVANCED_MEDIC_FACILITIES                    = "Advanced Medic Facilities (Medic)"
MEDIC_OPTICAL_FLARE                                = "Optical Flare (Medic)"
MEDIC_RESOURCE_EFFICIENCY                          = "Resource Efficiency (Medic)"
MEDIC_RESTORATION                                  = "Restoration (Medic)"
MEDIC_STABILIZER_MEDPACKS                          = "Stabilizer Medpacks (Medic)"
MEDIC_ADAPTIVE_MEDPACKS                            = "Adaptive Medpacks (Medic)"
MEDIC_NANO_PROJECTOR                               = "Nano Projector (Medic)"
MEDIVAC_ADVANCED_HEALING_AI                        = "Advanced Healing AI (Medivac)"
MEDIVAC_AFTERBURNERS                               = "Afterburners (Medivac)"
MEDIVAC_EXPANDED_HULL                              = "Expanded Hull (Medivac)"
MEDIVAC_RAPID_DEPLOYMENT_TUBE                      = "Rapid Deployment Tube (Medivac)"
MEDIVAC_SCATTER_VEIL                               = "Scatter Veil (Medivac)"
MEDIVAC_ADVANCED_CLOAKING_FIELD                    = "Advanced Cloaking Field (Medivac)"
MISSILE_TURRET_HELLSTORM_BATTERIES                 = "Hellstorm Batteries (Missile Turret)"
MISSILE_TURRET_TITANIUM_HOUSING                    = "Titanium Housing (Missile Turret)"
PLANETARY_FORTRESS_PROGRESSIVE_AUGMENTED_THRUSTERS = "Progressive Augmented Thrusters (Planetary Fortress)"
PLANETARY_FORTRESS_ADVANCED_TARGETING              = "Advanced Targeting (Planetary Fortress)"
PREDATOR_RESOURCE_EFFICIENCY                       = "Resource Efficiency (Predator)"
PREDATOR_CLOAK                                     = "Cloak (Predator)"
PREDATOR_CHARGE                                    = "Charge (Predator)"
RAVEN_ANTI_ARMOR_MISSILE                           = "Anti-Armor Missile (Raven)"
RAVEN_BIO_MECHANICAL_REPAIR_DRONE                  = "Bio Mechanical Repair Drone (Raven)"
RAVEN_HUNTER_SEEKER_WEAPON                         = "Hunter-Seeker Weapon (Raven)"
RAVEN_INTERFERENCE_MATRIX                          = "Interference Matrix (Raven)"
RAVEN_INTERNAL_TECH_MODULE                         = "Internal Tech Module (Raven)"
RAVEN_RAILGUN_TURRET                               = "Railgun Turret (Raven)"
RAVEN_SPIDER_MINES                                 = "Spider Mines (Raven)"
RAVEN_RESOURCE_EFFICIENCY                          = "Resource Efficiency (Raven)"
RAVEN_DURABLE_MATERIALS                            = "Durable Materials (Raven)"
REAPER_ADVANCED_CLOAKING_FIELD                     = "Advanced Cloaking Field (Reaper)"
REAPER_COMBAT_DRUGS                                = "Combat Drugs (Reaper)"
REAPER_G4_CLUSTERBOMB                              = "G-4 Clusterbomb (Reaper)"
REAPER_LASER_TARGETING_SYSTEM                      = "Laser Targeting System (Reaper)"
REAPER_PROGRESSIVE_STIMPACK                        = "Progressive Stimpack (Reaper)"
REAPER_SPIDER_MINES                                = "Spider Mines (Reaper)"
REAPER_U238_ROUNDS                                 = "U-238 Rounds (Reaper)"
REAPER_JET_PACK_OVERDRIVE                          = "Jet Pack Overdrive (Reaper)"
SCIENCE_VESSEL_DEFENSIVE_MATRIX                    = "Defensive Matrix (Science Vessel)"
SCIENCE_VESSEL_EMP_SHOCKWAVE                       = "EMP Shockwave (Science Vessel)"
SCIENCE_VESSEL_IMPROVED_NANO_REPAIR                = "Improved Nano-Repair (Science Vessel)"
SCIENCE_VESSEL_ADVANCED_AI_SYSTEMS                 = "Advanced AI Systems (Science Vessel)"
SCV_ADVANCED_CONSTRUCTION                          = "Advanced Construction (SCV)"
SCV_DUAL_FUSION_WELDERS                            = "Dual-Fusion Welders (SCV)"
SCV_HOSTILE_ENVIRONMENT_ADAPTATION                 = "Hostile Environment Adaptation (SCV)"
SIEGE_TANK_ADVANCED_SIEGE_TECH                     = "Advanced Siege Tech (Siege Tank)"
SIEGE_TANK_GRADUATING_RANGE                        = "Graduating Range (Siege Tank)"
SIEGE_TANK_INTERNAL_TECH_MODULE                    = "Internal Tech Module (Siege Tank)"
SIEGE_TANK_JUMP_JETS                               = "Jump Jets (Siege Tank)"
SIEGE_TANK_LASER_TARGETING_SYSTEM                  = "Laser Targeting System (Siege Tank)"
SIEGE_TANK_MAELSTROM_ROUNDS                        = "Maelstrom Rounds (Siege Tank)"
SIEGE_TANK_SHAPED_BLAST                            = "Shaped Blast (Siege Tank)"
SIEGE_TANK_SMART_SERVOS                            = "Smart Servos (Siege Tank)"
SIEGE_TANK_SPIDER_MINES                            = "Spider Mines (Siege Tank)"
SIEGE_TANK_SHAPED_HULL                             = "Shaped Hull (Siege Tank)"
SIEGE_TANK_RESOURCE_EFFICIENCY                     = "Resource Efficiency (Siege Tank)"
SPECTRE_IMPALER_ROUNDS                             = "Impaler Rounds (Spectre)"
SPECTRE_NYX_CLASS_CLOAKING_MODULE                  = "Nyx-Class Cloaking Module (Spectre)"
SPECTRE_PSIONIC_LASH                               = "Psionic Lash (Spectre)"
SPECTRE_RESOURCE_EFFICIENCY                        = "Resource Efficiency (Spectre)"
SPIDER_MINE_CERBERUS_MINE                          = "Cerberus Mine (Spider Mine)"
SPIDER_MINE_HIGH_EXPLOSIVE_MUNITION                = "High Explosive Munition (Spider Mine)"
THOR_330MM_BARRAGE_CANNON                          = "330mm Barrage Cannon (Thor)"
THOR_PROGRESSIVE_IMMORTALITY_PROTOCOL              = "Progressive Immortality Protocol (Thor)"
THOR_PROGRESSIVE_HIGH_IMPACT_PAYLOAD               = "Progressive High Impact Payload (Thor)"
THOR_BUTTON_WITH_A_SKULL_ON_IT                     = "Button With a Skull on It (Thor)"
THOR_LASER_TARGETING_SYSTEM                        = "Laser Targeting System (Thor)"
THOR_LARGE_SCALE_FIELD_CONSTRUCTION                = "Large Scale Field Construction (Thor)"
VALKYRIE_AFTERBURNERS                              = "Afterburners (Valkyrie)"
VALKYRIE_BURST_LASERS                              = "Burst Lasers (Valkyrie)"
VALKYRIE_ENHANCED_CLUSTER_LAUNCHERS                = "Enhanced Cluster Launchers (Valkyrie)"
VALKYRIE_SHAPED_HULL                               = "Shaped Hull (Valkyrie)"
VIKING_ANTI_MECHANICAL_MUNITION                    = "Anti-Mechanical Munition (Viking)"
VIKING_PHOBOS_CLASS_WEAPONS_SYSTEM                 = "Phobos-Class Weapons System (Viking)"
VIKING_RIPWAVE_MISSILES                            = "Ripwave Missiles (Viking)"
VIKING_SMART_SERVOS                                = "Smart Servos (Viking)"
VIKING_SHREDDER_ROUNDS                             = "Shredder Rounds (Viking)"
VIKING_WILD_MISSILES                               = "W.I.L.D. Missiles (Viking)"
VULTURE_AUTO_LAUNCHERS                             = "Auto Launchers (Vulture)"
VULTURE_ION_THRUSTERS                              = "Ion Thrusters (Vulture)"
VULTURE_PROGRESSIVE_REPLENISHABLE_MAGAZINE         = "Progressive Replenishable Magazine (Vulture)"
VULTURE_AUTO_REPAIR                                = "Auto-Repair (Vulture)"
WIDOW_MINE_BLACK_MARKET_LAUNCHERS                  = "Black Market Launchers (Widow Mine)"
WIDOW_MINE_CONCEALMENT                             = "Concealment (Widow Mine)"
WIDOW_MINE_DRILLING_CLAWS                          = "Drilling Claws (Widow Mine)"
WIDOW_MINE_EXECUTIONER_MISSILES                    = "Executioner Missiles (Widow Mine)"
WRAITH_ADVANCED_LASER_TECHNOLOGY                   = "Advanced Laser Technology (Wraith)"
WRAITH_DISPLACEMENT_FIELD                          = "Displacement Field (Wraith)"
WRAITH_PROGRESSIVE_TOMAHAWK_POWER_CELLS            = "Progressive Tomahawk Power Cells (Wraith)"
WRAITH_TRIGGER_OVERRIDE                            = "Trigger Override (Wraith)"
WRAITH_INTERNAL_TECH_MODULE                        = "Internal Tech Module (Wraith)"
WRAITH_RESOURCE_EFFICIENCY                         = "Resource Efficiency (Wraith)"

# Protoss Units
ZEALOT       = "Zealot"
STALKER      = "Stalker"
HIGH_TEMPLAR = "High Templar"
DARK_TEMPLAR = "Dark Templar"
IMMORTAL     = "Immortal"
COLOSSUS     = "Colossus"
PHOENIX      = "Phoenix"
VOID_RAY     = "Void Ray"
CARRIER      = "Carrier"

# Filler items
STARTING_MINERALS = "+15 Starting Minerals"
STARTING_VESPENE  = "+15 Starting Vespene"
STARTING_SUPPLY   = "+2 Starting Supply"
NOTHING           = "Nothing"


# Zerg Units
ZERGLING      = "Zergling"
SWARM_QUEEN   = "Swarm Queen"
ROACH         = "Roach"
HYDRALISK     = "Hydralisk"
BANELING      = "Baneling"
ABERRATION    = "Aberration"
MUTALISK      = "Mutalisk"
SWARM_HOST    = "Swarm Host"
INFESTOR      = "Infestor"
ULTRALISK     = "Ultralisk"
SPORE_CRAWLER = "Spore Crawler"
SPINE_CRAWLER = "Spine Crawler"

# Zerg Weapon / Armor Upgrades
ZERG_UPGRADE_PREFIX = "Progressive Zerg"
ZERG_FLYER_UPGRADE_PREFIX = f"{ZERG_UPGRADE_PREFIX} Flyer"

PROGRESSIVE_ZERG_MELEE_ATTACK         = f"{ZERG_UPGRADE_PREFIX} Melee Attack"
PROGRESSIVE_ZERG_MISSILE_ATTACK       = f"{ZERG_UPGRADE_PREFIX} Missile Attack"
PROGRESSIVE_ZERG_GROUND_CARAPACE      = f"{ZERG_UPGRADE_PREFIX} Ground Carapace"
PROGRESSIVE_ZERG_FLYER_ATTACK         = f"{ZERG_FLYER_UPGRADE_PREFIX} Attack"
PROGRESSIVE_ZERG_FLYER_CARAPACE       = f"{ZERG_FLYER_UPGRADE_PREFIX} Carapace"
PROGRESSIVE_ZERG_WEAPON_UPGRADE       = f"{ZERG_UPGRADE_PREFIX} Weapon Upgrade"
PROGRESSIVE_ZERG_ARMOR_UPGRADE        = f"{ZERG_UPGRADE_PREFIX} Armor Upgrade"
PROGRESSIVE_ZERG_GROUND_UPGRADE       = f"{ZERG_UPGRADE_PREFIX} Ground Upgrade"
PROGRESSIVE_ZERG_FLYER_UPGRADE        = f"{ZERG_FLYER_UPGRADE_PREFIX} Upgrade"
PROGRESSIVE_ZERG_WEAPON_ARMOR_UPGRADE = f"{ZERG_UPGRADE_PREFIX} Weapon/Armor Upgrade"

# Zerg Unit Upgrades
ZERGLING_HARDENED_CARAPACE    = "Hardened Carapace (Zergling)"
ZERGLING_ADRENAL_OVERLOAD     = "Adrenal Overload (Zergling)"
ZERGLING_METABOLIC_BOOST      = "Metabolic Boost (Zergling)"
ROACH_HYDRIODIC_BILE          = "Hydriodic Bile (Roach)"
ROACH_ADAPTIVE_PLATING        = "Adaptive Plating (Roach)"
ROACH_TUNNELING_CLAWS         = "Tunneling Claws (Roach)"
HYDRALISK_FRENZY              = "Frenzy (Hydralisk)"
HYDRALISK_ANCILLARY_CARAPACE  = "Ancillary Carapace (Hydralisk)"
HYDRALISK_GROOVED_SPINES      = "Grooved Spines (Hydralisk)"
BANELING_CORROSIVE_ACID       = "Corrosive Acid (Baneling)"
BANELING_RUPTURE              = "Rupture (Baneling)"
BANELING_REGENERATIVE_ACID    = "Regenerative Acid (Baneling)"
MUTALISK_VICIOUS_GLAVE        = "Vicious Glave (Mutalisk)"
MUTALISK_RAPID_REGENERATION   = "Rapid Regeneration (Mutalisk)"
MUTALISK_SUNDERING_GLAVE      = "Sundering Glave (Mutalisk)"
SWARM_HOST_BURROW             = "Burrow (Swarm Host)"
SWARM_HOST_RAPID_INCUBATION   = "Rapid Incubation (Swarm Host)"
SWARM_HOST_PRESSURIZED_GLANDS = "Pressurized Glands (Swarm Host)"
ULTRALISK_BURROW_CHARGE       = "Burrow Charge (Ultralisk)"
ULTRALISK_TISSUE_ANIMATION    = "Tissue Animation (Ultralisk)"
ULTRALISK_MONARCH_BLADES      = "Monarch Blades (Ultralisk)"

# Zerg Strains
ZERGLING_RAPTOR_STRAIN     = "Raptor Strain (Zergling)"
ZERGLING_SWARMLING_STRAIN  = "Swarmling Strain (Zergling)"
ROACH_VILE_STRAIN          = "Vile Strain (Roach)"
ROACH_CORPSER_STRAIN       = "Corpser Strain (Roach)"
HYDRALISK_IMPALER_STRAIN   = "Impaler Strain (Hydralisk)"
HYDRALISK_LURKER_STRAIN    = "Lurker Strain (Hydralisk)"
BANELING_SPLITTER_STRAIN   = "Splitter Strain (Baneling)"
BANELING_HUNTER_STRAIN     = "Hunter Strain (Baneling)"
MUTALISK_BROOD_LORD_STRAIN = "Brood Lord Strain (Mutalisk)"
MUTALISK_VIPER_STRAIN      = "Viper Strain (Mutalisk)"
SWARM_HOST_CARRION_STRAIN  = "Carrion Strain (Swarm Host)"
SWARM_HOST_CREEPER_STRAIN  = "Creeper Strain (Swarm Host)"
ULTRALISK_NOXIOUS_STRAIN   = "Noxious Strain (Ultralisk)"
ULTRALISK_TORRASQUE_STRAIN = "Torrasque Strain (Ultralisk)"

# Zerg Mercs
INFESTED_MEDICS      = "Infested Medics"
INFESTED_SIEGE_TANKS = "Infested Siege Tanks"
INFESTED_BANSHEES    = "Infested Banshees"
    
# Kerrigan Upgrades
KERRIGAN_KINETIC_BLAST           = "Kinetic Blast (Kerrigan Tier 1)"
KERRIGAN_HEROIC_FORTITUDE        = "Heroic Fortitude (Kerrigan Tier 1)"
KERRIGAN_LEAPING_STRIKE          = "Leaping Strike (Kerrigan Tier 1)"
KERRIGAN_CRUSHING_GRIP           = "Crushing Grip (Kerrigan Tier 2)"
KERRIGAN_CHAIN_REACTION          = "Chain Reaction (Kerrigan Tier 2)"
KERRIGAN_PSIONIC_SHIFT           = "Psionic Shift (Kerrigan Tier 2)"
KERRIGAN_ZERGLING_RECONSTITUTION = "Zergling Reconstitution (Kerrigan Tier 3)"
KERRIGAN_IMPROVED_OVERLORDS      = "Improved Overlords (Kerrigan Tier 3)"
KERRIGAN_AUTOMATED_EXTRACTORS    = "Automated Extractors (Kerrigan Tier 3)"
KERRIGAN_WILD_MUTATION           = "Wild Mutation (Kerrigan Tier 4)"
KERRIGAN_SPAWN_BANELINGS         = "Spawn Banelings (Kerrigan Tier 4)"
KERRIGAN_MEND                    = "Mend (Kerrigan Tier 4)"
KERRIGAN_TWIN_DRONES             = "Twin Drones (Kerrigan Tier 5)"
KERRIGAN_MALIGNANT_CREEP         = "Malignant Creep (Kerrigan Tier 5)"
KERRIGAN_VESPENE_EFFICIENCY      = "Vespene Efficiency (Kerrigan Tier 5)"
KERRIGAN_INFEST_BROODLINGS       = "Infest Broodlings (Kerrigan Tier 6)"
KERRIGAN_FURY                    = "Fury (Kerrigan Tier 6)"
KERRIGAN_ABILITY_EFFICIENCY      = "Ability Efficiency (Kerrigan Tier 6)"
KERRIGAN_APOCALYPSE              = "Apocalypse (Kerrigan Tier 7)"
KERRIGAN_SPAWN_LEVIATHAN         = "Spawn Leviathan (Kerrigan Tier 7)"
KERRIGAN_DROP_PODS               = "Drop-Pods (Kerrigan Tier 7)"
KERRIGAN_PRIMAL_FORM             = "Primal Form (Kerrigan)"

# Kerrigan Levels
KERRIGAN_LEVELS_1  = "1 Kerrigan Level"
KERRIGAN_LEVELS_2  = "2 Kerrigan Levels"
KERRIGAN_LEVELS_3  = "3 Kerrigan Levels"
KERRIGAN_LEVELS_4  = "4 Kerrigan Levels"
KERRIGAN_LEVELS_5  = "5 Kerrigan Levels"
KERRIGAN_LEVELS_6  = "6 Kerrigan Levels"
KERRIGAN_LEVELS_7  = "7 Kerrigan Levels"
KERRIGAN_LEVELS_8  = "8 Kerrigan Levels"
KERRIGAN_LEVELS_9  = "9 Kerrigan Levels"
KERRIGAN_LEVELS_10 = "10 Kerrigan Levels"
KERRIGAN_LEVELS_14 = "14 Kerrigan Levels"
KERRIGAN_LEVELS_35 = "35 Kerrigan Levels"
KERRIGAN_LEVELS_70 = "70 Kerrigan Levels"

