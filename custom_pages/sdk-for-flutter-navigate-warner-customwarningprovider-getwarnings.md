---
title: "getWarnings method - CustomWarningProvider class - warner library - Dart API"
slug: "sdk-for-flutter-navigate-warner-customwarningprovider-getwarnings"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getWarnings.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="warner/CustomWarningProvider-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getWarnings</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-warner-customwarning-class">CustomWarning</a></span>\></span></span> <span class="name">getWarnings</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-getWarnings-param-currentSegment" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapdata-segmentdata-class">SegmentData</a></span> <span class="parameter-name">currentSegment</span>, </span>
2.  <span id="sdk-for-flutter-navigate-getWarnings-param-previousSegment" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapdata-segmentdata-class">SegmentData</a>?</span> <span class="parameter-name">previousSegment</span></span>

)

</div>

<div class="section desc markdown">

Returns a list of custom warnings for the given vehicle position.

This method evaluates the custom warning provider using the current vehicle position on the electronic horizon and returns the resulting custom warnings along with corresponding payload.

- `currentSegment` Segment data representing the vehicle’s current position on the electronic horizon.

- `previousSegment` Segment data representing the vehicle’s previous position on the electronic horizon. This parameter may be null if no previous position information is available.

Returns `List<CustomWarning>`. A list of `CustomWarning` instances representing all applicable custom warnings. The list may be empty if no warnings apply.

</div>

## Implementation

``` dart
List<CustomWarning> getWarnings(SegmentData currentSegment, SegmentData? previousSegment);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
