import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class CircleShineImage extends StatefulWidget {
  final double blur;
  final Color color;
  final Duration duration;
  final Curve curve;
  final ImageProvider image;
  final double radius;

  const CircleShineImage(
      {Key? key,
      this.blur = 20,
      this.color = Colors.blue,
      this.duration = const Duration(seconds: 2),
      this.curve = Curves.ease,
      this.radius = 50,
      required this.image})
      : super(key: key);

  @override
  State<StatefulWidget> createState() => _CircleShineImageState();
}

class _CircleShineImageState extends State<CircleShineImage> with SingleTickerProviderStateMixin {
  late AnimationController _ctrl;
  late Animation<double> _animation;

  @override
  void initState() {
    _ctrl = AnimationController(vsync: this, duration: widget.duration);
    _animation = Tween<double>(begin: 0, end: widget.blur).chain(CurveTween(curve: widget.curve)).animate(_ctrl);
    _ctrl.repeat(reverse: true);
    super.initState();
  }

  @override
  void dispose() {
    _ctrl.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Center(
      child: AnimatedBuilder(
        animation: _animation,
        builder: (_, __) => Container(
          height: widget.radius * 2,
          width: widget.radius * 2,
          decoration: BoxDecoration(
              image: DecorationImage(image: widget.image, fit: BoxFit.cover),
              shape: BoxShape.circle,
              boxShadow: [BoxShadow(color: widget.color, blurRadius: _animation.value)]),
        ),
      ),
    );
  }
}
