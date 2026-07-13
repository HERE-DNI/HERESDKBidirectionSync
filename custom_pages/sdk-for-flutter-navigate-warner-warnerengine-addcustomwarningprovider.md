---
title: "addCustomWarningProvider method - WarnerEngine class - warner library - Dart API"
slug: "sdk-for-flutter-navigate-warner-warnerengine-addcustomwarningprovider"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="warner/WarnerEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">addCustomWarningProvider</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">addCustomWarningProvider</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-addCustomWarningProvider-param-customWarningProvider" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-warner-customwarningprovider-class">CustomWarningProvider</a></span> <span class="parameter-name">customWarningProvider</span>, </span>
2.  <span id="sdk-for-flutter-navigate-addCustomWarningProvider-param-segmentDataLoaderOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-class">SegmentDataLoaderOptions</a></span> <span class="parameter-name">segmentDataLoaderOptions</span></span>

)

</div>

<div class="section desc markdown">

Registers a custom warning provider.

The registered provider participates in warning evaluation and is invoked to generate custom warnings based on the current vehicle position.

- `customWarningProvider` A provider responsible for generating custom warnings.

- `segmentDataLoaderOptions` Specifies which data should be loaded by the `SegmentDataLoader`.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
void addCustomWarningProvider(CustomWarningProvider customWarningProvider, SegmentDataLoaderOptions segmentDataLoaderOptions);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

