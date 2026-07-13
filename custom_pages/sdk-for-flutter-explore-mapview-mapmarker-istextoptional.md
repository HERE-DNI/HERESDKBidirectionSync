---
title: "isTextOptional property - MapMarker class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapmarker-istextoptional"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMarker-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">isTextOptional</span> property

</div>

<div id="sdk-for-flutter-explore-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">bool</span> <span class="name">isTextOptional</span>

</div>

<div class="section desc markdown">

Determines if the marker can be displayed with icon and without text. Returns `true` if the marker allows text to be hidden, `false` otherwise. Defaults to `false`.

</div>

## Implementation

``` dart
bool get isTextOptional;
```

</div>

<div id="sdk-for-flutter-explore-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">isTextOptional=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-isTextOptional-param-value" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Determines if the marker can be displayed with icon and without text. Sets whether the marker is allowed to appear without text.

Controls whenever `MapMarker` can be shown as icon only when <a href="sdk-for-flutter-explore-mapview-mapmarker-isoverlapallowed">MapMarker.isOverlapAllowed</a> is `false`, has no effect otherwise. If `false` then the `MapMarker` will not appear when icon or text are blocked by other labels. If `true`, icon will appear even if the text part is blocked by other labels.

</div>

## Implementation

``` dart
set isTextOptional(bool value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

