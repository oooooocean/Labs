import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class BurstMenu extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => _BurstMenuState();
}

class _BurstMenuState extends State<BurstMenu> with SingleTickerProviderStateMixin {
  final List<Widget> _menus = [Colors.red, Colors.blue, Colors.orange, Colors.greenAccent]
      .map((e) => Container(width: 40, height: 40, decoration: BoxDecoration(color: e, shape: BoxShape.circle)))
      .toList();
  final Widget _center =
      SizedBox(width: 60, height: 60, child: Image.network('http://img.duoziwang.com/2021/01/1-21041H243490-L.jpg'));

  @override
  Widget build(BuildContext context) {
    return Center(
      child: SizedBox(
        width: 200,
        height: 200,
        child: Flow(
          delegate: _CircleFlowDelegate(),
          children: [..._menus, _center],
        ),
      ),
    );
  }
}

class _CircleFlowDelegate extends FlowDelegate {
  @override
  void paintChildren(FlowPaintingContext context) {
    // TODO: implement paintChildren
  }

  @override
  bool shouldRepaint(covariant FlowDelegate oldDelegate) => false;
}
