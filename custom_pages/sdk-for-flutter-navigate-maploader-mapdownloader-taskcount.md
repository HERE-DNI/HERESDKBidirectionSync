---
title: "taskCount property - MapDownloader class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-taskcount"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- taskCount.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/MapDownloader-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">taskCount</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">int</span> <span class="name">taskCount</span>

</div>

<div class="section desc markdown">

The number of concurrent tasks for downloading a map. A valid task count is between 1 to 64. When the value set is outside the valid range, then it is clamped to a valid range:

- when passed in value is 0 or less, then task count is set to 1;
- when passed in value is 65 or more, then task count is set to 64. Gets the number of concurrent tasks for downloading a map.

</div>

## Implementation

``` dart
int get taskCount;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">taskCount=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-taskCount-param-value" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

The number of concurrent tasks for downloading a map. A valid task count is between 1 to 64. When the value set is outside the valid range, then it is clamped to a valid range:

- when passed in value is 0 or less, then task count is set to 1;
- when passed in value is 65 or more, then task count is set to 64. Sets the number of concurrent tasks for downloading a map.

</div>

## Implementation

``` dart
set taskCount(int value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
