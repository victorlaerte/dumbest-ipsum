# coding=utf-8

import sublime
import sublime_plugin
import random
import re

class DumbestIpsumCommand(sublime_plugin.TextCommand):

    s1 = "dilma"
    s2 = "dilmes"
    s3 = "trump"

    def run(self, edit, qty=1, person="dilma"):

        #sel() returns an iterable RegionSet
        selections = self.view.sel()
        for selection in selections:

            dilmaPhrases = [u"Eu, para ir, eu faço uma escala. Para voltar, eu faço duas, para voltar para o Brasil. Neste caso agora nós tínhamos uma discussão. Eu tinha que sair de Zurique, podia ir para Boston, ou pra Boston, até porque... vocês vão perguntar, mas é mais longe? Não é não, a Terra é curva, viu?",
                        u"É interessante que muitas vezes no Brasil, você é, como diz o povo brasileiro, muitas vezes você é criticado por ter o cachorro e, outras vezes, por não ter o mesmo cachorro. Esta é uma crítica interessante que acontece no Brasil",
                        u"E nós criamos um programa que eu queria falar para vocês, que é o Ciência sem Fronteiras. Por que eu queria falar do Ciência sem Fronteiras para vocês? É que em todas as demais... porque nós vamos fazer agora o Ciência sem Fronteiras 2. O 1 é o 100 000, mas vai ter de continuar fazendo Ciência sem Fronteiras no Brasil",
                        u"Eu dou dinheiro pra minha filha. Eu dou dinheiro pra ela viajar, então é... é... Já vivi muito sem dinheiro, já vivi muito com dinheiro. -Jornalista: Coloca esse dinheiro na poupança que a senhora ganha R$10 mil por mês. -Dilma: O que que é R$10 mil?",
                        u"A única área que eu acho, que vai exigir muita atenção nossa, e aí eu já aventei a hipótese de até criar um ministério. É na área de... Na área... Eu diria assim, como uma espécie de analogia com o que acontece na área agrícola.",
                        u"Primeiro eu queria cumprimentar os internautas. -Oi Internautas! Depois dizer que o meio ambiente é sem dúvida nenhuma uma ameaça ao desenvolvimento sustentável. E isso significa que é uma ameaça pro futuro do nosso planeta e dos nossos países. O desemprego beira 20%, ou seja, 1 em cada 4 portugueses.",
                        u"Se hoje é o dia das crianças... Ontem eu disse: o dia da criança é o dia da mãe, dos pais, das professoras, mas também é o dia dos animais, sempre que você olha uma criança, há sempre uma figura oculta, que é um cachorro atrás. O que é algo muito importante!",
                        u"Todos as descrições das pessoas são sobre a humanidade do atendimento, a pessoa pega no pulso, examina, olha com carinho. Então eu acho que vai ter outra coisa, que os médicos cubanos trouxeram pro brasil, um alto grau de humanidade.",
                        u"No meu xinélo da humildade eu gostaria muito de ver o Neymar e o Ganso. Por que eu acho que.... 11 entre 10 brasileiros gostariam. Você veja, eu já vi, parei de ver. Voltei a ver, e acho que o Neymar e o Ganso têm essa capacidade de fazer a gente olhar.",
                        u"A população ela precisa da Zona Franca de Manaus, porque na Zona franca de Manaus, não é uma zona de exportação, é uma zona para o Brasil. Portanto ela tem um objetivo, ela evita o desmatamento, que é altamente lucravito. Derrubar arvores da natureza é muito lucrativo!",
                        u"Ai você fala o seguinte: \"- Mas vocês acabaram isso?\" Vou te falar: -\"Não, está em andamento!\" Tem obras que \"vai\" durar pra depois de 2010. Agora, por isso, nós já não desenhamos, não começamos a fazer projeto do que nós \"podêmo fazê\"? 11, 12, 13, 14... Por que é que não?"
                        u"Eu queria destacar uma questão, que é uma questão que está afetando o Brasil inteiro, que é a questão da vigilância sanitária: gente, é o vírus Aedes aegypti, com as suas diferentes modalidades: chikungunya, zika vírus."];

            trumpPhrases = [u"You know, it really doesn’t matter what the media write as long as you’ve got a young and beautiful piece of ass.",
                        u"The concept of global warming was created by and for the Chinese in order to make U.S. manufacturing non-competitive.",
                        u"Listen you mother fuckers, we're going to tax you 25 percent!",
                        u"When was the last time anybody saw us beating, let's say, China in a trade deal? They kill us. I beat China all the time. All the time.",
                        u"The U.S. will invite El Chapo, the Mexican drug lord who just escaped prison, to become a U.S. citizen because our leaders can't say no!",
                        u"I will build a great wall — and nobody builds walls better than me, believe me —and I’ll build them very inexpensively. I will build a great, great wall on our southern border, and I will make Mexico pay for that wall. Mark my words.",
                        u"The wall will go up and Mexico will start behaving.",
                        u"Laziness is a trait in the blacks. ... Black guys counting my money! I hate it.",
                        u"The only kind of people I want counting my money are little short guys that wear yamakas every day.",
                        u"If you can’t get rich dealing with politicians, there’s something wrong with you.",
                        u"A certificate of live birth is not the same thing by any stretch of the imagination as a birth certificate.",
                        u"He's not a war hero. He's a war hero because he was captured. I like people that weren't captured, OK, I hate to tell you.",
                        u"One of the key problems today is that politics is such a disgrace. Good people don’t go into government."];

            personality = {"dilma" : dilmaPhrases, "trump" : trumpPhrases};

            text = "";
            chose = []
            phrases = personality[person];

            from random import randint
            for i in list(range(0, qty)):

                if i > 0: text += "\n"

                r = randint(0, len(phrases) - 1)
                while r in chose: r = randint(0, len(phrases) - 1)

                text += phrases[r]
                chose.append(r)

            r1 = sublime.Region(selection.begin() - len(self.s1), selection.begin())
            r2 = sublime.Region(selection.begin() - len(self.s2), selection.begin())
            r3 = sublime.Region(selection.begin() - len(self.s3), selection.begin())

            if self.view.substr(r1).lower() == 'dilma':
                self.view.erase(edit, r1)
                selection = sublime.Region(r1.begin())
            elif self.view.substr(r2).lower() == 'dilmes':
                self.view.erase(edit, r2)
                selection = sublime.Region(r2.begin())
            elif self.view.substr(r3).lower() == 'trump':
                self.view.erase(edit, r3)
                selection = sublime.Region(r3.begin())
            else:
                text += "\n"
                self.view.erase(edit, selection)

            # insert text before current cursor position
            self.view.insert(edit, selection.begin(), text)
