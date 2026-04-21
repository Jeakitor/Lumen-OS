# Testing
*Please note that the following tests were conducted on my own Arch Linux build as a tester for the basic installer program*
## Test 1: Hardware Detection
**Input:** Run installer on target machine  
**Expected:** CPU, architecture, and RAM are displayed  
**Result:** Pass  
**Evidence:** 

<img width="700" height="268" alt="image" src="https://github.com/user-attachments/assets/a56ef99d-7bb3-4702-ad97-68fd6b49c806" />

--- 

## Test 2: Profile Selection
**Input:** Choose Minimal  
**Expected:** No DE/apps selected  
**Result:** Pass  
**Evidence:** 

<img width="691" height="316" alt="image" src="https://github.com/user-attachments/assets/2b39ecd6-0da8-426e-8fe1-ab9e00da6c85" />


---

## Test 3: Timezone Validation
**Input:** Invalid timezone → then valid  
**Expected:** Re-prompt until valid  
**Result:** Pass  
**Evidence:**

<img width="319" height="493" alt="image" src="https://github.com/user-attachments/assets/1613ae69-cb39-4691-a2ca-af21b0d8073c" />


---

## Test 4: Keyboard Selection
**Input:** Choose “us”  
**Expected:** Summary shows keyboard = us  
**Result:** Pass

<img width="284" height="166" alt="image" src="https://github.com/user-attachments/assets/3483dae1-1408-4e07-b30a-4f8ab4706393" />

<img width="322" height="210" alt="Screenshot_20260418_121733" src="https://github.com/user-attachments/assets/dbeaed6b-46af-488d-925f-ca0a6771e855" />

---

## Test 5: User Creation
**Input:** Password mismatch once, then correct  
**Expected:** Re-prompt until match  
**Result:** Pass

<img width="332" height="218" alt="image" src="https://github.com/user-attachments/assets/504ce5f5-5d9c-4173-b643-ba52bf3a645a" />


---

## Test 6: Disk Mode
**Input:** Select auto  
**Expected:** “Partitioning disk automatically…” in plan  
**Result:** Pass

<img width="381" height="94" alt="image" src="https://github.com/user-attachments/assets/9ecd3b24-6b0f-4319-a5a2-c1c5e2315f54" />
<img width="334" height="227" alt="image" src="https://github.com/user-attachments/assets/f644c2b0-b974-4405-8d9f-cb4704d63cf2" />


---

## Test 7: Command Preview
**Input:** Any config  
**Expected:** Shows timezone + keyboard + packages  
**Result:** Pass

<img width="653" height="426" alt="image" src="https://github.com/user-attachments/assets/d2d8a843-8c5b-454a-a534-0d84b85fb63e" />

<img width="576" height="317" alt="image" src="https://github.com/user-attachments/assets/97cb8fe8-5642-4d99-9b8f-f07dd7763dcf" />

---

## Test 8: Simulation Mode
**Input:** Simulate  
**Expected:** No real installs run  
**Result:** Pass

<img width="325" height="326" alt="image" src="https://github.com/user-attachments/assets/c3aa0d0d-deb2-4867-977b-53ea8703c657" />

---

## Test 9: Execution Mode
**Input:** Execute (safe app like vlc)  
**Expected:** Command runs successfully  
**Result:** Pass

<img width="544" height="147" alt="image" src="https://github.com/user-attachments/assets/413946ca-4327-4c53-9c09-2d46a2747e4c" />
**Note:** The installation process was manually stopped after command execution began in order to prevent unintended changes to the system. However, the successful initiation of command execution confirms that the system correctly transitions from simulation mode to execution mode.

---

## Test 10: Usability
**Input:** Non-technical user follows prompts  
**Expected:** Can complete flow without CLI knowledge  
**Result:** Pass

