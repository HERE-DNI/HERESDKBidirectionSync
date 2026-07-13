---
title: "onComplete method - PrefetchStatusListener class - prefetcher library - Dart API"
slug: "sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-oncomplete"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onComplete.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="prefetcher/PrefetchStatusListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">onComplete</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">onComplete</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-onComplete-param-error" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</span> <span class="parameter-name">error</span></span>

)

</div>

<div class="section desc markdown">

Called after the geo-corridor data downloads has been completed either with success or with error.

Invoked on the main thread.

- `error` Represents an error in case of a failure. If an error occurs, to resume operation, please download geo-corridor again. It is `null` for an operation that succeeds.

</div>

## Implementation

``` dart
void onComplete(MapLoaderError? error);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
