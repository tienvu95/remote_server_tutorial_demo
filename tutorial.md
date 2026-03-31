# Step-by-Step Remote Server Tutorial

## 0. Before you start
Have ready:
- your Andrew ID or school username
- server hostname: `TBD_SERVER_HOST`
- authentication method: `TBD`
- VS Code installed
- Git installed
- a terminal app

---

## 1. Connect to the server (TBD, not sure mode of connection)

### Terminal
```bash
ssh YOUR_ANDREW_ID@TBD_SERVER_HOST
```

If SSH config is used:
```bash
ssh myclassserver
```

Example `~/.ssh/config`:
```sshconfig
Host myclassserver
    HostName TBD_SERVER_HOST
    User YOUR_ANDREW_ID
    IdentityFile ~/.ssh/id_ed25519
```

### VS Code
1. Install **Remote - SSH**.
2. Open Command Palette.
3. Choose **Remote-SSH: Connect to Host**.
4. Pick the configured host or enter `YOUR_ANDREW_ID@TBD_SERVER_HOST`.

### Optional: Jupyter tunnel
```bash
ssh -L 8888:localhost:8888 YOUR_ANDREW_ID@TBD_SERVER_HOST
```
Then start Jupyter on the server:
```bash
jupyter notebook --no-browser --port 8888
```
Open `http://localhost:8888` on your laptop.

---

## 2. Create your workspace
```bash
mkdir -p ~/YOUR_ANDREW_ID/tutorial-demo
cd ~/YOUR_ANDREW_ID/tutorial-demo
pwd
ls
```

---

## 3. Clone the repo
If the repo is public:
```bash
git clone https://github.com/tienvu95/remote_server_tutorial_demo.git
cd remote_server_tutorial_demo
```

If students need their own copy, the cleanest workflow is:
1. Fork the repo on GitHub.
2. Clone their fork.
3. Create a new branch.
4. Commit changes.
5. Push the branch.

```bash
git checkout -b my-first-edit
```

Create and edit a text file:
```bash
echo "Hello, this is MY_NAME." > student_notes.txt
cat student_notes.txt
nano student_notes.txt
```

Commit and push:
```bash
git add student_notes.txt
git commit -m "Add student notes"
git push origin my-first-edit
```

---

## 4. Set up a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
which python
pip install -r requirements.txt
```

Why not use one shared environment?
- package versions may conflict
- one student's install can break another's work
- isolated environments make projects reproducible

---

## 5. Run code
### Command line
```bash
python hello_remote.py
```

### Jupyter notebook
```bash
jupyter notebook --no-browser --port 8888
```
Open the provided notebook: `remote_demo.ipynb`

---

## 6. Transfer files
### Download from server to local with `scp`
Run on your local machine:
```bash
scp YOUR_ANDREW_ID@TBD_SERVER_HOST:~/YOUR_ANDREW_ID/tutorial-demo/remote_server_tutorial_demo/student_notes.txt .
```

### Upload from local to server with `scp`
```bash
scp sample_local_upload.txt YOUR_ANDREW_ID@TBD_SERVER_HOST:~/YOUR_ANDREW_ID/tutorial-demo/remote_server_tutorial_demo/
```

### `rsync`
Download:
```bash
rsync -avz YOUR_ANDREW_ID@TBD_SERVER_HOST:~/YOUR_ANDREW_ID/tutorial-demo/remote_server_tutorial_demo/student_notes.txt .
```
Upload:
```bash
rsync -avz sample_local_upload.txt YOUR_ANDREW_ID@TBD_SERVER_HOST:~/YOUR_ANDREW_ID/tutorial-demo/remote_server_tutorial_demo/
```

---

## 7. Helpful commands
Check files:
```bash
pwd
ls -lah
cd
mkdir
rm
cp
mv
cat
head
tail
```

Check resource usage:
```bash
htop
```
If `htop` is unavailable:
```bash
top
```

### Run a long job in `tmux`
Start a session:
```bash
tmux new -s demo
```
Run the script:
```bash
python long_job.py
```
Detach:
```bash
Ctrl-b then d
```
List sessions:
```bash
tmux ls
```
Reconnect:
```bash
tmux attach -t demo
```

### Save logs
```bash
python long_job.py > demo.log 2>&1
cat demo.log
```

### Editors
- `nano file.txt` for beginners
- `vim file.txt` if already comfortable

---

## 8. Discussion topics
- What a scheduler like Slurm does
- CPU vs GPU: when each is useful
- Shared-resource etiquette:
  - do not hog compute
  - watch memory and storage
  - protect private data
  - never edit other people's files
