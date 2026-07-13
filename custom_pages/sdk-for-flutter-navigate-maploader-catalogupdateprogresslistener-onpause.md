---
title: "onPause method - CatalogUpdateProgressListener class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-catalogupdateprogresslistener-onpause"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onPause.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/CatalogUpdateProgressListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">onPause</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">onPause</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-onPause-param-error" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</span> <span class="parameter-name">error</span></span>

)

</div>

<div class="section desc markdown">

Called when update is paused.

Invoked on the main thread.

- `error` Populated when a retryable error is the reason for a pause. A retryable error can happen, when, for example, the HERE SDK tries too often to resume a download that was paused due to a lost connection. In general, the HERE SDK will try a few times, before the update is paused. This error value gives a hint on the reason for the necessary retry operation. A paused download can be resumed by the user at a later time. It is 'null' when `CatalogUpdateTask.pauseWithCompaction` was called by the user.

</div>

## Implementation

``` dart
void onPause(MapLoaderError? error);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
