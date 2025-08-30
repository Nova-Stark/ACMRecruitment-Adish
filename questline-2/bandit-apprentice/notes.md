# Bandit tasks 

## Bandit0 
`cat readme`

## Bandit1
`cat ./"-"`

## Bandit2

`cat ./"--spaces in this filename--"`

## Bandit3

`cd inhere`
`ls -a`
`cat ./"...Hiding-From-You"`

## Bandit4

`cd inhere`
`ls -a`
`cat ./"-file07"`

## Bandit5

`cd inhere`
`find inhere -size 1033c`
`cat ./"maybehere07/.file2"`

## Bandit6

`find ./ -user bandit7 -group bandit6 -size 33c`

`cat "/var/lib/dpkg/info/bandit7.password"`

## Bandit7

`cat data.txt | grep "millionth"`

## Bandit8

`sort data.txt | uniq -u`

## Bandit9

`strings data.txt | grep '==='`

## Bandit10

` cat data.txt | base64 -d`
