# 🔒🔑 Password Manager 🔑🔒

---

### Stored information:
* **🌐 Domain**
* **👤 Username / 📧 Email**
* **🗝️ Password**   

---
### Features
* **Generate a password** generates a new strong 
  password and copy it  
* **Save** checkbox will store email for next use
* **Show Data** button opens data file 
with stored passwords
  
---  
### Bugs
* **Show Data** button currently working only in **Windows**
  
    ```
    # Line 104
    if platform == "win32":
      show_passwords_button = Button(text="Show Data", width=14, bg=BLUE, command=show_data)
    else:
      show_passwords_button = Button(text="Show Data", width=14, bg=BLUE, state=DISABLED)
    ```  
     
---

### GUI   
   
![](images/gui.png)
