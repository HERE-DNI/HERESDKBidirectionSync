---
title: "isCurrentPositionIncluded property - AreaCameraBehavior class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-areacamerabehavior-iscurrentpositionincluded"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- isCurrentPositionIncluded.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/AreaCameraBehavior-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">isCurrentPositionIncluded</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">bool</span> <span class="name">isCurrentPositionIncluded</span>

</div>

<div class="section desc markdown">

Include current position in camera view. Decides if the current position should be added to the set of visible points. Note that if the current position is in the vicinity of any of the visible points, setting this to `false` will not explicitly exclude the current position from the camera view. However if displaying an area potentially away from the current position, this does need to be explicitly set to `false` or it will try to include the current position. Defaults to false. Gets whether to include the current position.

</div>

## Implementation

``` dart
bool get isCurrentPositionIncluded;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">isCurrentPositionIncluded=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-isCurrentPositionIncluded-param-value" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Include current position in camera view. Decides if the current position should be added to the set of visible points. Note that if the current position is in the vicinity of any of the visible points, setting this to `false` will not explicitly exclude the current position from the camera view. However if displaying an area potentially away from the current position, this does need to be explicitly set to `false` or it will try to include the current position. Defaults to false. Sets whether to include the current position.

</div>

## Implementation

``` dart
set isCurrentPositionIncluded(bool value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
