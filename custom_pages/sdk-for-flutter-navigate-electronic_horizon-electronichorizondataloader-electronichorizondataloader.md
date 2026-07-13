---
title: "ElectronicHorizonDataLoader constructor - ElectronicHorizonDataLoader - electronic_horizon library - Dart API"
slug: "sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloader-electronichorizondataloader"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ElectronicHorizonDataLoader.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="electronic_horizon/ElectronicHorizonDataLoader-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">ElectronicHorizonDataLoader</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">ElectronicHorizonDataLoader</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-class">SegmentDataLoaderOptions</a></span> <span class="parameter-name">options</span>, </span>
3.  <span id="sdk-for-flutter-navigate-param-segmentDataCacheSize" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">segmentDataCacheSize</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance of <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloader-class">ElectronicHorizonDataLoader</a>.

The constructor accepts options to configure the data loader. For more information, see <a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-class">SegmentDataLoaderOptions</a>. The cache size limits the number of segments that the loader can keep in memory at the same time.

- `sdkEngine` The <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a> instance that provides shared services, such as networking and map data.

- `options` The <a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-class">SegmentDataLoaderOptions</a> instance that configures how segment data is requested.

- `segmentDataCacheSize` The maximum number of segments that the loader can cache.

Throws <a href="sdk-for-flutter-navigate-core-errors-instantiationexception-class">InstantiationException</a>. <a href="sdk-for-flutter-navigate-core-errors-instantiationexception-class">InstantiationException</a> If the data loader cannot be created.

</div>

## Implementation

``` dart
factory ElectronicHorizonDataLoader(SDKNativeEngine sdkEngine, SegmentDataLoaderOptions options, int segmentDataCacheSize) => $prototype.make(sdkEngine, options, segmentDataCacheSize);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
