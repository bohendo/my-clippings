
---
#  Mastering Bitcoin
## by Andreas Antonopoulos
---

 - loc 258 - currencies were targeted by worried governments and eventually litigated

 - loc 369 - A wallet is simply a collection of addresses and the keys that unlock the funds within.

 - loc 512 - The inputs and outputs (debits and credits) do not necessarily add up to the same amount. Instead, outputs add up to slightly less than inputs and the difference represents an implied “transaction fee,”

 - loc 516 - In bitcoin terms, “spending” is signing a transaction that transfers value from a previous transaction over to a new owner identified by a bitcoin address.

 - loc 519 - Transactions move value from transaction inputs to transaction outputs. An input is where the coin value is coming from, usually a previous transaction’s output. A transaction output assigns a new owner to the value by associating it with a key. The destination key is called an encumbrance. It imposes a requirement for a signature for the funds to be redeemed in future transactions.

 - loc 565 - This URL will return all the unspent transaction outputs for an address, giving any application the information it needs to construct transaction inputs for spending. We use the simple command-line HTTP client cURL to retrieve the response. Example 2-1. Look up all the unspent outputs for Alice’s bitcoin address $ curl https://blockchain.info/unspent?active=1Cdid9KFAaatwczBwBttQcwXYCpvK8h7FK

 - loc 624 - Because the transaction contains all the information necessary to process, it does not matter how or where it is transmitted to the bitcoin network.

 - loc 630 - Any bitcoin network node (other client) that receives a valid transaction it has not seen before will immediately forward it to other nodes to which it is connected.

 - loc 654 - A good way to describe mining is like a giant competitive game of sudoku that resets every time someone finds a solution and whose difficulty automatically adjusts so that it takes approximately 10 minutes to find a solution.

 - loc 666 - As more miners started joining the bitcoin network, the difficulty of the problem increased rapidly. Soon, Jing and other miners upgraded to more specialized hardware, such as high-end dedicated graphical processing units (GPUs) cards such as those used in gaming desktops or consoles. At the time of this writing, the difficulty is so high that it is profitable only to mine with application-specific integrated circuits (ASIC), essentially hundreds of mining algorithms printed in hardware, running in parallel on a single silicon chip.

 - loc 869 - The Bitcoin Core client implements a JSON-RPC interface that can also be accessed using the command-line helper bitcoin-cli.

 - loc 1051 - Transaction IDs are not authoritative until a transaction has been confirmed. Absence of a transaction hash in the blockchain does not mean the transaction was not processed. This is known as “transaction malleability,” because transaction hashes can be modified prior to confirmation in a block. After confirmation, the txid is immutable and authoritative.

 - loc 1359 - The libbitcoin library is a cross-platform C++ development toolkit that supports the libbitcoin-server full node and the Bitcoin Explorer (bx) command line tool. The bx commands offer many of the same capabilities as the bitcoind client commands we illustrated in this chapter. The bx commands also offer some key management and manipulation tools that are not offered by bitcoind, including type-2 deterministic keys and mnemonic key encoding, as well as stealth address, payment, and query support.

 - loc 1371 - Bitcoin Explorer offers many useful commands for encoding and decoding addresses, and converting to and from different formats and representations.

 - loc 1498 - In the payment portion of a bitcoin transaction, the recipient’s public key is represented by its digital fingerprint, called a bitcoin address, which is used in the same way as the beneficiary name on a check (i.e., “Pay to the order of”).

 - loc 1498 - In the payment portion of a bitcoin transaction, the recipient’s public key is represented by its digital fingerprint, called a bitcoin address, which is used in the same way as the beneficiary name on a check (i.e., “Pay to the order of”). In most cases, a bitcoin address is generated from and corresponds to a public key.

 - loc 1498 - In the payment portion of a bitcoin transaction, the recipient’s public key is represented by its digital fingerprint, called a bitcoin address, which is used in the same way as the beneficiary name on a check (i.e., “Pay to the order of”). In most cases, a bitcoin address is generated from and corresponds to a public key. However, not all bitcoin addresses represent public keys; they can also represent other beneficiaries such as scripts,

 - loc 1504 - The bitcoin address is the only representation of the keys that users will routinely see, because this is the part they need to share with the world.

 - loc 1514 - Bitcoin uses elliptic curve multiplication as the basis for its public key cryptography.

 - loc 1523 - In most wallet implementations, the private and public keys are stored together as a key pair for convenience. However, the public key can be calculated from the private key, so storing only the private key is also possible.

 - loc 1528 - The private key (k) is a number, usually picked at random. From the private key, we use elliptic curve multiplication, a one-way cryptographic function, to generate a public key (K). From the public key (K), we use a one-way cryptographic hash function to generate a bitcoin address (A).

 - loc 1541 - You can pick your private keys randomly using just a coin, pencil, and paper: toss a coin 256 times and you have the binary digits of a random private key you can use in a bitcoin wallet.

 - loc 1553 - In programming terms, this is usually achieved by feeding a larger string of random bits, collected from a cryptographically secure source of randomness, into the SHA256 hash algorithm that will conveniently produce a 256-bit number.

 - loc 1585 - The public key is calculated from the private key using elliptic curve multiplication, which is irreversible: where k is the private key, G is a constant point called the generator point and K is the resulting public key. The reverse operation, known as “finding the discrete logarithm” — calculating k if you know K — is as difficult as trying all possible values of k, i.e., a brute-force search.

 - loc 1596 - Bitcoin uses a specific elliptic curve and set of mathematical constants, as defined in a standard called secp256k1, established by the National Institute of Standards and Technology (NIST).

 - loc 1598 - The secp256k1 curve is defined by the following function, which produces

 - loc 1604 - finite field of prime order

 - loc 1628 - There is also a + operator, called “addition,” which has some properties similar to the traditional addition of real numbers

 - loc 1629 - some properties similar to the traditional addition of real numbers that grade school children learn. Given two points P1 and P2 on the elliptic curve, there is a third point P3 = P1 + P2, also on the elliptic curve.

 - loc 1629 - some properties similar to the traditional addition of real numbers that grade school children learn. Given two points P1 and P2 on the elliptic curve, there is a third point P3 = P1 + P2, also on the elliptic curve. Geometrically, this third point P3 is calculated by drawing a line between P1 and P2.

 - loc 1629 - some properties similar to the traditional addition of real numbers that grade school children learn. Given two points P1 and P2 on the elliptic curve, there is a third point P3 = P1 + P2, also on the elliptic curve. Geometrically, this third point P3 is calculated by drawing a line between P1 and P2. This line will intersect the elliptic curve in exactly one additional place. Call this point P3' = (x, y). Then reflect in the x-axis to get P3 = (x, –y). There

 - loc 1629 - some properties similar to the traditional addition of real numbers that grade school children learn. Given two points P1 and P2 on the elliptic curve, there is a third point P3 = P1 + P2, also on the elliptic curve. Geometrically, this third point P3 is calculated by drawing a line between P1 and P2. This line will intersect the elliptic curve in exactly one additional place. Call this point P3' = (x, y). Then reflect in the x-axis to get P3 = (x, –y).

 - loc 1634 - If P1 and P2 are the same point, the line “between” P1 and P2 should extend to be the tangent on the curve at this point P1.

 - loc 1643 - Now that we have defined addition, we can define multiplication in the standard way that extends addition. For a point P on the elliptic curve, if k is a whole number, then kP = P + P + P + … + P (k times).

 - loc 1711 - Base58 is Base64 without the 0 (number zero), O (capital o), l (lower L), I (capital i), and the symbols “\+” and “/”.

 - loc 1716 - Base58Check is a Base58 encoding format, frequently used in bitcoin, which has a built-in error-checking code. The checksum is an additional four bytes added to the end of the data that is being encoded. The checksum is derived from the hash of the encoded data and

 - loc 1716 - The checksum is an additional four bytes added to the end of the data that is being encoded.

 - loc 1718 - When presented with a Base58Check code, the decoding software will calculate the checksum of the data and compare it to the checksum included in the code.

 - loc 1721 - To convert data (a number) into a Base58Check format, we first add a prefix to the data, called the “version byte,” which serves to easily identify the type of data that is encoded. For example, in the case of a bitcoin address the prefix is zero (0x00 in hex),

 - loc 1728 - The result is composed of three items: a prefix, the data, and a checksum. This result is encoded using the Base58 alphabet described previously.

 - loc 1733 - In bitcoin, most of the data presented to the user is Base58Check-encoded to make it compact, easy to read, and easy to detect errors. The version prefix in Base58Check encoding is used to create easily distinguishable formats, which when encoded in Base58 contain specific characters at the beginning of the Base58Check-encoded payload. These characters make it easy for humans to identify the type of data that is

 - loc 1733 - In bitcoin, most of the data presented to the user is Base58Check-encoded to make it compact, easy to read, and easy to detect errors. The version prefix in Base58Check encoding is used to create easily distinguishable formats, which when encoded in Base58 contain specific characters at the beginning of the Base58Check-encoded payload. These characters make it easy for humans to identify the type of data that is encoded and how to use it.

 - loc 1733 - In bitcoin, most of the data presented to the user is Base58Check-encoded to make it compact, easy to read, and easy to detect errors. The version prefix in Base58Check encoding is used to create easily distinguishable formats, which when encoded in Base58 contain specific characters at the beginning of the Base58Check-encoded payload. These characters make it easy for humans to identify the type of data that is encoded and how to use it. This is what differentiates, for example, a Base58Check-encoded bitcoin address that starts with a 1 from a Base58Check-encoded

 - loc 1856 - Wallet Import Format (WIF)

 - loc 1857 - Notice that the “payload” of the compressed key is appended with the suffix 01, signalling that the derived public key is to be compressed.

 - loc 1862 - opposite of the previous command), we use the base58check-encode

 - loc 1894 - if we know the x coordinate we can calculate the y coordinate by solving the equation y2 mod p = (x3 + 7) mod p. That allows us to store only the x coordinate of the public key point,

 - loc 1907 - to distinguish between the two possible values of y, we store a compressed public key with the prefix 02 if the y is even, and 03 if it is odd, allowing the software to correctly deduce the y coordinate from the x coordinate and uncompress the public key to the full coordinates of the point.

 - loc 1919 - a single private key can produce a public key expressed in two different formats (compressed and uncompressed) that produce two different bitcoin addresses. However, the private key is identical for both bitcoin addresses.

 - loc 1936 - Private keys are not compressed and cannot be compressed. The term “compressed private key” really means “private key from which compressed public keys should be derived,” whereas “uncompressed private key” really means “private key from which uncompressed public keys should be derived.”

 - loc 2155 - In the first bitcoin clients, wallets were simply collections of randomly generated private keys. This type of wallet is called a Type-0 nondeterministic wallet.

 - loc 2167 - Deterministic, or “seeded” wallets are wallets that contain private keys that are all derived from a common seed, through the use of a one-way hash function.

 - loc 2184 - BIP0039 defines the creation of a mnemonic code and seed as a follows: Create a random sequence (entropy) of 128 to 256 bits. Create a checksum of the random sequence by taking the first few bits of its SHA256 hash. Add the checksum to the end of the random sequence. Divide the sequence into sections of 11 bits, using those to index a dictionary of 2048 predefined words. Produce 12 to 24 words representing the mnemonic code.

 - loc 2231 - Hierarchical deterministic wallets contain keys derived in a tree structure, such that a parent key can derive a sequence of children keys, each of which can derive a sequence of grandchildren keys, and so on, to an infinite depth.

 - loc 2241 - The second advantage of HD wallets is that users can create a sequence of public keys without having access to the corresponding private keys. This allows HD wallets to be used on an insecure server or in a receive-only capacity,

 - loc 2254 - The root seed is input into the HMAC-SHA512 algorithm and the resulting hash is used to create a master private key (m) and a master chain code. The master private key (m) then generates a corresponding master public key (M), using the normal elliptic curve multiplication process m * G that we saw earlier in this chapter.

 - loc 2261 - The child key derivation functions are based on a one-way hash function that combines: A parent private or public key (ECDSA uncompressed key) A seed called a chain code (256 bits) An index number (32 bits) The chain code is used to introduce seemingly random data to the process, so that the index is not sufficient to derive other child keys.

 - loc 2274 - Each parent key can have 2 billion children keys.

 - loc 2278 - Child private keys are indistinguishable from nondeterministic (random) keys.

 - loc 2285 - A child private key, the corresponding public key, and the bitcoin address are all indistinguishable from keys and addresses created randomly. The fact that they are part of a sequence is not visible, outside of the HD wallet function that created them.

 - loc 2290 - The two essential ingredients are the key and chain code, and combined these are called an extended key. The term “extended key” could also be thought of as “extensible key” because such a key can be used to derive children.

 - loc 2290 - The two essential ingredients are the key and chain code, and combined these are called an extended key. The term “extended key” could also be thought of as “extensible key” because such a key can be used to derive children. Extended keys are stored and represented simply as the concatenation of the 256-bit key and 256-bit chain code into a 512-bit sequence. There are two types of extended keys. An extended private key is the combination of a private key and chain code and can be used to derive child private keys (and from them, child public keys).

 - loc 2290 - The two essential ingredients are the key and chain code, and combined these are called an extended key. The term “extended key” could also be thought of as “extensible key” because such a key can be used to derive children. Extended keys are stored and represented simply as the concatenation of the 256-bit key and 256-bit chain code into a 512-bit sequence. There are two types of extended keys. An extended private key is the combination of a private key and chain code and can be used to derive child private keys (and from them, child public keys). An extended public key is a public key and chain code, which can be used to create child public keys,

 - loc 2290 - The two essential ingredients are the key and chain code, and combined these are called an extended key. The term “extended key” could also be thought of as “extensible key” because such a key can be used to derive children. Extended keys are stored and represented simply as the concatenation of the 256-bit key and 256-bit chain code into a 512-bit sequence. There are two types of extended keys. An extended private key is the combination of a private key and chain code and can be used to derive child private keys (and from them, child public keys). An extended public key is a public key and chain code, which can be used to create child public keys, as described in Generating a Public Key

 - loc 2300 - Sharing an extended key gives access to the entire branch.

 - loc 2302 - The Base58Check coding for extended keys uses a special version number that results in the prefix “xprv” and “xpub” when encoded in Base58 characters, to make them easily recognizable. Because the extended key is 512 or 513 bits, it is also much longer than other Base58Check-encoded strings we have seen previously.

 - loc 2313 - An extended public key can be used, therefore, to derive all of the public keys (and only the public keys) in that branch of the HD wallet structure.

 - loc 2313 - An extended public key can be used, therefore, to derive all of the public keys (and only the public keys) in that branch of the HD wallet structure. This shortcut can be used to create very secure public-key-only deployments where a server or application has a copy of an extended public key and no private keys whatsoever. That kind of deployment can produce an infinite number of public keys and bitcoin addresses, but cannot spend any of the money sent to those addresses.

 - loc 2313 - An extended public key can be used, therefore, to derive all of the public keys (and only the public keys) in that branch of the HD wallet structure. This shortcut can be used to create very secure public-key-only deployments where a server or application has a copy of an extended public key and no private keys whatsoever. That kind of deployment can produce an infinite number of public keys and bitcoin addresses, but cannot spend any of the money sent to those addresses. Meanwhile, on another, more secure server, the extended private key can derive all the corresponding private keys to sign transactions and spend the money.

 - loc 2313 - An extended public key can be used, therefore, to derive all of the public keys (and only the public keys) in that branch of the HD wallet structure. This shortcut can be used to create very secure public-key-only deployments where a server or application has a copy of an extended public key and no private keys whatsoever. That kind of deployment can produce an infinite number of public keys and bitcoin addresses, but cannot spend any of the money sent to those addresses. Meanwhile, on another, more secure server, the extended private key can derive all the corresponding private keys to sign transactions and spend the money. One common application of this solution is to install an extended public key on a web server that serves an ecommerce application.

 - loc 2334 - single leaked child private key, together with a parent

 - loc 2334 - A single leaked child private key, together with a parent chain code, reveals all the private keys of all the children. Worse, the child private key together with a parent chain code can be used to deduce the parent private key. To counter this risk, HD wallets use an alternative derivation function called hardened derivation, which “breaks” the relationship between parent public key and child chain code. The hardened derivation function uses the parent private key to derive the child chain code, instead of the parent public key.

 - loc 2349 - a best practice, the level-1 children of the master keys are always derived through the hardened derivation, to prevent compromise of the master keys.

 - loc 2349 - As a best practice, the level-1 children of the master keys are always derived through the hardened derivation, to prevent compromise of the master keys.

 - loc 2352 - The index number used in the derivation function is a 32-bit integer. To easily distinguish between keys derived through the normal derivation function versus keys derived through hardened derivation, this index number is split into two ranges. Index numbers between 0 and 231–1 (0x0 to 0x7FFFFFFF) are used only for normal derivation. Index numbers between 231 and 232–1 (0x80000000 to 0xFFFFFFFF) are used only for hardened derivation.

 - loc 2354 - Index numbers between 0 and 231–1 (0x0 to 0x7FFFFFFF) are used only for normal derivation. Index numbers between 231 and 232–1 (0x80000000 to 0xFFFFFFFF) are used only for hardened derivation.

 - loc 2357 - To make the index number easier to read and display, the index number for hardened children is displayed starting from zero, but with a prime symbol. The first normal child key is therefore displayed as 0, whereas the first hardened child (index 0x80000000) is displayed as 0'.

 - loc 2362 - Keys in an HD wallet are identified using a “path”

 - loc 2363 - Private keys derived from the master private key start with “m”. Public

 - loc 2363 - Private keys derived from the master private key start with “m”. Public keys derived from the master public key start with “M”.

 - loc 2364 - the first child private key of the master private key is m/0. The first child public key is M/0. The second grandchild of the first child is m/0/1, and so on.

 - loc 2366 - identifier m/x/y/z describes the key that is the z-th child of key m/x/y, which is the y-th child of key m/x, which is the x-th child of m.

 - loc 2391 - All HD wallets following the BIP0044 structure are identified by the fact that they only used one branch of the tree: m/44'/. BIP0044 specifies the structure as consisting of five predefined tree levels: m / purpose' / coin_type' / account' / change / address_index The first-level “purpose” is always set to 44'. The second-level “coin_type” specifies the type of cryptocurrency coin, allowing for multicurrency HD wallets where each currency has its own subtree under the second level.

 - loc 2417 - $ bx seed | bx hd-new > m # create a new master private key from a seed and store in file "m"

 - loc 2428 - $ cat m | bx hd-private | bx hd-private --index 12

 - loc 2428 - $ cat m | bx hd-private | bx hd-private --index 12 --hard | bx hd-private --index 4 # generate m/0/12'/4

 - loc 2444 - BIP0038 proposes a common standard for encrypting private keys with a passphrase and encoding them with Base58Check so that they can be stored securely

 - loc 2444 - BIP0038 proposes a common standard for encrypting private keys with a passphrase and encoding them with Base58Check so that they can be stored securely on backup media, transported securely between wallets, or kept in any other conditions where the key might be exposed.

 - loc 2446 - The standard for encryption uses the Advanced Encryption Standard (AES),

 - loc 2452 - you see a key that starts with 6P, that means it is encrypted and requires a passphrase in order to convert (decrypt) it back into a WIF-formatted private key (prefix 5) that can be used in any wallet.

 - loc 2452 - If you see a key that starts with 6P, that means it is encrypted and requires a passphrase in order to convert (decrypt) it back into a WIF-formatted private key (prefix 5) that can be used in any wallet.

 - loc 2456 - common use case for BIP0038 encrypted keys is for paper wallets that can be used to back up private keys on a piece of paper. As

 - loc 2472 - Bitcoin addresses that begin with the number “3” are pay-to-script hash (P2SH) addresses, sometimes erroneously called multi-signature or multi-sig addresses.

 - loc 2476 - funds sent to “3” addresses require something more than the presentation of one public key hash and one private key signature as proof of ownership. The requirements are designated at the time the address is created, within the script, and all inputs to this address will be encumbered with the same requirements.

 - loc 2480 - Encoding a pay-to-script hash address involves using the same double-hash function as used during creation of a bitcoin address, only applied on the script instead of the public key:

 - loc 2491 - P2SH address most often represents a multi-signature script, but it might also represent a script encoding other types of transactions.

 - loc 2491 - A P2SH address most often represents a multi-signature script, but it might also represent a script encoding other types of transactions.

 - loc 2496 - The bitcoin multi-signature feature is designed to require M signatures (also known as the “threshold”) from a total of N keys, known as an M-of-N multi-sig, where M is equal to or less than N.

 - loc 2504 - Vanity addresses are valid bitcoin addresses that contain human-readable messages. For example, 1LoveBPzzD72PUXLzCkYAtGFYmK5vYNR33 is a valid address that contains the letters forming the word “Love” as the first four Base-58 letters. Vanity addresses require generating and testing billions of candidate private keys, until one derives a bitcoin address with the desired pattern.

 - loc 2505 - 1LoveBPzzD72PUXLzCkYAtGFYmK5vYNR33 is a valid address that contains the letters forming the word “Love” as the first four Base-58 letters. Vanity addresses require generating and testing billions of candidate private keys, until one derives a bitcoin address with the desired pattern.

 - loc 2511 - Vanity addresses are no less or more secure than any other address.

 - loc 2572 - Each additional character increases the difficulty by a factor of 58.

 - loc 2580 - Example 4-8 shows an example of a “vanity miner,” a program designed to find vanity addresses, written in C+

 - loc 2580 - Example 4-8 shows an example of a “vanity miner,” a program designed to find vanity addresses, written in C++.

 - loc 2726 - Eugenia generates the vanity address 1Kids33q44erFfpeXrmDSz7zEqG2FesZEN, users are likely to look at the vanity pattern word and a few characters beyond, for example noticing the “1Kids33” part of the address. That would force an attacker to generate a vanity address matching at least six characters (two more), expending an effort that is 3,364 times (58 × 58) higher than the effort Eugenia expended for her four-character vanity.

 - loc 2729 - Essentially, the effort Eugenia expends (or pays a vanity pool for) “pushes” the attacker into having to produce a longer pattern vanity. If Eugenia pays a pool to generate an 8-character vanity address, the attacker would be pushed into the realm of 10 characters, which is infeasible on a personal computer and expensive even with a custom vanity-mining rig or vanity pool.

 - loc 2747 - bitaddress.org. This page contains all the code necessary to generate keys and paper wallets, even while completely disconnected from the Internet. To use it, save the HTML page on your local drive or on an external USB flash drive. Disconnect from the Internet and open the file in a browser.

 - loc 2765 - Although you can deposit funds into a paper wallet several times,

 - loc 2765 - Although you can deposit funds into a paper wallet several times, you should withdraw all funds only once, spending everything.

 - loc 2768 - By spending the entire balance of a paper wallet only once, you reduce the risk of key compromise. If you need only a small amount, send any remaining funds to a new paper wallet in the same transaction.

 - loc 2803 - Transactions can be created online or offline by anyone, even if the person creating the transaction is not an authorized signer on the account. For example, an accounts payable clerk might process payable checks for signature by the CEO.

 - loc 2815 - Because the transaction is signed and contains no confidential information, private keys, or credentials, it can be publicly broadcast using any underlying network transport that is convenient.

 - loc 2815 - Because the transaction is signed and contains no confidential information, private keys, or credentials, it can be publicly broadcast using any underlying network transport that is convenient. Unlike credit card transactions, for example, which contain sensitive information and

 - loc 2815 - Because the transaction is signed and contains no confidential information, private keys, or credentials, it can be publicly broadcast using any underlying network transport that is convenient. Unlike credit card transactions, for example, which contain sensitive information

 - loc 2815 - Because the transaction is signed and contains no confidential information, private keys, or credentials, it can be publicly broadcast using any underlying network transport that is convenient. Unlike credit card transactions, for example, which contain sensitive information and can only be transmitted on encrypted networks, a bitcoin transaction can be sent over any network. As long as the transaction can reach a bitcoin node that will propagate it into the bitcoin network, it doesn’t

 - loc 2815 - Because the transaction is signed and contains no confidential information, private keys, or credentials, it can be publicly broadcast using any underlying network transport that is convenient. Unlike credit card transactions, for example, which contain sensitive information and can only be transmitted on encrypted networks, a bitcoin transaction can be sent over any network. As long as the transaction can reach a bitcoin node that will propagate it into the bitcoin network, it doesn’t matter how it is transported to the first node. Bitcoin transactions

 - loc 2815 - Because the transaction is signed and contains no confidential information, private keys, or credentials, it can be publicly broadcast using any underlying network transport that is convenient. Unlike credit card transactions, for example, which contain sensitive information and can only be transmitted on encrypted networks, a bitcoin transaction can be sent over any network. As long as the transaction can reach a bitcoin node that will propagate it into the bitcoin network, it doesn’t matter how it is transported to the first node.

 - loc 2831 - Messages, including transactions and blocks, are propagated from each node to all the peers to which it is connected, a process called “flooding.” A new validated transaction injected into any node on the network will be sent to all of the nodes connected to it (neighbors), each of which will send the transaction to all its neighbors, and so on. In this way, within a few seconds a valid transaction will propagate in an exponentially expanding ripple across the network until all nodes in the network have received it.

 - loc 2835 - To prevent spamming, denial-of-service attacks, or other nuisance attacks against the bitcoin system, every node independently validates every transaction before propagating it further.

 - loc 2862 - Locktime, also known as nLockTime from the variable name used in the reference client, defines the earliest time that a transaction is valid and can be relayed on the network or added to the blockchain. It is set to zero in most transactions to indicate immediate propagation and execution. If locktime is nonzero and below 500 million, it is interpreted as a block height, meaning the transaction is not valid and is not relayed or included in the blockchain prior to the specified block height. If it is above 500 million, it is interpreted as a Unix Epoch timestamp

 - loc 2870 - The fundamental building block of a bitcoin transaction is an unspent transaction output, or UTXO.

 - loc 2878 - There are no accounts or balances in bitcoin; there are only unspent transaction outputs (UTXO) scattered in the blockchain.

 - loc 2881 - Although UTXO can be any arbitrary value, once created it is indivisible just like a coin that cannot be cut in half. If a UTXO is larger than the desired value of a transaction, it must still be consumed in its entirety and change must be generated in the transaction.

 - loc 2898 - The exception to the output and input chain is a special type of transaction called the coinbase transaction, which is the first transaction in each block. This transaction is placed there by the “winning” miner and creates brand-new bitcoin payable to that miner as a reward for mining.

 - loc 2929 - Example 5-1. A script that calls the blockchain.info API to find the UTXO related to an address

 - loc 2966 - Transaction outputs associate a specific amount (in satoshis) to a specific encumbrance or locking script that defines the condition that must be met to spend that amount. In most cases, the locking script will lock the output to a specific bitcoin address, thereby transferring ownership of that amount to the new owner.

 - loc 2966 - Transaction outputs associate a specific amount (in satoshis) to a specific encumbrance or locking script that defines the condition that must be met to spend that amount. In most cases, the locking script will lock the output to a specific bitcoin address, thereby transferring ownership of that amount to the new owner. When Alice paid Bob’s Cafe for a cup of coffee, her transaction created a 0.015 bitcoin output encumbered or locked to the cafe’s bitcoin address.

 - loc 2982 - Example 5-3. A script for calculating how much total bitcoin will be issued

 - loc 3124 - Transaction fees serve as an incentive to include (mine) a transaction into the next block and also as a disincentive against “spam” transactions or any kind of abuse of the system, by imposing a small cost on every transaction.

 - loc 3149 - if you consume a 20-bitcoin UTXO to make a 1-bitcoin payment, you must include a 19-bitcoin change output back to your wallet. Otherwise, the 19-bitcoin “leftover” will be counted as a transaction fee and will be collected by the miner who mines your transaction in a block.

 - loc 3176 - a technique used in CoinJoin transactions where multiple parties join transactions together to protect their privacy.

 - loc 3177 - When a chain of transactions is transmitted across the network, they don’t always arrive in the same order. Sometimes, the child might arrive before the parent. In that case, the nodes that see a child first can see that it references a parent transaction that is not yet known. Rather than reject the child, they put it in a temporary pool to await the arrival of its parent and propagate it to every other node. The pool of transactions without parents is known as the orphan transaction pool. Once the parent arrives, any orphans that reference the UTXO created by the parent are released from the pool, revalidated recursively, and then the entire chain of transactions can be included in the transaction pool, ready to be mined in a block.

 - loc 3185 - There is a limit to the number of orphan transactions stored in memory, to prevent a denial-of-service attack against bitcoin nodes.

 - loc 3187 - the number of orphan transactions in the pool

 - loc 3187 - the number of orphan transactions in the pool exceeds MAX_ORPHAN_TRANSACTIONS, one or more randomly selected orphan transactions are evicted from the pool,

 - loc 3187 - client. If the number of orphan transactions in the pool exceeds MAX_ORPHAN_TRANSACTIONS, one or more randomly selected orphan transactions are evicted from the pool,

 - loc 3187 - If the number of orphan transactions in the pool exceeds MAX_ORPHAN_TRANSACTIONS, one or more randomly selected orphan transactions are evicted from the pool,

 - loc 3200 - Bitcoin transaction validation is not based on a static pattern, but instead is achieved through the execution of a scripting language. This language allows for a nearly infinite variety of conditions to be expressed. This is how bitcoin gets the power of “programmable money.”

 - loc 3206 - Historically, the locking script was called a scriptPubKey, because it usually contained a public key or bitcoin address. In this book we refer to it as a “locking script” to acknowledge the much broader range of possibilities of this scripting technology.

 - loc 3206 - A locking script is an encumbrance placed on an output, and it specifies the conditions that must be met to spend the output in the future. Historically, the locking script was called a scriptPubKey, because it usually contained a public key or bitcoin address. In this book we refer to it as a “locking script” to acknowledge the much broader range of possibilities of this scripting technology.

 - loc 3208 - In most bitcoin applications, what we refer to as a locking script will appear in the source code as scriptPubKey.

 - loc 3211 - Unlocking scripts are part of every transaction input, and most of the time they contain a digital signature produced by the user’s wallet from his or her private key. Historically, the unlocking script is called scriptSig, because it usually contained a digital signature.

 - loc 3222 - First, the unlocking script is executed, using the stack execution engine. If the unlocking script executed without errors (e.g., it has no “dangling” operators left over), the main stack (not the alternate stack) is copied and the locking script is executed. If the result of executing the locking script with the stack data copied from the unlocking script is “TRUE,” the unlocking script has succeeded in resolving the conditions imposed by the locking script and, therefore, the input is a valid authorization to spend the UTXO.

 - loc 3235 - The bitcoin transaction script language, called Script, is a Forth-like reverse-polish notation stack-based execution language.

 - loc 3237 - Script is a very simple language that was designed to be limited in scope and executable on a range of hardware, perhaps as simple as an embedded device, such as a handheld calculator.

 - loc 3237 - Script is a very simple language that was designed to be limited in scope and executable on a range of hardware, perhaps as simple as an embedded device, such as a handheld calculator. It requires minimal processing and cannot do many of the fancy things modern programming languages can do. In the case of programmable money, that is a deliberate security feature.

 - loc 3237 - Script is a very simple language that was designed to be limited in scope and executable on a range of hardware, perhaps as simple as an embedded device, such as a handheld calculator. It requires minimal processing and cannot do many of the fancy things modern programming languages can do. In the case of programmable money, that is a deliberate security feature. Bitcoin’s scripting language is called a stack-based language because it uses a data structure called a stack. A stack is a very simple data structure, which can be visualized as a stack of cards. A stack allows two operations: push and pop. Push adds an item on top of the stack. Pop removes the top item from the stack. The scripting language executes the script by processing each item from left to right. Numbers (data constants) are pushed onto the stack. Operators push or pop one or more parameters from the stack, act on them, and might push a result onto the stack. For example, OP_ADD will pop two items from the stack, add them, and push the resulting sum onto the stack. Conditional operators evaluate a condition, producing a boolean

 - loc 3278 - the language is not Turing Complete,

 - loc 3279 - the language cannot be used to create an infinite loop or other form of “logic bomb” that could be embedded in a transaction in a way that causes a denial-of-service attack against the bitcoin network.

 - loc 3284 - The bitcoin transaction script language is stateless,

 - loc 3289 - In the first few years of bitcoin’s development, the developers introduced some limitations in the types of scripts that could be processed by the reference client.

 - loc 3293 - Although it is possible to create a nonstandard transaction containing a script that is not one of the standard types, you must find a miner who does not follow these limitations to mine that transaction into a block.

 - loc 3296 - The five standard types of transaction scripts are pay-to-public-key-hash (P2PKH), public-key, multi-signature (limited to 15 keys), pay-to-script-hash (P2SH), and data output (OP_RETURN),

 - loc 3302 - An output locked by a P2PKH script can be unlocked (spent) by presenting a public key and a digital signature created by the corresponding private key.

 - loc 3304 - That transaction output would have a locking script of the form: OP_DUP OP_HASH160 <Cafe Public Key Hash> OP_EQUAL OP_CHECKSIG

 - loc 3308 - The preceding locking script can be satisfied with an unlocking script of the form: <Cafe Signature> <Cafe Public Key> The two scripts together would form the following combined validation script: <Cafe Signature> <Cafe Public Key> OP_DUP

 - loc 3308 - The preceding locking script can be satisfied with an unlocking script of the form: <Cafe Signature> <Cafe Public Key> The two scripts together would form the following combined validation script: <Cafe Signature> <Cafe Public Key> OP_DUP OP_HASH160 <Cafe Public Key Hash> OP_EQUAL OP_CHECKSIG

 - loc 3308 - The preceding locking script can be satisfied with an unlocking script of the form: <Cafe Signature> <Cafe Public Key> The two scripts together would form the following combined validation script: <Cafe Signature> <Cafe Public Key> OP_DUP OP_HASH160 <Cafe Public Key Hash> OP_EQUAL OP_CHECKSIG When executed, this combined script will evaluate to TRUE if, and only if, the unlocking script matches the conditions set by the locking script. In other words, the result will be TRUE if the unlocking script has a valid signature from the cafe’s private key that corresponds to the public key hash set as an encumbrance.

 - loc 3323 - A pay-to-public-key locking script looks like this: <Public Key A> OP_CHECKSIG The corresponding unlocking script that must be presented to unlock this type of output is a simple signature, like this: <Signature from Private Key A> The combined script, which is validated by the transaction validation software, is: <Signature from Private Key A> <Public Key A> OP_CHECKSIG

 - loc 3341 - The general form of a locking script setting an M-of-N multi-signature condition is: M <Public Key 1> <Public Key 2> ... <Public Key N> N OP_CHECKMULTISIG where N is the total number of listed public keys and M is the threshold of required signatures to spend the output.

 - loc 3341 - The general form of a locking script setting an M-of-N multi-signature condition is: M <Public Key 1> <Public Key 2> ... <Public Key N> N OP_CHECKMULTISIG where N is the total number of listed public keys and M is the threshold of required signatures to spend the output. A locking script setting a 2-of-3 multi-signature condition looks like this: 2 <Public Key A> <Public Key B> <Public Key C> 3 OP_CHECKMULTISIG

 - loc 3344 - A locking script setting a 2-of-3 multi-signature condition looks like this: 2 <Public Key A> <Public Key B> <Public Key C> 3 OP_CHECKMULTISIG The preceding locking script can be satisfied with an unlocking script containing pairs of signatures and public keys: OP_0 <Signature B> <Signature C>

 - loc 3344 - A locking script setting a 2-of-3 multi-signature condition looks like this: 2 <Public Key A> <Public Key B> <Public Key C> 3 OP_CHECKMULTISIG The preceding locking script can be satisfied with an unlocking script containing pairs of signatures and public keys: OP_0 <Signature B> <Signature C> or any combination of two signatures from the private keys corresponding to the three listed public keys.

 - loc 3350 - The prefix OP_0 is required because of a bug in the original implementation of CHECKMULTISIG

 - loc 3353 - The two scripts together would form the combined validation script: OP_0 <Signature B> <Signature C> 2 <Public Key A> <Public Key B> <Public Key C> 3 OP_CHECKMULTISIG

 - loc 3360 - Many developers have tried to use the transaction scripting language to take advantage of the security and resilience of the system for applications such as digital notary services, stock certificates, and smart contracts.

 - loc 3364 - The use of bitcoin’s blockchain to store data unrelated to bitcoin payments is a controversial subject.

 - loc 3364 - The use of bitcoin’s blockchain to store data unrelated to bitcoin payments is a controversial subject. Many developers consider such use abusive and want to discourage it. Others view it as a demonstration of the powerful capabilities of blockchain technology and want to encourage such experimentation.

 - loc 3366 - Those who object to the inclusion of non-payment data argue that it causes “blockchain bloat,” burdening those running full bitcoin

 - loc 3366 - Those who object to the inclusion of non-payment data argue that it causes “blockchain bloat,” burdening those running full bitcoin nodes with carrying the cost of disk storage for data that the blockchain was not intended to carry. Moreover, such transactions create UTXO that cannot be spent, using the destination bitcoin address as a free-form 20-byte field.

 - loc 3366 - Those who object to the inclusion of non-payment data argue that it causes “blockchain bloat,” burdening those running full bitcoin nodes with carrying the cost of disk storage for data that the blockchain was not intended to carry. Moreover, such transactions create UTXO that cannot be spent, using the destination bitcoin address as a free-form 20-byte field. Because the address is used for data, it doesn’t correspond to a private key and the resulting UTXO can never be spent; it’s a fake payment.

 - loc 3368 - such transactions create UTXO that cannot be spent, using the destination bitcoin address as a free-form 20-byte field.

 - loc 3371 - In version 0.9 of the Bitcoin Core client, a compromise was reached with the introduction of the OP_RETURN operator. OP_RETURN allows developers to add 80 bytes of nonpayment data to a transaction output. However, unlike the use of “fake” UTXO, the OP_RETURN operator creates an explicitly provably unspendable output, which does not need to be stored in the UTXO set.

 - loc 3372 - OP_RETURN allows developers to add 80 bytes of nonpayment data to a transaction output. However, unlike the use of “fake” UTXO, the OP_RETURN operator creates an explicitly provably unspendable output, which does not need to be stored in the UTXO set.

 - loc 3377 - OP_RETURN scripts look like this: OP_RETURN <data>

 - loc 3386 - OP_RETURN is usually an output with a zero bitcoin amount, because any bitcoin assigned to such an output is effectively lost forever.

 - loc 3407 - multi-signature scheme like that offers corporate governance controls and protects against theft, embezzlement, or loss. The resulting script is quite long and looks like this: 2 <Mohammed's Public Key> <Partner1 Public Key> <Partner2 Public Key> <Partner3 Public Key> <Attorney Public Key> 5 OP_CHECKMULTISIG

 - loc 3407 - A multi-signature scheme like that offers corporate governance controls and protects against theft, embezzlement, or loss. The resulting script is quite long and looks like this: 2 <Mohammed's Public Key> <Partner1 Public Key> <Partner2 Public Key> <Partner3 Public Key> <Attorney Public Key> 5 OP_CHECKMULTISIG

 - loc 3416 - Pay-to-script-hash (P2SH) was developed to resolve these practical difficulties and to make the use of complex scripts as easy as a payment to a bitcoin address.

 - loc 3416 - Pay-to-script-hash (P2SH) was developed to resolve these practical difficulties and to make the use of complex scripts as easy as a payment to a bitcoin address. With P2SH payments, the complex locking script is replaced with its digital fingerprint, a cryptographic hash. When a transaction attempting to spend the UTXO is presented later, it must contain the script that matches the hash, in addition to the unlocking script. In simple terms, P2SH means “pay to a script matching this hash, a script that will be presented later when this output is spent.”

 - loc 3437 - This shifts the burden in fees and complexity from the sender to the recipient (spender) of the transaction.

 - loc 3450 - The 20-byte hash of the preceding script is: 54c557e07dde5bb6cb791c7a540e0a4796f5e97e A P2SH transaction locks the output to this hash instead of the longer script, using the locking script: OP_HASH160 54c557e07dde5bb6cb791c7a540e0a4796f5e97e OP_EQUAL which, as you can see, is much shorter. Instead of “pay to this 5-key multi-signature script,” the P2SH equivalent transaction is “pay to a script with this hash.”

 - loc 3451 - A P2SH transaction locks the output to this hash instead of the longer script, using the locking script: OP_HASH160 54c557e07dde5bb6cb791c7a540e0a4796f5e97e OP_EQUAL which, as you can see, is much shorter. Instead of “pay to this 5-key multi-signature script,” the P2SH equivalent transaction is “pay to a script with this hash.”

 - loc 3458 - The two scripts are combined in two stages. First, the redeem script is checked against the locking script to make sure the hash matches: <2 PK1 PK2 PK3 PK4 PK5 5 OP_CHECKMULTISIG> OP_HASH160 <redeem scriptHash> OP_EQUAL If the redeem script hash matches, the unlocking script is executed on its own, to unlock the redeem script: <Sig1> <Sig2> 2 PK1 PK2 PK3 PK4 PK5 5 OP_CHECKMULTISIG

 - loc 3486 - As of version 0.9.2 of the Bitcoin Core client, P2SH transactions can contain any valid script, making the P2SH standard much more flexible and allowing for experimentation with many novel and complex types of transactions.

 - loc 3491 - you lock an output with the hash of an invalid transaction it will be processed regardless.

 - loc 3491 - you lock an output with the hash of an invalid transaction it will be processed regardless. However, you will not be able to spend it

 - loc 3491 - if you lock an output with the hash of an invalid transaction it will be processed regardless. However, you will not be able to spend it

 - loc 3496 - The P2SH transaction will be considered valid and accepted even if the redeem script is invalid. You might accidentally lock bitcoin in such a way that it cannot later be spent.

 - loc 3511 - Decentralization of control is a core design principle and that can only be achieved and maintained by a flat, decentralized P2P consensus network. The term “bitcoin network” refers to the collection of nodes running the bitcoin P2P protocol. In addition to the bitcoin P2P protocol, there are other protocols such as Stratum, which are used for mining and lightweight or mobile wallets.

 - loc 3516 - We use the term “extended bitcoin network” to refer to the overall network that includes the bitcoin P2P protocol, pool-mining protocols, the Stratum protocol, and any other related protocols connecting the components of the bitcoin system.

 - loc 3521 - A bitcoin node is a collection of functions: routing, the blockchain database, mining, and wallet services.

 - loc 3527 - Some nodes, called full nodes, also maintain a complete and up-to-date copy of the blockchain.

 - loc 3529 - Some nodes maintain only a subset of the blockchain and verify transactions using a method called simplified payment verification, or SPV.

 - loc 3546 - Various large companies interface with the bitcoin network by running full-node clients based on the Bitcoin Core client, with full copies of the blockchain and a network node, but without mining or wallet functions. These nodes act as network edge routers, allowing various other services (exchanges, wallets, block explorers, merchant payment processing) to be built on top.

 - loc 3562 - To connect to a known peer, nodes establish a TCP connection, usually to port 8333 (the port generally known as the one used by bitcoin),

 - loc 3577 - How does a new node find peers? The first method is to query DNS using a number of “DNS seeds,” which are DNS servers that provide a list of IP addresses of bitcoin nodes. Some of those DNS seeds provide a static list of IP addresses of stable bitcoin listening nodes.

 - loc 3584 - Alternatively, a bootstrapping node that knows nothing of the network must be given the IP address of at least one bitcoin node, after which it can establish connections through further introductions.

 - loc 3686 - Let’s assume, for example, that a node only has the genesis block. It will then receive an inv message from its peers containing the hashes of the next 500 blocks in the chain. It will start requesting blocks from all of its connected peers, spreading the load and ensuring that it doesn’t overwhelm any peer with requests.

 - loc 3703 - SPV nodes download only the block headers and do not download the transactions included in each block. The resulting chain of blocks, without transactions, is 1,000 times smaller than the full blockchain. SPV nodes cannot construct a full picture of all the UTXOs that are available for spending because they do not know about all the transactions on the network. SPV nodes verify transactions using a slightly different methodology that relies on peers to provide partial views of relevant parts of the blockchain on demand.

 - loc 3719 - An SPV node cannot validate whether the UTXO is unspent. Instead, the SPV node will establish a link between the transaction and the block that contains it, using a merkle path (see Merkle Trees). Then, the SPV node waits until it sees the six blocks 300,001 through 300,006 piled on top of the block containing the transaction and verifies it by establishing its depth under blocks 300,006 to 300,001. The fact that other nodes on the network accepted block 300,000 and then did the necessary work to produce six more blocks on top of it is proof, by proxy, that the transaction was not a double-spend.

 - loc 3724 - An SPV node cannot be persuaded that a transaction exists in a block when the transaction does not in fact exist. The SPV node establishes the existence of a transaction in a block by requesting a merkle path proof and by validating the proof of work in the chain of blocks. However, a transaction’s existence can be “hidden” from an SPV node.

 - loc 3724 - An SPV node cannot be persuaded that a transaction exists in a block when the transaction does not in fact exist. The SPV node establishes the existence of a transaction in a block by requesting a merkle path proof and by validating the proof of work in the chain of blocks. However, a transaction’s existence can be “hidden” from an SPV node. An SPV node can definitely prove that a transaction exists but cannot verify that a transaction, such as a double-spend of the same UTXO, doesn’t exist because it doesn’t have a record of all transactions.

 - loc 3729 - To defend against this, an SPV node needs to connect randomly to several nodes, to increase the probability that it is in contact

 - loc 3729 - To defend against this, an SPV node needs to connect randomly to several nodes, to increase the probability that it is in contact with at least one honest node. This need to randomly connect means that SPV nodes also are vulnerable to network partitioning attacks or Sybil attacks, where they are connected to fake nodes or fake networks and do not have access to honest nodes or the real bitcoin network. For most practical purposes, well-connected SPV nodes are secure enough, striking the right balance between resource needs, practicality, and security. For infallible security, however, nothing beats running a full blockchain node.

 - loc 3735 - A full blockchain node verifies a transaction by checking the entire chain of thousands of blocks below it in order to guarantee that the UTXO is not spent, whereas an SPV node checks how deep the block is buried by a handful of blocks above it.

 - loc 3744 - Because SPV nodes need to retrieve specific transactions in order to selectively verify them, they also create a privacy risk. Unlike full blockchain nodes, which collect all transactions within each block, the SPV node’s requests for specific data can inadvertently reveal the addresses in their wallet.

 - loc 3748 - Shortly after the introduction of SPV/lightweight nodes, the bitcoin developers added a feature called bloom filters to address the privacy risks of SPV nodes.

 - loc 3748 - Shortly after the introduction of SPV/lightweight nodes, the bitcoin developers added a feature called bloom filters to address the privacy risks of SPV nodes. Bloom filters allow SPV nodes to receive a subset of the transactions without revealing precisely which addresses they are interested in, through a filtering mechanism that uses probabilities rather than fixed patterns.

 - loc 3753 - A bloom filter is a probabilistic search filter, a way to describe a desired pattern without specifying it exactly.

 - loc 3761 - If she asks a less specific pattern, she gets a lot more possible addresses and better privacy,

 - loc 3762 - Bloom filters serve this function by allowing an SPV node to specify a search pattern for transactions that can be tuned toward precision or privacy. A more specific bloom filter will produce accurate results, but at the expense of revealing what addresses are used in the user’s wallet. A less specific bloom filter will produce more data about more transactions, many irrelevant to the node, but will allow the node to maintain better privacy.

 - loc 3772 - Bloom filters are implemented as a variable-size array of N binary digits (a bit field) and a variable number of M hash functions.

 - loc 3772 - Bloom filters are implemented as a variable-size array of N binary digits (a bit field) and a variable number of M hash functions. The hash functions are designed to always produce an output that is between 1 and N,

 - loc 3772 - Bloom filters are implemented as a variable-size array of N binary digits (a bit field) and a variable number of M hash functions. The hash functions are designed to always produce an output that is between 1 and N, corresponding to the array of binary digits.

 - loc 3775 - By choosing different length (N) bloom filters and a different number (M) of hash functions, the bloom filter can be

 - loc 3775 - By choosing different length (N) bloom filters and a different number (M) of hash functions, the bloom filter can be tuned, varying the level of accuracy and therefore privacy.

 - loc 3780 - To add a pattern to the bloom filter, the pattern is hashed by each hash function in turn. Applying the first hash function to the input results in a number between 1 and N. The corresponding bit in the array (indexed from 1 to N) is found and set to 1,

 - loc 3798 - To test if a pattern is part of a bloom filter, the pattern is hashed by each hash function and the resulting bit pattern is tested against the bit array. If all the bits indexed by the hash functions are set to 1, then the pattern is probably recorded in the bloom filter. Because the bits may be set because of overlap from multiple patterns, the answer is not certain, but is rather probabilistic. In simple terms, a bloom filter positive match is a “Maybe, Yes.”

 - loc 3808 - In simple terms, a negative match on a bloom filter is a “Definitely Not!”

 - loc 3817 - filters are used to filter the transactions (and blocks containing them) that an SPV node receives from its peers. SPV nodes will create a filter that matches only the addresses held in the SPV node’s wallet. The

 - loc 3829 - Almost every node on the bitcoin network maintains a temporary list of unconfirmed transactions called the memory pool, mempool, or transaction pool.

 - loc 3842 - Both the transaction pool and orphan pool (where implemented) are stored in local memory and are not saved on persistent storage; rather, they are dynamically populated from incoming network messages.

 - loc 3842 - Both the transaction pool and orphan pool (where implemented) are stored in local memory and are not saved on persistent storage; rather, they are dynamically populated from incoming network messages. When a node starts, both pools are empty and are gradually populated with new transactions received on the network.

 - loc 3845 - Some implementations of the bitcoin client also maintain a UTXO database or UTXO pool, which is the set of all unspent outputs on the blockchain.

 - loc 3853 - Alert messages are a seldom used function, but are nevertheless implemented in most nodes. Alert messages are bitcoin’s “emergency broadcast system,” a means by which the core bitcoin developers can send an emergency text message to all bitcoin nodes.

 - loc 3856 - The alert system has only been used a handful of times, most notably in early 2013 when a critical database bug caused a

 - loc 3856 - The alert system has only been used a handful of times, most notably in early 2013 when a critical database bug caused a multiblock fork to occur in the bitcoin blockchain.

 - loc 3880 - The Bitcoin Core client stores the blockchain metadata using Google’s LevelDB database.

 - loc 3886 - each block contains the hash of its parent inside its own header. The sequence of hashes linking each block to its parent creates a chain going back all the way to the first block ever created, known as the genesis block.

 - loc 3893 - The “previous block hash” field is inside the block header and thereby affects the current block’s hash. The child’s own identity changes if the parent’s identity changes.

 - loc 3897 - This cascade effect ensures that once a block has many generations following it, it cannot be changed without forcing a recalculation of all subsequent blocks.

 - loc 3910 - The block is made of a header, containing metadata, followed by a long list of transactions that make up the bulk of its size. The block header is 80 bytes, whereas the average transaction is at least 250 bytes and the average block contains more than 500 transactions.

 - loc 3953 - The primary identifier of a block is its cryptographic hash, a digital fingerprint, made by hashing the block header

 - loc 3953 - The primary identifier of a block is its cryptographic hash, a digital fingerprint, made by hashing the block header twice through the SHA256 algorithm. The resulting 32-byte hash is called the block hash but is more accurately the block header hash, because only the block header is used to compute it.

 - loc 3953 - The primary identifier of a block is its cryptographic hash, a digital fingerprint, made by hashing the block header twice through the SHA256 algorithm. The resulting 32-byte hash is called the block hash but is more accurately the block header hash, because only the block header is used to compute it. For example, 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f

 - loc 3967 - Unlike the block hash, the block height is not a unique identifier.

 - loc 3968 - Two or more blocks might have the same block height, competing for the same position in the blockchain.

 - loc 4012 - The genesis block contains a hidden message within it. The coinbase transaction input contains the text “The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.” This message was intended to offer proof of the earliest date this block was created, by referencing the headline of the British newspaper The Times. It also serves as a tongue-in-cheek reminder of the importance of an independent monetary system, with bitcoin’s launch occurring at the same time as an unprecedented worldwide monetary crisis.

 - loc 4050 - A merkle tree, also known as a binary hash tree, is a data structure used for efficiently summarizing and verifying the integrity of large sets of data. Merkle trees are binary trees containing cryptographic hashes.

 - loc 4058 - A Merkle tree is constructed by recursively hashing pairs of nodes until there is only one hash, called the root, or merkle root.

 - loc 4058 - A Merkle tree is constructed by recursively hashing pairs of nodes until there is only one hash, called the root, or merkle root. The cryptographic hash algorithm used in bitcoin’s merkle trees is SHA256 applied twice, also known as double-SHA256.

 - loc 4058 - Merkle tree is constructed by recursively hashing pairs of nodes until there is only one hash, called the root, or merkle root. The cryptographic hash algorithm used in bitcoin’s merkle trees is SHA256 applied twice, also known as double-SHA256. When N data elements are hashed and summarized in a merkle tree, you can check to see if any one data element is included in the tree with at most 2*log2(N) calculations, making this a very efficient data structure.

 - loc 4067 - construct the parent node HAB, the two 32-byte hashes of the children are concatenated to create a 64-byte string. That string is then double-hashed to produce the parent node’s hash:

 - loc 4067 - For example, to construct the parent node HAB, the two 32-byte hashes of the children are concatenated to create a 64-byte string. That string is then double-hashed to produce the parent node’s hash: H~AB~ = SHA256(SHA256(H~A~ + H~B~)) The process continues until there is only

 - loc 4067 - For example, to construct the parent node HAB, the two 32-byte hashes of the children are concatenated to create a 64-byte string. That string is then double-hashed to produce the parent node’s hash: H~AB~ = SHA256(SHA256(H~A~ + H~B~)) The process continues until there is only one node at the top, the node known as the Merkle root.

 - loc 4073 - Because the merkle tree is a binary tree, it needs an even number of leaf nodes. If there is an odd number of transactions to summarize, the last transaction hash will be duplicated to create an even number of leaf nodes, also known as a balanced tree.

 - loc 4090 - node can prove that a transaction K is included in the block by producing a merkle path that is only four 32-byte hashes long (128 bytes total). The path consists of the four hashes (noted in blue in Figure 7-5) HL, HIJ, HMNOP and HABCDEFGH. With those four hashes provided as an authentication path, any node can prove that HK (noted in green in the diagram) is included in the merkle root by computing four additional pair-wise hashes HKL, HIJKL, HIJKLMNOP, and the merkle tree root

 - loc 4090 - a node can prove that a transaction K is included in the block by producing a merkle path that is only four 32-byte hashes long (128 bytes total). The path consists of the four hashes (noted in blue in Figure 7-5) HL, HIJ, HMNOP and HABCDEFGH. With those four hashes provided as an authentication path, any node can prove that HK (noted in green in the diagram) is included in the merkle root by computing four additional pair-wise hashes HKL, HIJKL, HIJKLMNOP, and the merkle tree root

 - loc 4226 - while the block size increases rapidly, from 4 KB with 16 transactions to

 - loc 4227 - With merkle trees, a node can download just the block headers (80 bytes per block) and still be able to identify a transaction’s inclusion in a block by retrieving a small merkle path from a full node, without storing or transmitting the vast majority of the blockchain, which might be several gigabytes in size.

 - loc 4236 - The SPV node will establish a bloom filter on its connections to peers to limit the transactions received to only those containing addresses of interest. When a peer sees a transaction that matches the bloom filter, it will send that block using a merkleblock message. The merkleblock message contains the block header as well as a merkle path that links the transaction of interest to the merkle root in the block. The SPV node can use this merkle path to connect the transaction to the block and verify that the transaction is included in the block. The SPV node also uses the block header to link the block to the rest of the blockchain.

 - loc 4313 - $ python max_money.py Total BTC to ever be created: 2099999997690000 Satoshis

 - loc 4320 - Many economists argue that a deflationary economy is a disaster that should be avoided at all costs. That is because in a period of rapid deflation, people tend to hoard money instead of spending it, hoping that prices will fall. Such a phenomenon unfolded during Japan’s “Lost Decade,”

 - loc 4323 - Bitcoin experts argue that deflation is not bad per se. Rather, deflation is associated with a collapse in demand because that is the only example of deflation we have to study.

 - loc 4327 - In practice, it has become evident that the hoarding instinct caused by a deflationary currency can be overcome by discounting from vendors, until the discount overcomes the hoarding instinct of the buyer. Because the seller is also motivated to hoard, the discount becomes the equilibrium price at which the two hoarding instincts are matched.

 - loc 4341 - Satoshi Nakamoto’s main invention is the decentralized mechanism for emergent consensus. Emergent, because consensus is not achieved explicitly — there is no election or fixed moment when consensus occurs. Instead, consensus is an emergent artifact of the asynchronous interaction of thousands of independent nodes, all following simple rules.

 - loc 4393 - To miners, receiving a new block means someone else won the competition and they lost. However, the end of one round of a competition is also the beginning of the next round.

 - loc 4412 - This block is called a candidate block because it is not yet a valid block, as it does not contain a valid proof of work.

 - loc 4412 - Jing’s node immediately constructs a new empty block, a candidate for block 277,316. This block is called a candidate block because it is not yet a valid block, as it does not contain a valid proof of work. The block becomes valid only if the miner succeeds in finding a solution to the proof-of-work algorithm. Transaction Age, Fees, and Priority To construct the candidate block, Jing’s bitcoin

 - loc 4413 - block is called a candidate block because it is not yet a valid block, as it does not contain a valid proof of work.

 - loc 4420 - The priority of a transaction is calculated as the sum of the value and age of the inputs divided by the total size of the transaction: Priority = Sum (Value of input * Input Age) / Transaction Size

 - loc 4423 - The age of a UTXO is the number of blocks that have elapsed since the UTXO was recorded on the blockchain,

 - loc 4424 - For a transaction to be considered “high priority,” its priority must be greater than 57,600,000, which corresponds to one bitcoin (100m satoshis), aged one day (144 blocks), in a transaction of 250 bytes total size:

 - loc 4427 - The first 50 kilobytes of transaction space in a block are set aside for high-priority transactions. Jing’s node will fill the first 50 kilobytes, prioritizing the highest priority transactions first, regardless of fee.

 - loc 4430 - Jing’s mining node then fills the rest of the block up to the maximum block size (MAX_BLOCK_SIZE in the code), with transactions that carry at least the minimum fee, prioritizing those with the highest fee per kilobyte of transaction.

 - loc 4438 - Bitcoin transactions do not have an expiration time-out. A transaction that is valid now will be valid in perpetuity.

 - loc 4439 - only as long as it is held in a mining node memory pool. When a mining node is restarted, its memory pool is wiped

 - loc 4440 - because it is a transient non-persistent form of storage. Although a valid transaction might have been propagated across the network, if it is not executed it

 - loc 4440 - When a mining node is restarted, its memory pool is wiped clear, because it is a transient non-persistent form of storage. Although a valid transaction might have been propagated across the network, if it is not executed it

 - loc 4440 - When a mining node is restarted, its memory pool is wiped clear, because it is a transient non-persistent form of storage. Although a valid transaction might have been propagated across the network, if it is not executed it may eventually not reside in the memory pool of any miner.

 - loc 4476 - The first transaction added to the block is a special transaction, called a generation transaction or coinbase transaction. This transaction is constructed by Jing’s node and is his reward for the mining effort. Jing’s node creates the generation transaction as a payment to his own wallet: “Pay Jing’s address 25.09094928 bitcoin.” The total amount of reward that Jing collects for mining a block is the sum of the coinbase reward (25 new bitcoins) and the transaction fees (0.09094928) from all the transactions included in the block

 - loc 4485 - "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff0f03443b0403858402062f503253482fffffffff0110c08d9500000000232102aa970c592640d19de03ff6f329d6fd2eecb023263b9ba5d1b81c29b523da8b21ac00000000", "txid" : "d5ada064c6417ca25c4308bd158c34b77e1c0eca2a73cda16c737e7424afba2f", "version" : 1, "locktime" : 0, "vin" : [ { "coinbase" : "03443b0403858402062f503253482f", "sequence" : 4294967295 } ], "vout" : [ { "value" : 25.09094928, "n" : 0, "scriptPubKey" : { "asm" : "02aa970c592640d19de03ff6f329d6fd2eecb023263b9ba5d1b81c29b523da8b21OP_CHECKSIG", "hex" : "2102aa970c592640d19de03ff6f329d6fd2eecb023263b9ba5d1b81c29b523da8b21ac", "reqSigs" : 1, "type" : "pubkey", "addresses" : [ "1MxTkeEP2PmHSMze5tUZ1hAV3YTKu2Gh1N" ] } } ], "blockhash" : "0000000000000001b6b9a13b095e96db41c4a928b97ef2d944a9b31b2cc7bdc4", "confirmations" : 35566, "time" : 1388185914, "blocktime" : 1388185914 } Unlike

 - loc 4520 - Unlike regular transactions, the generation transaction does not consume (spend) UTXO as inputs. Instead, it has only one input, called the coinbase, which creates bitcoin from nothing.

 - loc 4603 - Generation transactions do not have an unlocking script (a.k.a., scriptSig) field. Instead, this field is replaced by coinbase data, which must be between 2 and 100 bytes. Except for the first few bytes, the rest of the coinbase data can be used by miners in any way they want; it is arbitrary data. In the genesis block, for example, Satoshi Nakamoto added the text “The Times 03/Jan/2009 Chancellor on brink of second bailout for banks” in the coinbase data,

 - loc 4603 - Generation transactions do not have an unlocking script (a.k.a., scriptSig) field. Instead, this field is replaced by coinbase data, which must be between 2 and 100 bytes. Except for the first few bytes, the rest of the coinbase data can be used by miners in any way they want; it is arbitrary data. In the genesis block, for example, Satoshi Nakamoto added the text “The Times 03/Jan/2009 Chancellor on brink of second bailout for banks” in the coinbase data, using it as a proof of the date and to convey a message.

 - loc 4603 - Generation transactions do not have an unlocking script (a.k.a., scriptSig) field. Instead, this field is replaced by coinbase data, which must be between 2 and 100 bytes. Except for the first few bytes, the rest of the coinbase data can be used by miners in any way they want; it is arbitrary data. In the genesis block, for example, Satoshi Nakamoto added the text “The Times 03/Jan/2009 Chancellor on brink of second bailout for banks” in the coinbase data, using it as a proof of the date and to convey a message. Currently, miners use the coinbase data to include extra nonce values and strings identifying the mining pool, as we will see in the following sections.

 - loc 4609 - As per Bitcoin Improvement Proposal 34 (BIP0034), version-2 blocks (blocks with the version field set to 2) must contain the block height index as a script “push” operation in the beginning of the coinbase field.

 - loc 4617 - The next few hexadecimal digits (03858402062) are used to encode an extra nonce (see The Extra Nonce Solution), or random value, used to find a suitable proof of work solution. The final part of the coinbase data (2f503253482f) is the ASCII-encoded string /P2SH/, which indicates that the mining node that mined this block supports the pay-to-script-hash (P2SH) improvement defined in BIP0016. The introduction of the P2SH capability required a “vote” by miners to endorse either BIP0016 or BIP0017. Those endorsing the BIP0016 implementation were to include /P2SH/ in their coinbase data.

 - loc 4617 - The next few hexadecimal digits (03858402062) are used to encode an extra nonce (see The Extra Nonce Solution), or random value, used to find a suitable proof of work solution. The final part of the coinbase data (2f503253482f) is the ASCII-encoded string /P2SH/, which indicates that the mining node that mined this block supports the pay-to-script-hash (P2SH) improvement defined in BIP0016. The introduction of the P2SH capability required a “vote” by miners to endorse either BIP0016 or BIP0017. Those endorsing the BIP0016 implementation were to include /P2SH/ in their coinbase data. Those endorsing the BIP0017 implementation of P2SH were to include the string p2sh/CHV in their coinbase data. The BIP0016 was elected as the winner, and many miners continued including the string /P2SH/ in their coinbase to indicate support for this feature.

 - loc 4720 - With all the other fields filled, the block header is now complete and the process of mining can begin. The goal is now to find a value for the nonce that results in a block header hash that is less than the difficulty target. The mining node will need to test billions or trillions of nonce values before a nonce is found that satisfies the requirement.

 - loc 4720 - With all the other fields filled, the block header is now complete and the process of mining can begin. The goal is now to find a value for the nonce that results in a block header hash that is less than the difficulty target.

 - loc 4784 - The nonce is used to vary the output of a cryptographic function, in this case to vary the SHA256 fingerprint of the phrase.

 - loc 4907 - we saw that the block contains the difficulty target, in a notation called “difficulty bits” or just “bits,” which in block 277,316 has the value of 0x1903a30c. This notation expresses the difficulty target as a coefficient/exponent format, with the first two hexadecimal digits for the exponent and the next six hex digits as the coefficient. In this block, therefore, the exponent is 0x19 and the coefficient is 0x03a30c. The formula to calculate the difficulty target from this representation is: target = coefficient * 2^(8 * (exponent – 3))

 - loc 4932 - Every 2,016 blocks, all nodes retarget the proof-of-work difficulty. The equation for retargeting difficulty measures the time it took to find the last 2,016 blocks and compares that to the expected time of 20,160 minutes (two weeks based upon a desired 10-minute block time). The ratio between the actual timespan and desired timespan is calculated and a corresponding adjustment (up or down) is made to the difficulty.

 - loc 4985 - While the difficulty calibration happens every 2,016 blocks, because of an off-by-one error in the original Bitcoin Core client it is based on the total time of the previous 2,015 blocks (not 2,016 as it should be), resulting in a retargeting bias towards higher difficulty by 0.05%.

 - loc 5045 - Nodes maintain three sets of blocks: those connected to the main blockchain, those that form branches off the main blockchain (secondary chains), and finally, blocks that do not have a known parent in the known chains (orphans). Invalid blocks are rejected as soon as any one of the validation criteria fails and are therefore not included in any chain.

 - loc 5048 - The “main chain” at any time is whichever chain of blocks has the most cumulative difficulty associated with it.

 - loc 5050 - The main chain will also have branches with blocks that are “siblings” to the blocks on the main chain. These blocks are valid but not part of the main chain. They are kept for future reference, in case one of those chains is extended to exceed the main chain in difficulty.

 - loc 5062 - If a valid block is received and no parent is found in the existing chains, that block is considered an “orphan.” Orphan blocks are saved in the orphan block pool where they will stay until their parent is received.

 - loc 5065 - Orphan blocks usually occur when two blocks that were mined within a short time of each other are received in reverse order

 - loc 5073 - Blocks might arrive at different nodes at different times, causing the nodes to have different perspectives of the blockchain. To resolve this, each node always selects and attempts to extend the chain of blocks that represents the most proof of work, also known as the longest chain or greatest cumulative difficulty chain.

 - loc 5073 - Blocks might arrive at different nodes at different times, causing the nodes to have different perspectives of the blockchain. To resolve this, each node always selects and attempts to extend the chain of blocks that represents the most proof of work, also known as the longest chain or greatest cumulative difficulty chain. By summing the difficulty recorded in each block in a chain, a node can calculate the total amount of proof of work that has been expended to create that chain.

 - loc 5139 - Some years the growth has reflected a complete change of technology, such as in 2010 and 2011 when many miners switched from using CPU mining to GPU mining and field programmable gate array (FPGA) mining. In 2013 the introduction of ASIC mining lead to another giant leap in mining power, by placing the SHA256 function directly on silicon chips specialized for the purpose of mining.

 - loc 5139 - Some years the growth has reflected a complete change of technology, such as in 2010 and 2011 when many miners switched from using CPU mining to GPU mining and field programmable gate array (FPGA) mining. In 2013 the introduction of ASIC mining lead to another giant leap in mining power, by placing the SHA256 function directly on silicon chips specialized for the purpose of mining. The first such chips could deliver more mining power in a single box than the entire bitcoin network in 2010.

 - loc 5167 - As difficulty increased, miners often cycled through all 4 billion values of the nonce without finding a block. However, this was easily resolved by updating the block timestamp to account for the elapsed time. Because the timestamp is part of the header, the change would allow miners to iterate through the values of the nonce again with different results. Once mining hardware exceeded 4 GH/sec, however, this approach became increasingly difficult

 - loc 5167 - As difficulty increased, miners often cycled through all 4 billion values of the nonce without finding a block. However, this was easily resolved by updating the block timestamp to account for the elapsed time. Because the timestamp is part of the header, the change would allow miners to iterate through the values of the nonce again with different results. Once mining hardware exceeded 4 GH/sec, however, this approach became increasingly difficult because the nonce values were exhausted in less than a second. As ASIC mining equipment started pushing and

 - loc 5173 - The solution was to use the coinbase transaction as a source of extra nonce values. Because the coinbase script can store between 2 and 100 bytes of data, miners started using that space as extra nonce space, allowing them to explore a much larger range of block header values to find valid blocks.

 - loc 5183 - Even the fastest consumer ASIC mining system cannot keep up with commercial systems that stack tens of thousands of these chips in giant warehouses near hydro-electric power stations. Miners now collaborate to form mining pools, pooling their hashing power and sharing the reward among thousands of participants. By participating in a pool, miners get a smaller share of the overall reward, but typically get rewarded every day, reducing uncertainty.

 - loc 5213 - By setting a lower difficulty for earning shares, the pool measures the amount of work done by each miner. Each time a pool miner finds a block header hash that is less than the pool difficulty, she proves she has done the hashing work to find that result. More importantly, the work to find shares contributes, in a statistically measurable way, to the overall effort to find a hash lower than the bitcoin network’s target.

 - loc 5228 - Most mining pools are “managed,” meaning that there is a company or individual running a pool server. The owner of the pool server is called the pool operator, and he charges pool miners a percentage fee of the earnings.

 - loc 5230 - The pool server runs specialized software and a pool-mining protocol that coordinates the activities of the pool miners. The pool server is also connected to one or more full bitcoin nodes and has direct access to a full copy of the blockchain database. This allows the pool server to validate blocks and transactions on behalf of the pool miners, relieving them of the burden of running a full node.

 - loc 5246 - centralized pool servers represent a single-point-of-failure. If the pool server is down or is slowed by a

 - loc 5246 - centralized pool servers represent a single-point-of-failure. If the pool server is down or is slowed by a denial-of-service attack, the pool miners cannot mine.

 - loc 5246 - centralized pool servers represent a single-point-of-failure. If the pool server is down or is slowed by a denial-of-service attack, the pool miners cannot mine. In 2011, to resolve these issues of centralization, a new pool mining method was proposed and implemented: P2Pool is a peer-to-peer mining pool, without a central operator. P2Pool works by decentralizing the functions of the pool server, implementing a parallel blockchain-like system called a share chain. A share chain is a blockchain running at a lower difficulty than the bitcoin

 - loc 5247 - P2Pool is a peer-to-peer mining pool, without a central operator. P2Pool works by decentralizing the functions of the pool server, implementing a parallel blockchain-like system called a share chain. A share chain is a blockchain running at a lower difficulty than the bitcoin blockchain.

 - loc 5247 - P2Pool is a peer-to-peer mining pool, without a central operator. P2Pool works by decentralizing the functions of the pool server, implementing a parallel blockchain-like system called a share chain. A share chain is a blockchain running at a lower difficulty than the bitcoin blockchain. The share chain allows pool miners to collaborate in a decentralized pool, by mining shares on the share chain at a rate of one share block every 30 seconds. Each of the blocks on the share chain records a proportionate share reward for the pool miners who contribute work, carrying the shares forward from the previous share block. When one of the share blocks also achieves the difficulty target of the bitcoin network, it is propagated and included on the bitcoin blockchain, rewarding all the pool miners who contributed to all the shares that preceded the winning share block.

 - loc 5256 - P2Pool mining is more complex than pool mining because it requires that the pool miners run a dedicated computer with enough disk space, memory, and Internet bandwidth to support a full bitcoin node and the P2Pool node software.

 - loc 5264 - Even though P2Pool reduces the concentration of power by mining pool operators, it is conceivably vulnerable to 51% attacks against the share chain itself. A much broader adoption of P2Pool does not solve the 51% attack problem for bitcoin itself. Rather, P2Pool makes bitcoin more robust overall, as part of a diversified mining ecosystem.

 - loc 5275 - A consensus attack cannot steal bitcoins, spend bitcoins without signatures, redirect bitcoins, or otherwise change past transactions or ownership records. Consensus attacks can only affect the most recent blocks and cause denial-of-service disruptions on the creation of future blocks.

 - loc 5277 - One attack scenario against the consensus mechanism is called the “51% attack.” In this scenario a group of miners, controlling a majority (51%) of the total network’s hashing power, collude to attack bitcoin. With the ability to mine the majority of the blocks, the attacking miners can cause deliberate “forks” in the blockchain and double-spend transactions or execute denial-of-service attacks against specific transactions or addresses. A fork/double-spend attack is one where the attacker causes previously confirmed blocks to be invalidated by forking below them and re-converging on an alternate chain.

 - loc 5321 - There is no possible way for a solo miner to control more than a small percentage of the total mining power. However, the centralization of control caused by mining pools has introduced the risk of for-profit attacks by a mining pool operator.

 - loc 5366 - Meta coins and meta chains are software layers implemented on top of bitcoin, either implementing a currency-inside-a-currency, or a platform/protocol overlay inside the bitcoin system.

 - loc 5371 - Since the introduction of the OP_RETURN transaction scripting opcode, the meta coins have been able to record metadata more directly in the blockchain, and most are migrating to using that instead.

 - loc 5374 - Colored coins is a meta protocol that overlays information on small amounts of bitcoin. A “colored” coin is an amount of bitcoin repurposed to express another asset.

 - loc 5383 - It is entirely up to the users of colored coins to assign and interpret the meaning of the “color” associated with specific coins. To color the coins, the user defines the associated metadata, such as the type of issuance, whether it can be subdivided into smaller units, a symbol and description, and other related information. Once colored, these coins can be bought and sold, subdivided, and aggregated, and receive dividend payments. The colored coins can also be “uncolored” by removing the special association and redeemed for their face value in bitcoin.

 - loc 5415 - Think of Mastercoin as an application-layer protocol on top of bitcoin’s financial transaction transport layer, just like HTTP runs on top of TCP.

 - loc 5422 - Counterparty is another protocol layer implemented on top of bitcoin. Counterparty enables user currencies, tradable tokens, financial instruments, decentralized asset exchanges, and other features. Counterparty is implemented primarily using the OP_RETURN operator in bitcoin’s scripting language to record metadata that enhances bitcoin transactions with additional meaning.

 - loc 5435 - Tenebrix was the first cryptocurrency to implement an alternative proof-of-work algorithm, namely scrypt, an algorithm originally designed for password stretching (brute-force resistance). The stated goal of Tenebrix was to make a coin that was resistant to mining with

 - loc 5435 - Tenebrix was the first cryptocurrency to implement an alternative proof-of-work algorithm, namely scrypt, an algorithm originally designed for password stretching (brute-force resistance). The stated goal of Tenebrix was to make a coin that was resistant to mining with GPUs and ASICs, by using a memory-intensive algorithm.

 - loc 5439 - Litecoin, in addition to using scrypt as the proof-of-work algorithm, also implemented a faster block-generation time, targeted at 2.5 minutes instead of bitcoin’s 10 minutes. The resulting currency is touted as “silver to bitcoin’s gold” and is intended as a light-weight alternative currency. Due to the faster confirmation time and the 84 million total currency limit, many adherents of Litecoin believe it is better suited for retail transactions than bitcoin.

 - loc 5443 - Litecoin.By 2013, there were 20 alt coins vying for position in the market. By the end of 2013, this number had exploded to 200, with 2013 quickly becoming the “year of the alt coins.”

 - loc 5443 - Alt coins continued to proliferate in 2011 and 2012, either based on bitcoin or on Litecoin.By 2013, there were 20 alt coins vying for position in the market. By the end of 2013, this number had exploded to 200, with 2013 quickly becoming the “year of the alt coins.”

 - loc 5485 - Freicoin was introduced in July 2012. It is a demurrage currency, meaning it has a negative interest rate for stored value. Value stored in Freicoin is assessed a 4.5% APR fee, to encourage consumption and discourage hoarding of money.

 - loc 5497 - 2013, we saw the invention of an alternative to proof of work, called proof of stake, which forms the basis of many modern alt coins. Proof of stake is a system by which existing owners of a currency can “stake” currency as interest-bearing collateral. Somewhat like a certificate of deposit (CD), participants can reserve a portion of their currency holdings, while earning an investment return in the form of new currency (issued as interest payments) and transaction fees.

 - loc 5502 - Peercoin was introduced in August 2012 and is the first alt coin to use a hybrid proof-of-work and proof-of-stake algorithm to issue new currency.

 - loc 5507 - Myriad was introduced in February 2014 and is notable because it uses five different proof-of-work algorithms (SHA256d, Scrypt, Qubit, Skein, or Myriad-Groestl) simultaneously, with difficulty varying for each algorithm depending on miner participation. The intent is to make Myriad immune to ASIC specialization and centralization as well as much more resistant to consensus attacks, because multiple mining algorithms would have to be attacked simultaneously.

 - loc 5538 - Primecoin was announced in July 2013. Its proof-of-work algorithm searches for prime numbers, computing Cunningham and bi-twin prime chains.

 - loc 5710 - If you want to leverage Bitcoin’s security, you need to ensure

 - loc 5711 - In simple terms: don’t take control of keys away from users and don’t take transactions off the blockchain.

 - loc 5725 - Traditional security architecture is based upon a concept called the root of trust, which is a trusted core used as the foundation for the security of the overall system or application.

 - loc 5731 - This security architecture is repeated at different scales, first establishing a root of trust within the hardware of a single system, then extending that root of trust through the operating system to higher-level system services, and finally across many servers layered in concentric circles of diminishing trust.

 - loc 5735 - Bitcoin systems can and should use the blockchain as their root of trust.

 - loc 5753 - The level of computer maintenance required to keep a computer virus-free and trojan-free is beyond the skill level of all but a tiny minority of computer users.

 - loc 5773 - I personally keep the vast majority of my bitcoins (99% or more) stored on paper wallets, encrypted with BIP0038, with multiple copies locked in safes.

 - loc 5773 - I personally keep the vast majority of my bitcoins (99% or more) stored on paper wallets, encrypted with BIP0038, with multiple copies locked in safes. Keeping bitcoin offline is called cold storage and it is one of the most effective security techniques. A cold storage system is one where the keys are generated on an offline system (one never connected to the Internet) and stored offline either on paper or on digital media, such as a USB memory stick.

 - loc 5779 - Without general-purpose software to compromise and with limited interfaces, hardware wallets can deliver an almost foolproof level of security to nonexpert users. I expect to see hardware wallets become the predominant method of bitcoin storage. For an example of such a hardware wallet, see the Trezor

 - loc 5785 - In July of 2011, a well-known bitcoin awareness and education project lost almost 7,000 bitcoins. In their effort to prevent theft, the owners had implemented a complex series of encrypted backups. In the end they accidentally lost the encryption keys, making the backups worthless and losing a fortune. Like hiding money by burying it in the desert, if you secure your bitcoin too well you might not be able to find it again.

 - loc 5795 - Whenever a company or individual stores large amounts of bitcoin, they should consider using a multi-signature bitcoin address.

 - loc 5798 - Multi-signature addresses can also offer redundancy, where a single person holds several keys that are stored in different locations.

