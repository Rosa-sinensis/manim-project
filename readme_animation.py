from manim import *
import numpy as np


class scene1(Scene):
    def construct(self):

        text1 = Text("Hello ").rotate(-PI/2)
        text2 = Text("World").rotate(-PI/2).next_to(text1, DOWN)
        text3 = Text("Sorry about that (^-^')").move_to(1.5*UP+RIGHT).scale(0.3)
        group1 = VGroup(text1, text2)
        self.play(FadeIn(group1),run_time=2)
        self.add(text3)  
        self.wait()
        # use for loop to animate text moving up and down
        self.play(
            group1.animate.rotate(PI/2).shift(UP)
        )
        self.remove(text3)
        self.play(
            text1.animate.set_color(BLUE),
            text2.animate.set_color(RED),
        )
        text4 = Text("   Welcome to my personal project. \nIt's for fun. And that's what matters").scale(0.4).next_to(group1, DOWN).move_to(DOWN)
        text5 = Text("(^∇^)b").move_to(UP+1.5*RIGHT).scale(0.3)
        self.play(group1.animate.scale(2))
        self.play(Write(text4))
        self.add(text5)
        self.wait(2)

        # try to implement using for loop
        square1 = Square().to_edge(UP+LEFT).scale(0.5).set_stroke(BLUE_E)
        square2 = Square().to_edge(UP+LEFT).scale(0.5).set_stroke(GREEN_E)
        square3 = Square().to_edge(UP+LEFT).scale(0.5).set_stroke(RED_E)
        square4 = Square().to_edge(UP+LEFT).scale(0.5).set_stroke(YELLOW_E)
        
        self.play(Create(square1))
        self.camera.background_color = BLUE_A
        self.remove(text5)

        self.play(
            Create(square2),
            square1.animate.to_edge(DOWN+LEFT),
        )
        self.camera.background_color = GREEN_A

        self.play(
            Create(square3),
            square1.animate.to_edge(DOWN+RIGHT),
            square2.animate.to_edge(DOWN+LEFT),
        )
        self.camera.background_color = RED_A

        self.play(
            Create(square4),
            square1.animate.to_edge(UP+RIGHT),
            square2.animate.to_edge(DOWN+RIGHT),
            square3.animate.to_edge(DOWN+LEFT),
        )
        self.camera.background_color = YELLOW_A

        self.play(
            square1.animate.to_edge(UP+LEFT),
            square2.animate.to_edge(UP+RIGHT),
            square3.animate.to_edge(DOWN+RIGHT),
            square4.animate.to_edge(DOWN+LEFT),
        )

        # set stroke can be gradient
        group2=VGroup(square1, square2, square3, square4)
        square5 = Square().scale(0.5).set_fill(BLACK, opacity=0.2).set_stroke(BLACK, opacity=0.2)
        circle1 = Circle().set_fill(BLACK, opacity=1).set_stroke(BLACK)

        # add updater, transform not linear, gradient change in circle black opacity
        self.play(Transform(group2, square5))
        self.play(Transform(square5, circle1))
        self.play(circle1.animate.scale(10).set_stroke(YELLOW), run_time=3)


class scene2(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 *DEGREES)
        
        ax = ThreeDAxes(
            x_range=[-10,10],
            y_range=[-10,10],
            z_range=[-10,10]
        )

        curve1 = ParametricFunction(lambda t: np.array([
            t, np.sin(2*t), 0
        ]), color=PINK, t_range=[-TAU, TAU]) 

        curve2 = ParametricFunction(lambda t: np.array([
            np.cos(4.5*t), np.sin(2.4*t), np.cos(2*t)*np.cos(2*t)
        ]), color=BLUE_D, t_range=[-20, 20])

        curve3 = ParametricFunction(lambda t: np.array([
            np.cos(6.5*t), np.sin(4.4*t), 3*np.cos(2.1*t)*np.cos(2.1*t)-1
        ]), color=RED, t_range=[-20, 20])

        curve4 = ParametricFunction(lambda t: np.array([
            np.exp(0.1*t)*np.cos(t), np.exp(-0.1*t)*np.sin(t), 2*t
        ]), color=RED, t_range=[-TAU, TAU])

        curve5 = ParametricFunction(lambda t: np.array([
            5*np.sin(3*t)*np.cos(5*t), np.sin(3*t), np.cos(5*t)
        ]), color=GREEN, t_range=[-TAU, TAU])

        curve6 = ParametricFunction(lambda t: np.array([
            np.exp(0.2*t)*np.cos(5*t), np.exp(0.2*t)*np.sin(5*t), 0.3*t
        ]), t_range=[-TAU, TAU])
        curve6.set_color(color=[RED_C, BLUE_E, PURPLE_E])
    

        self.play(Create(ax), run_time=2)
        self.move_camera(phi=0 * DEGREES, theta=90 *DEGREES, zoom=1.5, run_time=2)

        self.play(
            Create(curve1), run_time=2
            )

        self.move_camera(phi=75 * DEGREES, theta=45 *DEGREES, zoom=1.0)

        self.begin_ambient_camera_rotation(rate=0.8, about='theta')

        self.play(Transform(curve1, curve2), run_time=3)
        self.wait()
        self.remove(curve1)

        self.stop_ambient_camera_rotation(about='theta')
        self.begin_ambient_camera_rotation(rate=0.4, about='theta')

        self.play(Transform(curve2, curve3), run_time=3)
        self.wait(2)
        self.remove(curve2)

        self.play(Transform(curve3, curve4), run_time=3)
        self.remove(curve3)

        self.play(curve4.animate.set_color(BLACK), run_time=1)
        self.remove(curve4)

        self.stop_ambient_camera_rotation(about='theta')
        self.begin_ambient_camera_rotation(rate=0.8, about='theta')
        self.play(
            Create(curve5, run_time=5), 
        )
        self.begin_ambient_camera_rotation(rate=0.4, about='phi')
        self.wait(1.5)
        self.stop_ambient_camera_rotation(about='phi')
        self.wait(3)
        self.stop_ambient_camera_rotation(about='theta')   
        self.begin_ambient_camera_rotation(rate=0.3, about='theta')
        self.play(Transform(curve5, curve6), run_time=3)
        self.stop_ambient_camera_rotation(about='theta')
        self.wait(1)
        self.begin_ambient_camera_rotation(rate=-0.5, about='phi')
        #self.begin_ambient_camera_rotation(rate=0.4, about='theta') #double rotation require color gradient 
        #self.wait(2.6)
        self.wait(3.85)  # if rate = -ve
        self.remove(ax)
        self.stop_ambient_camera_rotation(about='phi')
        self.begin_ambient_camera_rotation(rate=5, about='theta')
        self.move_camera(zoom=20, run_time=4)
        self.play(curve6.animate.set_color(BLACK), run_time=1)
        self.remove(curve5)
        self.remove(curve6)
        self.stop_ambient_camera_rotation(about='theta')
        
        text1=Text("Mathematics;", color=BLUE)
        text2=Text("Mysterious yet beautiful", color=YELLOW).next_to(text1, DOWN)
        text3=Text("That's it for now.", font="Chalkboard SE").scale(0.5)
        text4=Text("Definitely a long way to go for me.", font="Chalkboard SE").next_to(text3, DOWN).scale(0.5)

        self.move_camera(phi=0 * DEGREES, theta=-90 *DEGREES, zoom=1.0, run_time=0.5)
        
        self.play(
            Write(text1),
            Write(text2),
        )
        group1 = VGroup(text1, text2)
        self.wait()
        self.play(
            FadeOut(group1)
        )
        self.play(
            Write(text3),
            Write(text4),
        )

        self.wait()
