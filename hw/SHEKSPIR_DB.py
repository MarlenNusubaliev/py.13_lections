# 1 SELECT plaintext, occurences FROM wordform  ORDER BY occurences DESC LIMIT 10;


# 2 shekspir_bd=# SELECT title FROM work WHERE work.genretype = 'a';
#  title 
# -------
# (0 rows)


# 5 shekspir_bd=# SELECT title FROM work WHERE (SELECT AVG(totalwords)FROM work) < totalwords;


# 6

'''
SELECT c1.charname, c1.speechcount, w.title
FROM character c1
JOIN character_work c2 ON c2.charid = c1.charid 
JOIN work w ON c2.workid = w.workid;

'''
'''
                charname                 | speechcount |           title           
------------------------------------------+-------------+---------------------------
 First Apparition                         |           1 | Macbeth
 First Citizen                            |           3 | Romeo and Juliet
 First Conspirator                        |           3 | Coriolanus
 First Gentleman                          |           1 | Othello
 First Goth                               |           4 | Titus Andronicus
 First Murderer                           |          21 | Macbeth
 First Musician                           |           5 | Othello
 First Musician                           |          10 | Romeo and Juliet
 First Officer                            |           3 | Othello
 First Player                             |           8 | Hamlet
 First Senator                            |          33 | Coriolanus
'''


# 7
'''
SELECT AVG(c1.speechcount)
FROM character c1
JOIN character_work c2 ON c1.charid = c2.charid
JOIN work w ON c2.workid = w.workid
WHERE w.title = 'Romeo and Juliet';

'''

'''
25.5454545454545455
(1 row)

'''


# 8.
'''
select count(plaintext)+ count(phonetictext)+ count(stemtext) as total  from paragraph  ;
 total  
--------
 106395
(1 row)

'''

# 9
'''select charname, speechcount from character where speechcount > 15 and speechcount < 30;'''


# 10
'''select year from work where work.year >= 1601 and work.year <= 1700;'''

# 11
'''select longtitle from work where longtitle ilike '%the%';'''

# 12
'''select distinct paragraph from paragraph ;'''

# 13
'''select id1.chapterid, id1.description, w.title
from chapter id1
join work w on id1.workid = w.workid;
'''


# 14
'''
SELECT p.paragraphnum, ch.charname, ch.speechcount
FROM paragraph p
JOIN character ch ON p.charid = ch.charid;
'''


# 15
'''
SELECT p.paragraphnum, w.title, w.year
FROM paragraph p
JOIN work w ON p.workid = w.workid;
'''

# =======================================================
# 1
'''
SELECT source, totalparagraphs FROM work WHERE work.source = 'Moby' and work.totalparagraphs < 100;
 source | totalparagraphs 
--------+-----------------
 Moby   |              47
 Moby   |              43
 Moby   |              19
(3 rows)

'''

# 2

'''
SELECT DISTINCT w.title, sum( ch.chapter) 
FROM chapter ch
JOIN work w ON ch.workid = w.workid GROUP BY w.title;
           title           |  sum  
---------------------------+-------
 Henry VI, Part II         |    87
 Antony and Cleopatra      |   257
 Henry IV, Part II         |    50
 Merry Wives of Windsor    |    67
 Much Ado about Nothing    |    40
 Pericles                  |    62
 King John                 |    46
 Sonnets                   | 11935
 Lover's Complaint         |     1
 Comedy of Errors          |    20
 Romeo and Juliet          |    73
 Henry VIII                |    41
 Timon of Athens           |    43
 Merchant of Venice        |    70
 Measure for Measure       |    45
 All's Well That Ends Well |    70
 Richard II                |    52
 Henry IV, Part I          |    47
 Twelfth Night             |    47
 Cymbeline                 |    89
 As You Like It            |    65
 Henry VI, Part I          |    89
 Coriolanus                |   115
 Titus Andronicus          |    30
 Henry VI, Part III        |   101
 Henry V                   |    81
 King Lear                 |    87
 Troilus and Cressida      |    88
 Phoenix and the Turtle    |     1
 Julius Caesar             |    43
 The Winter's Tale         |    31
 Taming of the Shrew       |    28
 Hamlet                    |    59
 Richard III               |    78
 Rape of Lucrece           |     3
 Venus and Adonis          |     1
 Midsummer Night's Dream   |    13
 Tempest                   |    14
 Passionate Pilgrim        |   231
 Love's Labour's Lost      |    14
 Two Gentlemen of Verona   |    57
 Macbeth                   |   101
 Othello                   |    31
(43 rows)

'''

# 4
'''
SELECT totalparagraphs, title FROM work ; 
 totalparagraphs |           title           
-----------------+---------------------------
            1031 | Twelfth Night
            1025 | All's Well That Ends Well
            1344 | Antony and Cleopatra
             872 | As You Like It
             661 | Comedy of Errors
            1226 | Coriolanus
             971 | Cymbeline
            1275 | Hamlet
             884 | Henry IV, Part I
            1013 | Henry IV, Part II
             846 | Henry V
             772 | Henry VI, Part I
             904 | Henry VI, Part II
             935 | Henry VI, Part III
             779 | Henry VIII
             888 | Julius Caesar
             615 | King John
            1177 | King Lear
              47 | Lover's Complaint
            1120 | Love's Labour's Lost
             758 | Macbeth
             980 | Measure for Measure
             718 | Merchant of Venice
            1161 | Merry Wives of Windsor
             603 | Midsummer Night's Dream
            1059 | Much Ado about Nothing
            1308 | Othello
              43 | Passionate Pilgrim
             748 | Pericles
              19 | Phoenix and the Turtle
             269 | Rape of Lucrece
             628 | Richard II
            1210 | Richard III
             989 | Romeo and Juliet
             154 | Sonnets
             965 | Taming of the Shrew
             698 | Tempest
             865 | Timon of Athens
             654 | Titus Andronicus
            1295 | Troilus and Cressida
             943 | Two Gentlemen of Verona
             201 | Venus and Adonis
             812 | The Winter's Tale
(43 rows)

'''
# 5

'''
SELECT ch.charname, ch.speechcount, w.title, w.genretype, w.year
FROM character ch
JOIN character_work chw ON ch.charid = chw.charid 
JOIN work w ON chw.workid = w.workid WHERE ch.speechcount > 200 ORDER BY w.year DESC;
      charname      | speechcount |         title          | genretype | year 
--------------------+-------------+------------------------+-----------+------
 Poet               |         733 | Lover's Complaint      | p         | 1609
 Poet               |         733 | Sonnets                | s         | 1609
 Timon              |         210 | Timon of Athens        | t         | 1607
 Antony             |         253 | Antony and Cleopatra   | t         | 1606
 Cleopatra          |         204 | Antony and Cleopatra   | t         | 1606
 Iago               |         272 | Othello                | t         | 1604
 Othello            |         274 | Othello                | t         | 1604
 Poet               |         733 | Phoenix and the Turtle | p         | 1601
 Hamlet             |         358 | Hamlet                 | t         | 1600
 Falstaff           |         471 | Merry Wives of Windsor | c         | 1600
 Antony             |         253 | Julius Caesar          | t         | 1599
 Rosalind           |         201 | As You Like It         | c         | 1599
 Falstaff           |         471 | Henry V                | h         | 1598
 Duke of Gloucester |         285 | Henry V                | h         | 1598
 Henry V            |         377 | Henry V                | h         | 1598
 Poet               |         733 | Passionate Pilgrim     | p         | 1598
 Henry V            |         377 | Henry IV, Part I       | h         | 1597
 Henry V            |         377 | Henry IV, Part II      | h         | 1597
 Falstaff           |         471 | Henry IV, Part II      | h         | 1597
 Falstaff           |         471 | Henry IV, Part I       | h         | 1597
 Poet               |         733 | Rape of Lucrece        | p         | 1594
 Poet               |         733 | Venus and Adonis       | p         | 1593
 Duke of Gloucester |         285 | Richard III            | h         | 1592
 Richard III        |         246 | Richard III            | h         | 1592
 Duke of Gloucester |         285 | Henry VI, Part I       | h         | 1591
 Richard III        |         246 | Henry VI, Part III     | h         | 1590
 Duke of Gloucester |         285 | Henry VI, Part II      | h         | 1590
(27 rows)

'''






