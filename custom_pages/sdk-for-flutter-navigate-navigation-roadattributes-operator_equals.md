---
title: "operator == method - RoadAttributes class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-roadattributes-operator_equals"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/RoadAttributes-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">operator ==</span> method

</div>

<div class="section multi-line-signature">

<div>

1.  @override

</div>

<span class="returntype">bool</span> <span class="name">operator ==</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>

)

</div>

<div class="section desc markdown">

The equality operator.

The default behavior for all `Object`s is to return true if and only if this object and `other` are the same object.

Override this method to specify a different equality relation on a class. The overriding method must still be an equivalence relation. That is, it must be:

- Total: It must return a boolean for all arguments. It should never throw.

- Reflexive: For all objects `o`, `o == o` must be true.

- Symmetric: For all objects `o1` and `o2`, `o1 == o2` and `o2 == o1` must either both be true, or both be false.

- Transitive: For all objects `o1`, `o2`, and `o3`, if `o1 == o2` and `o2 == o3` are true, then `o1 == o3` must be true.

The method should also be consistent over time, so whether two objects are equal should only change if at least one of the objects was modified.

If a subclass overrides the equality operator, it should override the <a href="sdk-for-flutter-navigate-navigation-roadattributes-hashcode">hashCode</a> method as well to maintain consistency.

</div>

## Implementation

``` dart
@override
bool operator ==(Object other) {
  if (identical(this, other)) return true;
  if (other is! RoadAttributes) return false;
  RoadAttributes _other = other;
  return isDirtRoad == _other.isDirtRoad &&
      isTunnel == _other.isTunnel &&
      isBridge == _other.isBridge &&
      isRamp == _other.isRamp &&
      isControlledAccess == _other.isControlledAccess &&
      isPrivate == _other.isPrivate &&
      isNoThrough == _other.isNoThrough &&
      isTollway == _other.isTollway &&
      isDividedRoad == _other.isDividedRoad &&
      isRightDrivingSide == _other.isRightDrivingSide &&
      isRoundabout == _other.isRoundabout &&
      isBuiltUpArea == _other.isBuiltUpArea;
}
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

