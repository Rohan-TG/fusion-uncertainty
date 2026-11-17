# converts % isotopic composition to % mass for MCNP inputs
import numpy as np
import periodictable
from periodictable.mass import isotope_abundance


def atomic_to_mass(Z, Aisotope, fraction_by_mass):
	"""Z: Queried material Z
	Aisotope: Nucleon number
	pct_by_mass: fraction of material composed by query"""

	element = periodictable.elements[Z]
	abundance =element[Aisotope].abundance / 100

	isotope_mass = element[Aisotope].mass

	isotope_abundances = []
	isotope_masses = []
	for isotope in element:
		if isotope.abundance > 0:
			isotope_abundances.append((isotope.abundance / 100))
			isotope_masses.append(isotope.mass)

	mass_abundance = (isotope_mass * abundance) / (np.sum([ab * isomass for ab, isomass in zip(isotope_abundances, isotope_masses)]))
	mass_fraction = fraction_by_mass * mass_abundance
	return mass_fraction