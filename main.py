from proracun import Vratilo, Lezaj

if __name__ == "__main__":
    vratilo = Vratilo()
    vratilo.plotForcesMoments()
    vratilo.plotShaft()

    lezajA = Lezaj("NU 206 ECP", 30, vratilo.F_A, 0, 44000, 36500, 0, True)
    lezajA.checkBearing()

    print("\n")

    # First iteration
    lezajB = Lezaj("6406", 30, vratilo.F_B, vratilo.F_Ba, 43600, 23600, 12, False)
    lezajB.checkBearing()

    print()

    # Second iteration
    lezajB = Lezaj("6307", 35, vratilo.F_B, vratilo.F_Ba, 35100, 19000, 13, False)
    lezajB.checkBearing()
