---
title: "onEventTextUpdated method - EventTextListener class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-eventtextlistener-oneventtextupdated"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/EventTextListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">onEventTextUpdated</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">onEventTextUpdated</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-onEventTextUpdated-param-eventText" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-eventtext-class">EventText</a></span> <span class="parameter-name">eventText</span></span>

)

</div>

<div class="section desc markdown">

Called whenever there is a new text notification for a maneuver (multiple notifications can be given for the same maneuver at different distances (for example: "After 500 meters turn right." or "Now turn right.") and in that case, this method will be called once for each distance.

- `eventText` Data related to next text announcement.

</div>

## Implementation

``` dart
void onEventTextUpdated(EventText eventText);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

