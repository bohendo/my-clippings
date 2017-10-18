
---
#  Penetration Testing
## by Georgia Weidman
---

 - loc 90 - MS08-067 patched an issue in the netapi32. dll that could allow attackers to use a specially crafted remote procedure call request via the Server Message Block (SMB) service to take over a target system. This vulnerability is particularly dangerous because it does not require an attacker to authenticate to the target machine before running the attack.MS08-067 gained eternal infamy as the vulnerability exploited by the Conficker worm, which was widely reported in the media

 - loc 118 - One excellent way to find usernames is by looking for email addresses on the Internet. You might be surprised to find corporate email addresses publicly listed on parent-teacher association contact info, sports team rosters, and, of course, social media. You can use a Python tool called theHarvester to quickly scour thousands of search engine results for possible email addresses. theHarvester can automate searching Google, Bing, PGP, LinkedIn, and others for email addresses

 - loc 120 - Feel free to use Maltego to study other Internet footprints, including your own, your company’s, your high school arch nemesis’s, and so on. Maltego uses information publicly available on the Internet, so it is perfectly legal to do reconnaissance on any entity.

 - loc 124 - After we connected, the SMTP server announced itself as SLMail version 5.5.0.4433.Now, keep in mind that admins can change banners like this to say anything, even sending attackers and pentesters on a wild goose chase, studying vulnerabilities for a product that is not deployed

 - loc 142 - Just as Metasploit evolved from an exploitation framework into a fully fledged penetrationtesting suite with hundreds of modules, Nmap has similarly evolved beyond its original goal of port scanning. The Nmap Scripting Engine (NSE) lets you run publicly available scripts and write your own

 - loc 143 - If you use the -sC flag to tell Nmap to run a script scan in addition to port scanning, it will run all the scripts in the default category

 - loc 144 - The NSE script nfs-ls.nse will connect to NFS and audit shares

 - loc 145 - As you can see, the NSE script found the NFS share /export/georgia u on our Linux target. Of particular interest is the . ssh directory v, which may include sensitive information such as SSH keys and (if public key authentication is allowed on the SSH server) a list of authorized keys

 - loc 146 - Some NSE scripts may crash services or harm the target system, and an entire category is dedicated to denial of service. For example, the script smb-check-vulns will check for the MS08-067 vulnerability and other SMB vulnerabilities. Its help information notes that this script is likely dangerous and shouldn’t be run on production systems unless you are prepared for the server to go down

 - loc 147 - Some Metasploit exploits include a check function that connects to a target to see if it is vulnerable, rather than attempting to exploit a vulnerability. We can use this command as a kind of ad hoc vulnerability scan, as shown in Listing 6-8.(There’s no need to specify a payload when running check because no exploitation will take place.

 - loc 147 - SLMail version 5.5.0.4433 has a known exploitable issue—CVE-2003-0264—so we can find it easily with a quick search in Msfconsole for cve:2003-0264

 - loc 149 - Nikto is a web application vulnerability scanner built into Kali that’s like Nessus for web apps: It looks for issues such as dangerous files, outdated versions, and misconfigurations

 - loc 149 - Nikto thinks that this install is subject to a code execution vulnerability, and further analysis of Open Sourced Vulnerability Database (OSVDB) entry 40478 reveals that this issue has a Metasploit exploit that we can use during exploitation. n o t e OSVDB (http://osvdb.com/) is a vulnerability repository specifically for open source software such as TikiWiki, with detailed information on a wide variety of products

