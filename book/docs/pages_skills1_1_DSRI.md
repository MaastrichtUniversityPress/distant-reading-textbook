# Getting Started with JupyterHub on DSRI (DCU4008)

In this course, we will use **Python**, a popular programming language for data analysis, to scrape and clean data from the web. Python is widely used in research and industry due to its simplicity and powerful libraries (collections of reusable code). To run Python code, we use **Jupyter Notebooks**, an interactive and user-friendly environment that combines code, visualizations, and explanatory text in a single document. Students who have completed the BA Digital Society degree at FASoS may already be familiar with Jupyter Notebooks, but even if you have never seen it before, you will quickly learn how to use them. 

We will not teach coding from scratch, so you only need to make minor adjustments to the code provided by the course coordinator. Also, you will not have to install anything on your own machine. Instead of setting up Python and a coding environment locally, you will access a **JupyterHub environment** on Maastricht University's DSRI (Data Science Research Infrastructure). JupyterHub provides a pre-configured workspace for all students, so everyone has the same interface and tools. Each student instance also has 2GB of data storage, but it is important to download your data and backups as soon as possible. DSRI is a working environment and not intended for long-term storage. To access the notebooks needed for the course *Machines of Knowledge*, please follow the steps below:

---

## Step 1 – Install and Connect to the UM VPN

It is your responsibility to install and configure the UM VPN before the course starts. The VPN allows you to connect to the university network remotely, and you will need this when collecting your own research data at home. At Maastricht University, we use the **Cisco AnyConnect VPN client**. Follow the [UM ICT VPN instructions](https://dsri.maastrichtuniversity.nl/docs/guide-vpn/) to set it up.

For VPN support, you can contact **UM ICT** directly:
- **ICT FASoS**: Visit in person by turning left at the reception and walking down the hallway with the red seats. Their office is usually open from 9 am to 4 pm on working days.
- **ICT Central**: Submit a request via the [online ticketing system](https://servicedesk.icts.maastrichtuniversity.nl/tas/public/ssp/) or visit their in-person service desk at the university library in the inner city.

To successfully connect to the VPN client, make sure to select access category **06** (for students) instead of **01** (for staff). Logging in to VPN is a requirement for access to DSRI / JupyterHub.

---

## Step 2 – Access JupyterHub

After connecting to the UM VPN, open your browser and go to the following JupyterHub:[https://machines-of-knowledge-fdcw-history-machines-of-knowledge.apps.dsri2.unimaas.nl/hub/login?next=%2Fhub%2F](https://machines-of-knowledge-fdcw-history-machines-of-knowledge.apps.dsri2.unimaas.nl/hub/login?next=%2Fhub%2F)

Then enter the following access information:
- **Username**: Your student I-number (e.g., `I6000000`). The tool should accept both *I* and *i* before your number.
- **Password**: The shared course password provided by your tutor.

Having one password for all students ensures that tutors and ICT staff can also access your projects when necessary and help with problems.

---

## Step 3 – Launch Your JupyterLab Environment

After logging in, you’ll see the JupyterHub interface with project folders on the left. This may take a minute or two to load. 

---

## Step 4 – Access Course Materials

In the **File Explorer** (left panel), navigate to the `notebooks` folder, which is hidden under `materials`. Here, you’ll find the course scripts, such as the Apple Web Scraper notebook. Double-click a notebook to open and run it.
Use the buttons at the top of the **File Explorer** to upload or download files as needed.

### Storage Reminder

Your instance has 2GB of storage, which is temporary. Download datasets to your local machine immediately after use to avoid data loss. 

---

## Step 5 – Use OpenRefine (Optional)

From the **Launcher** window, you can open **OpenRefine**, a tool for data cleaning and exploration. If you close the Launcher, reopen it via **File > New Launcher**.

---

## Restarting Your Environment

If the environment is inactive after a long period of disuse, the course coordinator may need to restart the pod behind JupyterHub. Contact the course coordinator when you cannot access your project as expected.

---

## Troubleshooting

- **VPN Issues**: Ensure you’re connected to the UM VPN before accessing JupyterHub. Contact **UM ICT Support** if you need help.
- **Login Problems**: Verify your I-number and the shared course password.
- **Missing Files**: Check if you’ve downloaded backups. Storage is not permanent.

---

## Further Reading

For context on data cleaning and preparation:
- Ignatow, G., & Mihalcea, R. (2018). *An introduction to text mining: Research design, data collection, and analysis.* SAGE Publications. https://doi.org/10.4135/9781506336985
- Piotrowski, M. (2012). *Natural language processing for historical texts.* Springer. https://doi.org/10.1007/978-3-031-02146-6
- Schöch, C. (2013). Big? Smart? Clean? Messy? Data in the humanities. *Journal of Digital Humanities*, 2(3). http://journalofdigitalhumanities.org/2-3/big-smart-clean-messy-data-in-the-humanities/

---

Instructions adapted by Monika Renate Barget (2025).

