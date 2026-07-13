---
title: "createState method - HereMap class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-heremap-createstate"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/HereMap-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">createState</span> method

</div>

<div class="section multi-line-signature">

<div>

1.  @override

</div>

<span class="returntype">State<span class="signature">\<<wbr></wbr><span class="type-parameter">StatefulWidget</span>\></span></span> <span class="name">createState</span>(<wbr></wbr>)

</div>

<div class="section desc markdown">

Creates the mutable state for this widget at a given location in the tree.

Subclasses should override this method to return a newly created instance of their associated `State` subclass:

``` dart
@override
State<SomeWidget> createState() => _SomeWidgetState();
```

</pre>

The framework can call this method multiple times over the lifetime of a `StatefulWidget`. For example, if the widget is inserted into the tree in multiple locations, the framework will create a separate `State` object for each location. Similarly, if the widget is removed from the tree and later inserted into the tree again, the framework will call <a href="sdk-for-flutter-navigate-mapview-heremap-createstate">createState</a> again to create a fresh `State` object, simplifying the lifecycle of `State` objects.

</div>

## Implementation

``` dart
@override
State<StatefulWidget> createState() => _HereMapState();
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

