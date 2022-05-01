from Land import Land


class StapleLands:
    def getStapleLands(deckColors=[]):
        colors = deckColors
        recommendedLands = list()
        stapleLands = StapleLands.initStapleLands()

        for x in stapleLands:
            if x.isWithinIdentity(colors):
                recommendedLands.append(x)

        return recommendedLands

    def initStapleLands():
        staples = list()

        badlands = Land("Badlands", "dual", ['b', 'r'])
        bayou = Land("Bayou", "dual", ['b', 'g'])
        plateau = Land("Plateau", "dual", ['w', 'r'])
        savannah = Land("Savannah", "dual", ['w', 'g'])
        scrubland = Land("Scrubland", "dual", ['w', 'b'])
        taiga = Land("Taiga", "dual", ['r', 'g'])
        tropicalIsland = Land("Tropical Island", "dual", ['u', 'g'])
        tundra = Land("Tundra", "dual", ['w', 'u'])
        undergroundSea = Land("Underground Sea", "dual", ['u', 'b'])
        volcanicIsland = Land("Volcanic Island", "dual", ['u', 'r'])

        staples.append(badlands)
        staples.append(bayou)
        staples.append(plateau)
        staples.append(savannah)
        staples.append(scrubland)
        staples.append(taiga)
        staples.append(tropicalIsland)
        staples.append(tundra)
        staples.append(undergroundSea)
        staples.append(volcanicIsland)

        bloodCrypt = Land("Blood Crypt", "dual", ['b', 'r'])
        breedingPool = Land("Breeding Pool", "dual", ['u', 'g'])
        godlessShrine = Land("Godless Shrine", "dual", ['w', 'b'])
        hallowedFountain = Land("Hallowed Fountain", "dual", ['w', 'u'])
        overgrownTomb = Land("Overgrown Tomb", "dual", ['b', 'g'])
        sacredFoundry = Land("Sacred Foundry", "dual", ['w', 'r'])
        steamVents = Land("Steam Vents", "dual", ['u', 'r'])
        stompingGround = Land("Stomping Ground", "dual", ['r', 'g'])
        templeGarden = Land("Temple Garden", "dual", ['w', 'g'])
        wateryGrave = Land("Watery Grave", "dual", ['u', 'b'])

        staples.append(bloodCrypt)
        staples.append(breedingPool)
        staples.append(godlessShrine)
        staples.append(hallowedFountain)
        staples.append(overgrownTomb)
        staples.append(sacredFoundry)
        staples.append(steamVents)
        staples.append(stompingGround)
        staples.append(templeGarden)
        staples.append(wateryGrave)

        aridMesa = Land("Arid Mesa", "fetch", ['w', 'r'])
        bloodstainedMire = Land("Bloodstained Mire", "fetch", ['b', 'r'])
        floodedStrand = Land("Flooded Strand", "fetch", ['w', 'u'])
        marshFlats = Land("Marsh Flats", "fetch", ['w', 'b'])
        mistyRainforest = Land("Misty Rainforest", "fetch", ['u', 'g'])
        pollutedDelta = Land("Polluted Delta", "fetch", ['u', 'b'])
        scaldingTarn = Land("Scalding Tarn", "fetch", ['u', 'r'])
        verdantCatacombs = Land("Verdant Catacombs", "fetch", ['b', 'g'])
        windsweptHeath = Land("Windswept Heath", "fetch", ['w', 'g'])
        woodedFoothills = Land("Wooded Foothills", "fetch", ['r', 'g'])

        staples.append(aridMesa)
        staples.append(bloodstainedMire)
        staples.append(floodedStrand)
        staples.append(marshFlats)
        staples.append(mistyRainforest)
        staples.append(pollutedDelta)
        staples.append(scaldingTarn)
        staples.append(verdantCatacombs)
        staples.append(windsweptHeath)
        staples.append(woodedFoothills)

        commandTower = Land("Command Tower", "5c", ['w', 'u', 'b', 'r', 'g'])
        exoticOrchard = Land("Exotic Orchard", "5c", ['w', 'u', 'b', 'r', 'g'])
        cityOfBrass = Land("City of Brass", "5c", ['w', 'u', 'b', 'r', 'g'])
        manaConfluence = Land("Mana Confluence", "5c", ['w', 'u', 'b', 'r', 'g'])
        tarnishedCitadel = Land("Tarnished Citadel", "5c", ['w', 'u', 'b', 'r', 'g'])
        forbiddenOrchard = Land("Forbidden Orchard", "5c", ['w', 'u', 'b', 'r', 'g'])

        staples.append(commandTower)
        staples.append(exoticOrchard)
        staples.append(cityOfBrass)
        staples.append(manaConfluence)
        staples.append(tarnishedCitadel)
        staples.append(forbiddenOrchard)
			
        return staples
