---
title: "IconProviderCallback typedef - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-iconprovidercallback"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">IconProviderCallback</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">IconProviderCallback</span> = <span class="returntype">void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-imageInfo" class="parameter"><span class="type-annotation">ImageInfo?</span> <span class="parameter-name">imageInfo</span>, </span><span id="sdk-for-flutter-navigate-param-iconDescription" class="parameter"><span class="type-annotation">String?</span> <span class="parameter-name">iconDescription</span>, </span><span id="sdk-for-flutter-navigate-param-error" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-iconprovidererror">IconProviderError</a>?</span> <span class="parameter-name">error</span></span>)</span></span>

</div>

<div class="section desc markdown">

A callback of this type is invoked when an icon is received from the <a href="sdk-for-flutter-navigate-mapview-iconprovider-class">IconProvider</a> in the `ImageInfo` format. The callback provides information about the loaded icon, or an <a href="sdk-for-flutter-navigate-mapview-iconprovidererror">IconProviderError</a> if one occurred.

`imageInfo` The created `ImageInfo` containing the icon, or `null` if an error occurred.

`iconDescription` An English description of the created icon. It will be `null` if an error occurred.

`error` The error that occurred, or `null` if the icon is loaded successfully.

</div>

## Implementation

``` dart
typedef IconProviderCallback = void Function(
    ImageInfo? imageInfo, String? iconDescription, IconProviderError? error);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

