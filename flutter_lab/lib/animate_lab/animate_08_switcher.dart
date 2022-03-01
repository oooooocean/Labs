import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class AnimSwitcher extends StatefulWidget {
  const AnimSwitcher({Key? key}) : super(key: key);

  @override
  State<StatefulWidget> createState() => _AnimSwitcherState();
}

class _AnimSwitcherState extends State<AnimSwitcher> {
  final _valueNotifier = ValueNotifier(0);

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Wrap(spacing: 15, crossAxisAlignment: WrapCrossAlignment.center, children: [
        IconButton(onPressed: () => _valueNotifier.value -= 1, icon: const Icon(Icons.remove_circle_outline)),
        ValueListenableBuilder<int>(
          valueListenable: _valueNotifier,
          builder: (_, value, __) => AnimatedSwitcher(
            duration: const Duration(milliseconds: 800),
            switchInCurve: Curves.fastOutSlowIn,
            transitionBuilder: (child, animation) => ScaleTransition(
              scale: Tween(begin: 0.0, end: 1.0).animate(animation),
              child: RotationTransition(turns: animation, child: child),
            ),
            child: Text(
              value.toString(),
              key: ValueKey(value),
              style: const TextStyle(fontSize: 40, color: Colors.redAccent),
            ),
          ),
        ),
        IconButton(onPressed: () => _valueNotifier.value += 1, icon: const Icon(Icons.add_circle_outline)),
      ]),
    );
  }
}
