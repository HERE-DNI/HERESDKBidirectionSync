---
title: "pause method - HereMapController class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-heremapcontroller-pause"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- pause.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/HereMapController-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">pause</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">pause</span>(<wbr></wbr>)

</div>

<div class="section desc markdown">

Pauses the map widget.

A paused map widget stops rendering updates until it gets resumed. It is recommended to not schedule any map updates while in the paused state as they are cached in-memory and will pile-up until the map widget gets resumed.

By default, the map widget gets automatically paused and resumed based on platform specific events (e.g. client application going into background/foreground). Once this method gets called, the automatic behavior gets disabled.

</div>

## Implementation

``` dart
void pause();
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
