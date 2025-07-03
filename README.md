# Battlesnake Python Starter Project

An official Battlesnake template written in Python. Get started at [play.battlesnake.com](https://play.battlesnake.com).

![Battlesnake Logo](https://media.battlesnake.com/social/StarterSnakeGitHubRepos_Python.png)

This project is a great starting point for anyone wanting to program their first Battlesnake in Python. It can be run locally or easily deployed to a cloud provider of your choosing. See the [Battlesnake API Docs](https://docs.battlesnake.com/api) for more detail. 

[![Run on Replit](https://repl.it/badge/github/BattlesnakeOfficial/starter-snake-python)](https://replit.com/@Battlesnake/starter-snake-python)

## Technologies Used

This project uses [Python 3](https://www.python.org/) and [Flask](https://flask.palletsprojects.com/). It also comes with an optional [Dockerfile](https://docs.docker.com/engine/reference/builder/) to help with deployment.

## Run Your Battlesnake

Install dependencies using pip

```sh
pip install -r requirements.txt
```

Start your Battlesnake

```sh
python main.py
```

You should see the following output once it is running

```sh
Running your Battlesnake at http://0.0.0.0:8000
 * Serving Flask app 'My Battlesnake'
 * Debug mode: off
```

Open [localhost:8000](http://localhost:8000) in your browser and you should see

```json
{"apiversion":"1","author":"","color":"#888888","head":"default","tail":"default"}
```

## Play a Game Locally

Install the [Battlesnake CLI](https://github.com/BattlesnakeOfficial/rules/tree/main/cli)
* You can [download compiled binaries here](https://github.com/BattlesnakeOfficial/rules/releases)
* or [install as a go package](https://github.com/BattlesnakeOfficial/rules/tree/main/cli#installation) (requires Go 1.18 or higher)

Command to run a local game

```sh
battlesnake play -W 11 -H 11 --name 'Python Starter Project' --url http://localhost:8000 -g solo --browser
```

## Next Steps
\documentclass{article}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{bookmark}
\usepackage{geometry}
\geometry{a4paper, margin=1in}
\usepackage{listings}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage[utf8x]{inputenc}
\usepackage{tcolorbox} 
\usepackage[ngerman]{babel}    
\usepackage{lmodern}           
\usepackage{parskip}     
\usepackage{amsmath, amssymb}  
\usepackage{enumitem}          
\usepackage{float} 
\usepackage{subcaption}
\usepackage{array} 
\usepackage{longtable}
\usepackage{tabularx}
\usepackage{booktabs}



\definecolor{myblue}{RGB}{50,100,200}
\hypersetup{
    colorlinks=true,
    linkcolor=myblue,
    urlcolor=blue
}
 





\lstset{
  basicstyle=\ttfamily\footnotesize,
  keywordstyle=\color{blue},
  commentstyle=\color{gray},
  stringstyle=\color{red},
  breaklines=true,
  frame=single,
  captionpos=b,
  language=Java
}

\title{ \includegraphics[width=2in]{unirostock.jpeg}

\huge{\textbf{KI SS 2025\\Programmier-Projekt. Battlesnake}} }

\author{%
    \textbf{Team-17}
    \\\\Helin Oguz, \ 223202103 
    \\Hüseyin Kayabasi, \   223201801 
    \\Cagla Yesildogan, \ 223201881
    \\Arian Akbari, \ 224100357
    \\Johannes Langer, \ %
}

\date{}

\begin{document}
\maketitle
\section*{1}
\textbf

Wir haben uns für ein \textbf{Sequenzdiagramm} entschieden, da dieses Diagramm den zeitlichen Ablauf der Methodenaufrufe und die Agentenfunktion klar und verständlich darstellt.

Die folgende Abbildung zeigt den Aufruf- und Entscheidungsablauf des Bots:

\begin{itemize}
    \item Der Game Engine ruft die \texttt{move()}-Methode auf.
    \item Die \texttt{move()}-Methode ist die Agentenfunktion, da hier die Entscheidung getroffen wird, in welche Richtung sich die Schlange bewegen soll.
    \item Von \texttt{move()} wird \texttt{minimax()} aufgerufen, um die beste mögliche Bewegung zu berechnen.
    \item Die Methode \texttt{minimax()} ruft dabei mehrere Hilfsmethoden auf:
    \begin{itemize}
        \item \texttt{eval\_state()}: Bewertet die aktuelle Situation.
        \item \texttt{is\_safe()}: Prüft, ob ein Feld sicher ist.
        \item \texttt{is\_head\_collision\_risk()}: Prüft das Risiko einer Head-to-Head-Kollision.
        \item \texttt{get\_neighbors()}: Liefert benachbarte Felder.
        \item \texttt{manhattan\_dist()}: Berechnet die Entfernung zu Zielen (z.B. Nahrung).
    \end{itemize}
\end{itemize}

Die Agentenfunktion ist also die \texttt{move()}-Methode. Diese ist im Sequenzdiagramm klar gekennzeichnet.
\begin{figure}[h] % 'h' burada yerleştirmek için
  \centering
  \includegraphics[width=1.1\textwidth]{seqq.png} % Görselin yolu ve genişliği
  \label{fig:ornek}
\end{figure}
\vspace{1em}
\section*{2}
Unser Bot ist ein \textbf{Goal-Based Agent}. Der Bot hat das Ziel, so lange wie möglich zu überleben. Dabei passt er sein Verhalten dynamisch an:

\begin{itemize}
    \item Bei niedriger Gesundheit priorisiert er das Erreichen von Nahrung.
    \item Wenn die Schlange groß genug ist, konzentriert sie sich auf das Überleben und vermeidet enge Räume.
\end{itemize}

Wir haben uns für dieses Agentenmodell entschieden, weil es in Battlesnake entscheidend ist, flexibel auf die Situation zu reagieren und Ziele situativ zu ändern. Ein reiner Reflex-Agent wäre nicht ausreichend, da komplexere Entscheidungsschritte (z.B. Minimax, Sicherheitsprüfung) benötigt werden.

\vspace{1em}
\section*{3}

Unser Bot verwendet folgende zusätzliche Strategien, die über einfache Bewegungsregeln hinausgehen:

\begin{itemize}
    \item \textbf{Minimax-Algorithmus mit Alpha-Beta-Pruning:} \\
    Der Bot berechnet die möglichen zukünftigen Züge in mehreren Ebenen und versucht, den bestmöglichen Zug zu wählen, indem er potenzielle Gefahren minimiert und Vorteile maximiert. \\
    \textit{Warum?} Dadurch kann der Bot besser planen und frühzeitig riskante Situationen vermeiden.

    \item \textbf{Head-to-Head-Kollisionsvermeidung:} \\
    Der Bot berücksichtigt, ob gegnerische Schlangen in der Nähe sind und vermeidet bewusst Felder, auf die größere oder gleich große Schlangen als nächstes ziehen könnten. \\
    \textit{Warum?} Um unnötige Kopf-an-Kopf-Kollisionen zu vermeiden und das Überleben zu sichern.

    \item \textbf{Dynamische Futter-Priorisierung:} \\
    Der Bot priorisiert das Fressen von Nahrung nur bei niedrigem Gesundheitswert oder kleiner Körpergröße. Ab einer bestimmten Körpergröße ignoriert der Bot bewusst Nahrung und konzentriert sich darauf, in sicheren offenen Bereichen zu bleiben. \\
    \textit{Warum?} Große Schlangen neigen dazu, sich selbst einzukesseln. Die Begrenzung der Körpergröße erhöht die Überlebenschance.
\end{itemize}

Diese Strategien machen den Bot flexibler und deutlich überlebensfähiger im Vergleich zu einfachen Reflex-Agenten.
\section*{4}

Die Umgebung von Battlesnake lässt sich folgendermaßen charakterisieren:

\begin{itemize}
    \item \textbf{Dynamisch:} \\
    Die Umgebung verändert sich ständig durch die Bewegungen der Schlangen und das Erscheinen von Nahrung. Jeder Zug beeinflusst die zukünftige Spielsituation.
    
    \item \textbf{Teilweise beobachtbar (partiell beobachtbar):} \\
    Obwohl das Spielbrett sichtbar ist, sind die zukünftigen Bewegungen der Gegner unbekannt. Man sieht den aktuellen Zustand, aber nicht die zukünftigen Aktionen der anderen Agenten.
    
    \item \textbf{Deterministisch:} \\
    Die Spielregeln sind klar definiert und jede Aktion hat eine eindeutige Folge, ohne Zufallselemente. Wenn man die Züge kennt, kann man das Ergebnis exakt vorhersagen.
    
    \item \textbf{Mehragentensystem:} \\
    Es gibt mehrere Agenten (Schlangen), die unabhängig voneinander agieren und konkurrieren. Die Entscheidungen eines Agenten beeinflussen die anderen.
\end{itemize}

Diese Eigenschaften machen Battlesnake zu einem anspruchsvollen Umfeld für die Entwicklung eines Agenten.  
Man benötigt Strategien, die mit unvollständiger Information und dynamischen Veränderungen umgehen können.

\end{document}
