---
title: "SDKCacheCallback typedef - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-sdkcachecallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SDKCacheCallback.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/maploader-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">SDKCacheCallback</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">SDKCacheCallback</span> = <span class="returntype">void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-maploaderError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</span> <span class="parameter-name">maploaderError</span></span>)</span></span>

</div>

<div class="section desc markdown">

A method which is called on the main thread when <a href="sdk-for-flutter-navigate-maploader-sdkcache-clearappcache">SDKCache.clearAppCache</a> has been completed.

- `maploaderError` Represents an error in case of a failure. It is `null` for an operation that succeeds. Please note, in case of failure, only <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError.internalError</a> error returned for now.

</div>

## Implementation

``` dart
typedef SDKCacheCallback = void Function(MapLoaderError? maploaderError);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
