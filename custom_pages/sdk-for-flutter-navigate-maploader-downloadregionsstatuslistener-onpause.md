---
title: "onPause method - DownloadRegionsStatusListener class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-onpause"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/DownloadRegionsStatusListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">onPause</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">onPause</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-onPause-param-error" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</span> <span class="parameter-name">error</span></span>

)

</div>

<div class="section desc markdown">

Called when download is paused.

- `error` Populated when retryable error is a reason of a pause. It is 'null' when pause is called by the user.

</div>

## Implementation

``` dart
void onPause(MapLoaderError? error);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

