import 'package:flutter/material.dart';

class Circle {
  final Color color;
  final double radius;
  final Offset center;

  Circle({required this.color, required this.radius, required this.center});
}

class CircleTween extends Tween<Circle> {
  CircleTween({required Circle begin, required Circle end}) : super(begin: begin, end: end);

  @override
  Circle lerp(double t) {
    return Circle(
        color: Color.lerp(begin!.color, end!.color, t)!,
        radius: (begin!.radius + (end!.radius - begin!.radius) * t),
        center: Offset.lerp(begin!.center, end!.center, t)!);
  }
}

class CircleWidget extends StatelessWidget {
  final Circle circle;

  const CircleWidget(this.circle, {Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      transform: Matrix4.translationValues(circle.center.dx, circle.center.dy, 0),
      width: circle.radius * 2,
      height: circle.radius * 2,
      decoration: BoxDecoration(color: circle.color, shape: BoxShape.circle),
    );
  }
}

class CirclePage extends StatefulWidget {
  const CirclePage({Key? key}) : super(key: key);

  @override
  State<StatefulWidget> createState() => _CirclePageState();
}

class _CirclePageState extends State<CirclePage> with SingleTickerProviderStateMixin {
  late AnimationController _ctrl;
  late Animation<Circle> _animation;

  @override
  void initState() {
    _ctrl = AnimationController(vsync: this, duration: const Duration(seconds: 2));
    _animation = CircleTween(
            begin: Circle(center: Offset.zero, radius: 25, color: Colors.blue),
            end: Circle(center: const Offset(100, 0), radius: 100, color: Colors.red))
        .animate(_ctrl);
    _ctrl.forward();
    super.initState();
  }

  @override
  void dispose() {
    _ctrl.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Center(child: AnimatedBuilder(animation: _animation, builder: (_, __) => CircleWidget(_animation.value)));
  }
}
