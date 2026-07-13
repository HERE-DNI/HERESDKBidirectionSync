---
title: "getSegment method - ElectronicHorizonDataLoader class - electronic_horizon library - Dart API"
slug: "sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloader-getsegment"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getSegment.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="electronic_horizon/ElectronicHorizonDataLoader-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getSegment</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloaderresult-class">ElectronicHorizonDataLoaderResult</a></span> <span class="name">getSegment</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-getSegment-param-segmentId" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapdata-directedocmsegmentid-class">DirectedOCMSegmentId</a></span> <span class="parameter-name">segmentId</span></span>

)

</div>

<div class="section desc markdown">

Returns loaded data for the given segment identifier.

The result contains either the loaded data or an error code.

- `segmentId` The segment identifier for which to return the loaded data from the cache.

Returns <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloaderresult-class">ElectronicHorizonDataLoaderResult</a>. The result object that contains either the loaded segment data or an error code.

</div>

## Implementation

``` dart
ElectronicHorizonDataLoaderResult getSegment(DirectedOCMSegmentId segmentId);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
