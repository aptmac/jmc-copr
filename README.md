# JDK Mission Control copr (9.0.0)

### Motivation
The purpose of this repo is to provide Fedora users with a method of easily installing and using JDK Mission Control (JMC). The current methodology includes packaging JMC binaries produced by Adoptium, and hosting them on my copr page: https://copr.fedorainfracloud.org/coprs/almac/

Special thanks to the Adoptium team for providing easy access to builds of JMC. Please find below a list of releases currently supported in copr, and where to find the sources used to package them.

## Instructions for building in copr
1. Use the included script to download the JMC Snapshot builds from Adoptium<br>
  `$ bash fetch-sources.sh`

2. Create a source rpm containing the JMC binaries and contents of this repo<br>
  `$ fedpkg srpm`

3. Upload the resulting srpm to COPR, and initiate a build

## Instructions to use the application

1. Enable the copr repo<br>
  `$ sudo dnf copr enable almac/jmc9`

2. Install JDK Mission Control<br>
  `$ sudo dnf install jmc`

3. Run JDK Mission Control<br>
  `$ jmc`
