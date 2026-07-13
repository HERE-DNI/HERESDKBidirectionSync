---
title: "unpinWidget method - HereMapController class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-heremapcontroller-unpinwidget"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/HereMapController-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">unpinWidget</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">unpinWidget</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-unpinWidget-param-widget" class="parameter"><span class="type-annotation">Widget</span> <span class="parameter-name">widget</span></span>

)

</div>

<div class="section desc markdown">

Removes a <a href="sdk-for-flutter-navigate-mapview-widgetpin-class">WidgetPin</a> from the MapView by specifying the corresponding `Widget`. Trying to unpin a widget that was not pinned or has been unpinned before has no effect. All pinned widgets equal to `widget` will be removed.

`widget` corresponding to the <a href="sdk-for-flutter-navigate-mapview-widgetpin-class">WidgetPin</a> to remove.

</div>

## Implementation

``` dart
void unpinWidget(Widget widget);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

