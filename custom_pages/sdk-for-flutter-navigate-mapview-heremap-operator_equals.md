---
title: "operator == method - HereMap class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-heremap-operator_equals"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/HereMap-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">operator ==</span> method

</div>

<div class="section multi-line-signature">

<div>

1.  @override
2.  @<a href="https://pub.dev/documentation/meta/1.17.0/meta/nonVirtual-constant.html">nonVirtual</a>

</div>

<span class="returntype">bool</span> <span class="name">operator ==</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>

)

<div class="features">

<span class="feature">inherited</span>

</div>

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

If a subclass overrides the equality operator, it should override the <a href="sdk-for-flutter-navigate-mapview-heremap-hashcode">hashCode</a> method as well to maintain consistency.

</div>

## Implementation

``` dart
@override
@nonVirtual
bool operator ==(Object other) => super == other;
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

