---
title: "key property - HereMap class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-heremap-key"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/HereMap-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">key</span> property

</div>

<div class="section multi-line-signature">

Key? <span class="name">key</span>

<div class="features">

<span class="feature">final</span><span class="feature">inherited</span>

</div>

</div>

<div class="section desc markdown">

Controls how one widget replaces another widget in the tree.

If the `runtimeType` and `key` properties of the two widgets are `operator==`, respectively, then the new widget replaces the old widget by updating the underlying element (i.e., by calling `Element.update` with the new widget). Otherwise, the old element is removed from the tree, the new widget is inflated into an element, and the new element is inserted into the tree.

In addition, using a `GlobalKey` as the widget's `key` allows the element to be moved around the tree (changing parent) without losing state. When a new widget is found (its key and type do not match a previous widget in the same location), but there was a widget with that same global key elsewhere in the tree in the previous frame, then that widget's element is moved to the new location.

Generally, a widget that is the only child of another widget does not need an explicit key.

See also:

- The discussions at `Key` and `GlobalKey`.

</div>

## Implementation

``` dart
final Key? key;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

