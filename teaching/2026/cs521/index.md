---
layout: default
---

# CS521 - Foundations of Crypto: From Blockchain to Present (Spring 2026)

Students enrolled in this class are expected to check this web page regularly. 
Complete lecture notes will be posted here.

## Zoom Link

This class will be taught on Wednesdays on the main UIUC campus, and on Fridays at the UIUC center in Chicago.  Students are welcome to attend both in person if they can/want, but they can also attend the class online at the following Zoom link:

[https://illinois.zoom.us/j/2172447431?pwd=dEtxWmdJR0FYOElUa1ZLL2RJRzdZUT09](https://illinois.zoom.us/j/2172447431?pwd=dEtxWmdJR0FYOElUa1ZLL2RJRzdZUT09)

### Lecture Recordings

We will record the lectures and post the links here (please always remind me to push "record"!):

[Jan 21](https://illinois.zoom.us/rec/share/EFX3hraatADbfPbXtkaEgb0VXcn5SzbyRbwqOtn9TXC6SCOBe-SGBotxUjOA6Csi.4rd-HiiHmZw2pe9J)
[Jan 23](https://illinois.zoom.us/rec/share/3DtqoyfcPYSa3haOld2N8ztBib9ZXkh5I1ylrOwsMqLJ-lDckf3lnQANhouIlg8.0LP3cePSiYu0dHsQ)
[Jan 28](https://illinois.zoom.us/rec/share/m7ndYHPfRfIe3ZZUf2UXxNqS0_O4N8BRZlEe71Rxe6wThcypS7R3oHVXl2svxw4d.ro2reWa_HVYgY0Gk)
[Jan 30](https://illinois.zoom.us/rec/share/Zli36X-2JEKSi2pat4S8cqtM8dZ1pjAzpfALMlxGdyyK2Fto8hx1xx7wZjIuGsjG.V1oDA8D_ogge3ZoB)
[Feb 4](https://illinois.zoom.us/rec/share/vqIUC9_7VCTKdrlwmC6tfue_Xco-w8QR6zwBaBjdPI01c2aZbxSD1LsyToGaUOVu.w7QCReKe6wnXKe5L)
[Feb 6](https://illinois.zoom.us/rec/share/hrLC8cjMcDtx9HseBpIagBxGYp-U57tJKNOfcs0V2rJbW_J2Wp_7qS9YtjkBPdx-.xZkneUSgU18HvQOj)
[Feb 11](https://illinois.zoom.us/rec/share/TjJFc3StgcrHJVkdgLnjs5s385s3EyLs1KreRL9qFPRSX165MJwaS8uvFDHOfkaI.siFhZmPxCHmJjkfn)
[Feb 13](https://illinois.zoom.us/rec/share/3dgH-WViXdA0DAYFJJbq0ZkgU3a_viOU3ikowtOMk0pOXUzRPv0tkFwISjR4RNqu.-amJscodxBvIpzLO)
[Feb 18](https://illinois.zoom.us/rec/share/BekFKwzywjIdgWRbX_z_mQvHR8aDbPn7pPlAtooECxNxkDglIWAfar72kjc9m6I.eLBNO-B7JEq3x-CK)
[Feb 20](https://illinois.zoom.us/rec/share/wBAUXg-GdylO07CXutG6uDic_-0rWOte4h8RPW48JwDp15LFDGDwtyjiRbtIcv88.zrMtwFImU6HrDopB)
[Feb 25](https://illinois.zoom.us/rec/share/t16Jsks43_wcGN97Y1ZYIsL6opFdvIDv0th80XsDMDzodL1K6qrNVmAoq-P4nHIy.udqK6CcwXkGZBxj-)

## Course Description

This class will introduce the fundamental concepts that underlie the emerging Crypto and Web3 technology in general, mostly but incorrectly identified with "blockchains".  Starting with basic concepts such as how to calculate hashes, sign transactions, and authenticate signatures, the course will then dive into consensus protocols, verifiable computing and zero-knowledge cryptography, blockchain languages and virtual machines, as well we various incentivization mechanisms for actors in decentralized networks to operate honestly.  The students taking this class will also be asked to read papers and blogs and discuss these topics in class, including potentially controversial topics which are of interest to the growing blockchain community.

<b>Prerequisites:</b> Basic understanding of math, to understand how and why a distributed protocol works, how a hash function is computed, and how a program is executed and produces a proof of its execution.

- Meetings: W/F 15:30-16:45.  On Wednesday, class will be taught on the Urbana-Champaign campus, in room Siebel 0220.  On Fridays, it will be taught at the UIUC Chicago center (Room 1XILLC-ARR).
- Credit: 4 credits
- Professor: [Grigore Rosu]({{site.baseurl}}/people/grigore-rosu/index.html) (Office: SC 2110)
- Office hours: Held by Grigore Rosu on Zoom or in SC 2110 or in Chicago; by appointment.

### [Syllabus](cs521 Syllabus.pdf) --- updated Feb 25

## Lecture Notes, Useful Material

The links below provide you with useful material for this class, including complete lecture notes. These materials will be added by need and can be changed repeatedly, so check regularly.

- ***Topic 1: Short History of Money*** [Slides.pdf](cs521 - Topic 1.pdf)
- ***Topic 2: Basic Cryptographic Primitives*** [Slides.pdf](cs521 - Topic 2.pdf)
- ***Topic 3: Bitcoin*** [Slides.pdf](cs521 - Topic 3.pdf) -- [White Paper](https://bitcoin.org/bitcoin.pdf)
- ***Topic 4: Ethereum*** [Slides.pdf](cs521 - Topic 4.pdf) -- [White Paper](https://ethereum.org/en/whitepaper/) -- [Yellow Paper](https://ethereum.github.io/yellowpaper/paper.pdf) -- [KEVM](https://jellopaper.org/) -- [ERC20](https://ethereum.org/en/developers/docs/standards/tokens/erc-20/)
- ***Topic 5: Consensus*** [Slides.pdf](cs521 - Topic 5.pdf) -- [Proof of Stake Ethereum](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/) -- Beacon Chain [K Formal Model](https://github.com/runtimeverification/beacon-chain-spec) [Dafny Formal Model](https://arxiv.org/abs/2110.12909) [Coq Formal Model](https://github.com/runtimeverification/beacon-chain-verification/tree/master/casper/coq) -- RANDAO [Statistical Model Checking](https://link.springer.com/chapter/10.1007/978-3-030-54994-7_25) 
- ***Topic 6: Zero-Knowledge Proofs*** [Slides.pdf](cs521 - Topic 6.pdf) [Justin Thaler's book](https://people.cs.georgetown.edu/jthaler/ProofsArgsAndZK.html)
- ...

