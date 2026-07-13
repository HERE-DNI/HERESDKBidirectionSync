---
title: "EventTextListener constructor - EventTextListener - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-eventtextlistener-eventtextlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EventTextListener.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/EventTextListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">EventTextListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">EventTextListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onEventTextUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onEventTextUpdatedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-eventtext-class">EventText</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive notifications when text notifications are available from <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>.

Multiple notifications can be given for the same maneuver at different distances.

</div>

## Implementation

``` dart
factory EventTextListener(
  void Function(EventText) onEventTextUpdatedLambda,

) => EventTextListener$Lambdas(
  onEventTextUpdatedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
