---
title: "addMapIdleListener method - HereMapControllerCore class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-heremapcontrollercore-addmapidlelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- addMapIdleListener.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/HereMapControllerCore-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">addMapIdleListener</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">addMapIdleListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-addMapIdleListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapidlelistener-class">MapIdleListener</a></span> <span class="parameter-name">listener</span></span>

)

</div>

<div class="section desc markdown">

Adds a listener for receiving idle state notifications and notifies it of the current state.

The first notification received is always the state at the time of registration.

The new listener is appended to the set of `HereMap` idle listeners as a strong reference. The caller is responsible for releasing the strong reference by calling <a href="sdk-for-flutter-explore-mapview-heremapcontrollercore-removemapidlelistener">HereMapControllerCore.removeMapIdleListener</a>.

The idle state notifications can occur on an arbitrary thread.

- `listener` The listener

</div>

## Implementation

``` dart
void addMapIdleListener(MapIdleListener listener);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
