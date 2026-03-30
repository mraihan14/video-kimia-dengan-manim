from manim import *

class Main_Scene(Scene):
    def construct(self):

        self.add_sound("sound.mp3", time_offset=1)
        #Pembuka
        image = ImageMobject("image.png") #Ganti dengan Image yang sesuai
        image.scale(0.2)
        image.to_edge(LEFT*3)
        box = SurroundingRectangle(image, color=YELLOW, buff=0.08)
        self.play(FadeIn(image))
        self.play(Create(box))

        identity=VGroup(Text("Nama : M. Raihan Pratama",font_size=24),Text("Kelas : XII F1",font_size=24),Text("Asal Sekolah : SMAN 5 Batang Hari",font_size=24)).arrange(DOWN,aligned_edge=LEFT)
        self.play(Write(identity))
        self.wait(9)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)

        title = Text("SOAl No. 40", font_size=36)
        subtitle = Text("Ujian Akhir Kimia SMAN 5 Batang Hari 2025", font_size=30)

        #subtitle.next_to(title, DOWN)

        self.play(Write(title),run_time=1)
        self.wait(0.05)


        self.play(title.animate.scale(0.8).to_edge(UP*6))
        self.play(FadeIn(subtitle),run_time=1)
        self.wait(5)
        self.play(Unwrite(subtitle))
        self.play(title.animate.to_corner(LEFT).to_edge(UP*1.5))
        self.wait(1)
        
        problem = VGroup(
            Text("Senyawa turunan benzena berikut yang dapat digunakan sebagai bahan dasar",font_size=21),
            Text("pewarna tekstil", color=YELLOW,font_size=21),
            Text("adalah…",font_size=21)
        ).arrange(RIGHT)
        self.play(Write(problem))

        self.wait(6)
        self.play(problem.animate.to_edge(UP*6))
        self.wait(2)

        option_a=Text("A. Toluena",font_size=20)
        option_b=Text("B. Asan Benzoat",font_size=20)
        option_c=Text("C. TNT",font_size=20)
        option_d=Text("D. Anilina",font_size=20)
        option_e=Text("E. Fenol",font_size=20)

        #underline = Underline(problem[1])
        #self.play(Create(underline))

        options = VGroup(option_a, option_b, option_c, option_d, option_e)
        options.arrange(DOWN,aligned_edge=LEFT,buff=0.17)
        options.next_to(problem,DOWN,buff=0.5)
        options.to_edge(LEFT*1.8)
        self.play(Write(options,run_time=8))
        self.wait(18) 
        underline = Underline(problem[1])
        self.play(Create(underline))

        # Pemabahasan
        ans_a=Text("Pelarut industri cat, pernis  lem, dan tiner.",font_size=20)
        ans_b=Text("Pengawet makanan dan minuman, serta antibakteri.",font_size=20)
        ans_c=Text("Bahan dasar peledak.",font_size=20)
        ans_d=VGroup(Text("Pewarna tekstil",color=YELLOW,font_size=20),Text("dan bahan dasar parasetamol.",font_size=20)).arrange(RIGHT)
        ans_e=Text("Bahan baku plastik, antiseptik, dan aspirin.",font_size=20)

        answers = VGroup(ans_a, ans_b, ans_c, ans_d, ans_e)
        tme=[6,7,10,7,6]
        for i, (opt, ans) in enumerate(zip(options, answers)):
            triangle = Triangle(fill_opacity=1).set_stroke(width=0)
            self.wait(tme[i])
            triangle.scale_to_fit_height(opt.height * 0.5)
            triangle.rotate(-PI/2)
            triangle.next_to(opt, RIGHT, buff=0.3)
            ans.next_to(triangle, RIGHT, buff=0.4)

            self.play(FadeIn(triangle), run_time=0.3)
            self.play(Write(ans), run_time=2)
            if i==3:
                self.wait(5)
                box = SurroundingRectangle(option_d, color=YELLOW, buff=0.07)
                self.play(Create(box))
        self.wait(6)
        check = Text("✔", color=GREEN)
        check.next_to(answers[3], RIGHT, buff=0.2)
        self.play(Write(check))
        self.wait(7)
        self.play(*[FadeOut(mob) for mob in self.mobjects],run_time=2)