# JMC 8 Builds (using AdoptOpenJDK binaries) in copr

## Motivation
The contents of this repository help to provide an option for easily downloading and using JDK Mission Control in Fedora.

## Instructions for building in copr
1. Use the included script to download the JMC builds from AdoptOpenJDK<br>
  `$ bash fetch-sources.sh`

2. Create a source rpm containing the JMC binaries and contents of this repo<br>
  `$ fedpkg srpm`

3. Upload the resulting srpm to COPR, and initiate a build

## Instructions to use the application

1. Enable the copr repo<br>
  `$ dnf copr enable almac/jmc8`

2. Install JDK Mission Control<br>
  `$ sudo dnf install jmc`

3. Run JDK Mission Control<br>
  `$ jmc`
