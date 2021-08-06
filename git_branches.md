# Git branches

## VS Code extensions

Install [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens).

## 1.0 Creation

### 1.1 Display existing branches

#### Local only

```commandline
git branch
```

```commandline
* main
(END)
```

#### Local and remote branches

```commandline
git branch -a
```

```commandline
* main
  remotes/arwhyte/HEAD -> arwhyte/main
  remotes/arwhyte/main
  remotes/umsi-arwhyte/main
(END)
```

:bulb: Press "Q" key to quit display.

### 1.2 Create and checkout a branch

#### Create branch

Command: `git branch < name >`

```commandline
git branch git_branches
```

```commandline
git branch

```

```commandline
* git_branches
  main
(END)
```