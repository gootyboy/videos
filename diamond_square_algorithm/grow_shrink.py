from manim import *

class GrowShrinkAnimation(Animation):
    def __init__(self, mobject, **kwargs):
        super().__init__(mobject, **kwargs)
        self.starting_mobject = mobject.copy()
        self.fill_color = self.starting_mobject.get_fill_color()
        self.fill_opacity = self.starting_mobject.get_fill_opacity()

    def interpolate_mobject(self, alpha):
        self.mobject.match_points(self.starting_mobject)
        self.mobject.match_style(self.starting_mobject)
        
        if alpha <= 0.5:
            a = alpha * 2
            self.mobject.scale(1.0 + (0.25 * a))
            self.mobject.set_fill(
                color=interpolate_color(self.fill_color, PURE_YELLOW, a),
                opacity=interpolate(self.fill_opacity, 1.0, a)
            )
        else:
            a = (alpha - 0.5) * 2
            peak_scale = 1.25
            target_scale = 1.0 / 1.25
            
            self.mobject.scale(peak_scale * interpolate(1.0, target_scale, a))
            self.mobject.set_fill(
                color=interpolate_color(PURE_YELLOW, self.fill_color, a),
                opacity=interpolate(1.0, self.fill_opacity, a)
            )

class GrowShrink(AnimationGroup):
    def __init__(self, *mobjects, **kwargs):
        kwargs.setdefault("run_time", 1.0)
        animations = []

        for mobj in mobjects:
            animations.append(GrowShrinkAnimation(mobj, **kwargs))
            
        super().__init__(*animations, lag_ratio=0)
