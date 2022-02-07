import 'dart:math';
import 'dart:ui' as ui;

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class AnimText extends StatefulWidget {
  const AnimText({Key? key}) : super(key: key);

  @override
  State<StatefulWidget> createState() => _AnimTextState();
}

class _AnimTextState extends State<AnimText> with SingleTickerProviderStateMixin {
  late AnimationController _ctrl;

  @override
  void initState() {
    _ctrl = AnimationController(vsync: this, duration: const Duration(seconds: 2), animationBehavior: AnimationBehavior.preserve);
    super.initState();
  }

  @override
  void dispose() {
    _ctrl.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: GestureDetector(
          onTap: () => _ctrl.repeat(),
          child: AnimatedBuilder(
            animation: _ctrl,
            builder: (_, __) => Text(
              'Flutter Lab',
              style: _textStyle,
            ),
          ),
        ),
      ),
    );
  }

  TextStyle get _textStyle => TextStyle(
        fontSize: 60,
        foreground: Paint()
          ..style = PaintingStyle.stroke
          ..strokeWidth = 2
          ..shader = ui.Gradient.linear(
              Offset.zero,
              const Offset(100, 0),
              const [
                Color(0xFFF60C0C),
                Color(0xFFF3B913),
                Color(0xFFE7F716),
                Color(0xFF3DF30B),
                Color(0xFF0DF6EF),
                Color(0xFF0829FB),
                Color(0xFFB709F4)
              ],
              const [1.0 / 7, 2.0 / 7, 3.0 / 7, 4.0 / 7, 5.0 / 7, 6.0 / 7, 1.0],
              TileMode.mirror,
              Matrix4.rotationZ(pi / 6).storage)
          ..maskFilter = MaskFilter.blur(BlurStyle.solid, 5 * _ctrl.value),
      );
}
