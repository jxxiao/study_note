<!--
 * @Author: jxxiao
 * @Date: 2019-07-10 00:45:40
 * @LastEditTime: 2019-11-19 20:58:43
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /study_note/git/2.远程分支.md
 -->
# 本地分支

## 1.1 创建仓库

```shell
git init
git add
git commit -m " "
```

init把当前文件夹变成一个git仓库
add 把文件添加到暂存区，
commit 把文件存进仓库。

git分为两个步骤，先把修改的文件夹通过add添加到暂存区，再commit提交。

## 1.2 我后悔了，git checkout和git reset

git这么多步骤，走到中间某一步我后悔了怎么办？
首先在不同的步骤后悔，操作都不一样，所以要记好了。

```shell
git checkout -- file #撤销文件修改
git reset HEAD <file> #撤销add
git reset --hard HEAD^ #撤销commit，HEAD^指上一个版本
```

另外为了回退到上一个版本，我们可能需要查看历史和历史命令，命令如下。

```shell
git log
git reflog
```

## 1.3 我删错了

有时候我们需要删除某个文件，我们可以通过下列命令：

```shell
git rm file
git commit -m ""
```

额，我一不小删错了怎么办？？？？

可以通过

```shell
git checkout -- file
```

checkout的本质是用上一次commit的文件替换掉工作区里的。

## 1.4 管理分支

这一部分是大招了啊。这里我们还会用checkout，但是注意没有“--”了。

假设我们的项目完成了一个1.0版本的，保存在版本库中，现在我要开始开发2.0版本了。这个开发过程是漫长的，我不可能完成一小部分就commit一次，这样我们的项目在我们开发2.0版本的时候就黄了。我们只有彻底完成了2.0版本，才会把他保存过去。这个时候就是分支branch的用处了。

我们先通过

```shell
git branch dev #创建dev分支
git checkout dev #转换到dev分支

git checkout -b dev #相当于上面的两条命令
```

创建了一个dev分支，他和原来的master分支是平行的，我们在dev上开发2.0版本，这样别人就可以在master上继续使用1.0版本。

某一天我们的2.0版本完成了，我就可以把dev分支合并到master分支上，通过下列命令完成。

```shell
git merge dev #把dev合并到master
git branch -d dev #记得把dev删除
```

# 2. 远程分支

初学git的小伙伴对于 git init ，git add, git commit,git reset这些命令肯定已经很熟悉了，但是很对于远程仓库等等还不够了解，我们这里就来讲一讲远程仓库的问题。

1.1 1.2 实际上就是廖雪峰git教程远程仓库内容。

## 2.1 创建一个远程仓库

首先，我们的本地肯定是有一个我们的仓库的，然后在github上创建一个仓库，（廖雪峰的教程有，就不细说了）。现在我们想把这两个仓库连起来，并把本地仓库传上去。

首先连起来：

```shell
git remote add origin https://github.com/jxxiao/learngit.git
```

origin是远程仓库的名字，后面是链接地址，这些东西其实在创建完github仓库都会显示的。实际上这里我们还没有把两个仓库连接，我们只是制定了远程仓库的位置。

接下来把本地仓库内容传上去：

```shell
git push -u origin master
```

-u的目的就是为了把两个仓库连接起来，后面的就是把master传到远程的origin上去，实际上应该叫origin/master。

之后我们修改完仓库就可以直接

```shell
git push origin master
```

## 2.2 远程仓库克隆

通过下列命令，我们可以把一个仓库克隆到本地。

```shell
git clone https://github.com/jxxiao/learngit.git
```

## 2.3 git fetch和git pull

### git fetch

1.git fetch不会改变本地仓库状态。也就是**不会更新master分支，不会修改本地磁盘上的文件**。git fetch就是一个单纯的下载操作。
2. 远程分支下载下来后，需要合并到本地分支，可以通过使用下列命令：

```shell
git cherry-pick o/master
git rebase o/master
git merge o/master
```

由于很多人要下载合并所以有了git pull。

### git pull

git pull 就是 git fetch + git merge o/master

但是经常会遇到一个问题，就是远程仓库版本是a，我pull下a，之后本地到了b，然而远程的a已经变成c了(可能是你直接打开GitHub修改了之类的)，这个时候想要push，是push不上去的。因为你的push必须要基于a。这个时候需要fetch后merge或者rebase。又一个简单的操作叫git pull -r(git pull --rebase)

## 2.4 git push

```shell
git push <remote> <place>
```

切到本地place分支，再找到remote的place分支，将本地place提交上去。

## 一些常用的

偶尔会不小心把不该push上去的东西push上去了，比如log等,但是希望本地保存这些文件。可以这样做：

```shell
git rm -r --cached dir1
git rm --cached dir2/*.pyc
git commit -m "remove irrelated files"
git push origin branch1
```
