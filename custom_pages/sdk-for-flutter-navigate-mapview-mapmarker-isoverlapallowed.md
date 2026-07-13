---
title: "isOverlapAllowed property - MapMarker class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapmarker-isoverlapallowed"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMarker-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">isOverlapAllowed</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">bool</span> <span class="name">isOverlapAllowed</span>

</div>

<div class="section desc markdown">

Determines whether or not the marker can overlap other markers. Returns `true` if the marker allows overlap with other markers, `false` otherwise. Defaults to `true`.

</div>

## Implementation

``` dart
bool get isOverlapAllowed;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">isOverlapAllowed=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-isOverlapAllowed-param-value" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Determines whether or not the marker can overlap other markers. Sets whether the marker is allowed to overlap with other markers.

If `false`, it will disappear the moment it overlaps another marker that has a higher visibility priority. A marker that allows overlap will always be drawn. Among markers that don't allow overlap, the one with the highest draw order has priority. Marker that is hidden due to overlapping with other markers is not pickable.

</div>

## Implementation

``` dart
set isOverlapAllowed(bool value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

