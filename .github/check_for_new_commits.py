import git
import os


def check_for_new_commits():
    # Clone the remote repository
    repo = git.Repo("neomega_kernel")
    # Fetch latest changes
    origin = repo.remote(name="origin")
    origin.fetch()
    # 检测是否本地有 commit 文件
    if os.path.exists("commit"):
        with open("commit", "r", encoding="utf-8") as f:
            local_commit = f.read()
    else:
        local_commit = ""
    remote_commit = origin.refs.main.commit

    if local_commit != remote_commit:
        print("New commits found in the remote repository!")
        print("Local commit:", local_commit)
        print("Remote commit:", remote_commit)
        with open("commit", "w", encoding="utf-8") as f:
            f.write(remote_commit)
        with open("new_commits.txt", "w") as f:
            f.write("true")
    else:
        print("No new commits found in the remote repository.")
        with open("new_commits.txt", "w") as f:
            f.write("false")


if __name__ == "__main__":
    check_for_new_commits()
