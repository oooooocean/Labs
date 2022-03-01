import 'dart:math';
import 'dart:ui' as ui;

import 'package:flutter/cupertino.dart';

class CircleHalo extends StatefulWidget {
  const CircleHalo({Key? key}) : super(key: key);

  @override
  State<StatefulWidget> createState() => _CircleHaloState();
}

class _CircleHaloState extends State<CircleHalo> with SingleTickerProviderStateMixin {
  late AnimationController _ctrl;

  @override
  void initState() {
    _ctrl = AnimationController(vsync: this, duration: const Duration(seconds: 2));
    _ctrl.repeat();
    super.initState();
  }

  @override
  void dispose() {
    _ctrl.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Center(child: CustomPaint(size: const Size(200, 200), painter: _CircleHaloPainter(_ctrl)));
  }
}

class _CircleHaloPainter extends CustomPainter {
  Animation<double> animation;

  _CircleHaloPainter(this.animation) : super(repaint: animation);

  final _paint = Paint()
    ..style = PaintingStyle.stroke
    ..strokeWidth = 1;

  final _breathTween = TweenSequence<double>([
    TweenSequenceItem(tween: Tween(begin: 0, end: 4), weight: 1),
    TweenSequenceItem(tween: Tween(begin: 4, end: 0), weight: 1)
  ]).chain(CurveTween(curve: Curves.decelerate));

  @override
  void paint(Canvas canvas, Size size) {
    canvas.translate(size.width / 2, size.height / 2);
    // 绘制圆
    canvas.drawArc(
        Rect.fromCenter(center: Offset.zero, width: 100, height: 100),
        0,
        2 * pi,
        false,
        _paint
          ..maskFilter = _blurFilter
          ..shader = _shader);

    // 绘制月牙
    canvas.save();
    canvas.rotate(animation.value * 2 * pi);
    canvas.drawPath(
        _circlePath,
        Paint()
          ..maskFilter = _blurFilter
          ..style = PaintingStyle.fill
          ..color = const Color(0xff00abf2));
    canvas.restore();
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;

  ui.Gradient get _shader {
    var colors = [
      const Color(0xFFF60C0C),
      const Color(0xFFF3B913),
      const Color(0xFFE7F716),
      const Color(0xFF3DF30B),
      const Color(0xFF0DF6EF),
      const Color(0xFF0829FB),
      const Color(0xFFB709F4),
    ];

    colors.addAll(colors.reversed.toList());

    final pos = List.generate(colors.length, (index) => index / colors.length);

    return ui.Gradient.sweep(Offset.zero, colors, pos, TileMode.clamp, 0, 2 * pi);
  }

  Path get _circlePath {
    final path1 = Path()..addOval(Rect.fromCenter(center: Offset.zero, width: 100, height: 100));
    final path2 = Path()..addOval(Rect.fromCenter(center: const Offset(-1, 0), width: 100, height: 100));
    return Path.combine(PathOperation.difference, path1, path2);
  }

  MaskFilter get _blurFilter => MaskFilter.blur(BlurStyle.solid, _breathTween.evaluate(animation));
}
