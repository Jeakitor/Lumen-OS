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
**Evidence:** (show retry)

---

## Test 4: Keyboard Selection
**Input:** Choose “us”  
**Expected:** Summary shows keyboard = us  
**Result:** Pass

---

## Test 5: User Creation
**Input:** Password mismatch once, then correct  
**Expected:** Re-prompt until match  
**Result:** Pass

---

## Test 6: Disk Mode
**Input:** Select auto  
**Expected:** “Partitioning disk automatically…” in plan  
**Result:** Pass

---

## Test 7: Command Preview
**Input:** Any config  
**Expected:** Shows timezone + keyboard + packages  
**Result:** Pass

---

## Test 8: Simulation Mode
**Input:** Simulate  
**Expected:** No real installs run  
**Result:** Pass

---

## Test 9: Execution Mode
**Input:** Execute (safe app like vlc)  
**Expected:** Command runs successfully  
**Result:** Pass

---

## Test 10: Usability
**Input:** Non-technical user follows prompts  
**Expected:** Can complete flow without CLI knowledge  
**Result:** Pass
