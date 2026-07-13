---
title: "onRoadAttributesUpdated method - RoadAttributesListener class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-roadattributeslistener-onroadattributesupdated"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/RoadAttributesListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">onRoadAttributesUpdated</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">onRoadAttributesUpdated</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-onRoadAttributesUpdated-param-roadAttributes" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-roadattributes-class">RoadAttributes</a></span> <span class="parameter-name">roadAttributes</span></span>

)

</div>

<div class="section desc markdown">

Called whenever any attribute of the current road changes.

It's guaranteed to be called at least once for the first road the user is traveling on.

- `roadAttributes` The object that contains attributes of the current road.

</div>

## Implementation

``` dart
void onRoadAttributesUpdated(RoadAttributes roadAttributes);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

