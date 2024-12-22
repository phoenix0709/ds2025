from gtts import gTTS
import os

part_1 = """Bonjour madame, je m'appelle Lan. Je suis vignt-un ans. Je suis étudiant en dernière année de spécialisation cybersécurité à l'USTH. Je habite à Hanoï, au Vietnam. J'aime écouter de la musique et pendant mon temps libre, mes genres préférés sont la musique country et la musique edm. De plus, j'aime aussi lire des livres, notamment des romans. Pour gagner un complément de revenus, je spécule souvent en bourse. Je parle vietnamien, anglais et français. Ma personnalité est très joyeuse et sociable. Ma famille compte quate personnes : père, mère, petit frère et moi."""

part_2_ex1_ex5 = """J’aime beaucoup écouter de la musique, c’est une vraie passion pour moi. Mon chanteur préféré est Taylor Swift. Je l’admire pour ses paroles profondes et les émotions qu’elle transmet à travers ses chansons. Son style musical est principalement la musique country, mais elle s’est également tournée vers la pop ces dernières années, et j’aime cette évolution. Ses chansons m’aident souvent à me détendre ou à réfléchir, et je me sens connectée à ses histoires.
En ce qui concerne les concerts, je n’ai pas encore eu l’occasion de la voir chanter en direct. J’espère qu’un jour je pourrai y aller, car je suis certaine que l’atmosphère et l’énergie d’un concert live doivent être incroyables.
J’écoute de la musique presque tous les jours, et elle m’accompagne dans beaucoup de moments de ma vie, que ce soit pour travailler, me détendre ou simplement passer un bon moment. La musique country et pop, comme celle de Taylor Swift, est mon genre préféré, car elle m’apporte beaucoup de joie et de motivation."""

part_2_ex12 = """Pour aller à l’université, j’utilise souvent en bus ou ma moto, selon les horaires et ma disponibilité. Heureusement, mon université n’est pas trop loin de chez moi, donc le trajet est assez pratique. En général, cela me prend environ vingt à trente minutes pour y arriver.
Dans ma vie quotidienne, je me déplace principalement à moto, car c’est rapide et flexible, surtout quand j’ai besoin de circuler en ville. Parfois, je prends aussi le bus, surtout lorsque je veux éviter les embouteillages ou lorsque je préfère économiser de l’essence. Pendant le week-end, je pars à moto pour rentrer chez moi à la campagne et passer du temps avec ma famille."""

audio_files = {
    "part_1.mp3": part_1,
    "part_2_1+5.mp3": part_2_ex1_ex5,
    "part_2_12.mp3": part_2_ex12
}

for filename, text in audio_files.items():
    tts = gTTS(text, lang='fr')
    tts.save(filename)
