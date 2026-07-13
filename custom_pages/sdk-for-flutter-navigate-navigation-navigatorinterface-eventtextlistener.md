---
title: "eventTextListener property - NavigatorInterface class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-eventtextlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- eventTextListener.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/NavigatorInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">eventTextListener</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-navigation-eventtextlistener-class">EventTextListener</a>?</span> <span class="name">eventTextListener</span>

</div>

<div class="section desc markdown">

Object to receive text notifications when they are available. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. **Note:** In order to receive the text notification emitted for the traffic merge warner, when `TrafficMergeWarningOptions.enable_text_notification` has been enabled, the `sdk.navigation.EventTextListener` must be enabled as well. Gets the listener that notifies when a text notification is available.

</div>

## Implementation

``` dart
EventTextListener? get eventTextListener;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">eventTextListener=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-eventTextListener-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-eventtextlistener-class">EventTextListener</a>?</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Object to receive text notifications when they are available. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. **Note:** In order to receive the text notification emitted for the traffic merge warner, when `TrafficMergeWarningOptions.enable_text_notification` has been enabled, the `sdk.navigation.EventTextListener` must be enabled as well. Sets the listener that notifies when a text notification is available.

</div>

## Implementation

``` dart
set eventTextListener(EventTextListener? value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
