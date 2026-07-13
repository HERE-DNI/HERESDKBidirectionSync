---
title: "safetyCameraWarningListener property - NavigatorInterface class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-safetycamerawarninglistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/NavigatorInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">safetyCameraWarningListener</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class">SafetyCameraWarningListener</a>?</span> <span class="name">safetyCameraWarningListener</span>

</div>

<div class="section desc markdown">

Object to receive safety camera warner notifications. If a listener is present, notifications about safety speed cameras will be also sent via <a href="sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class">SafetyCameraWarningListener</a>. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive safety camera warning notifications.

</div>

## Implementation

``` dart
SafetyCameraWarningListener? get safetyCameraWarningListener;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">safetyCameraWarningListener=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-safetyCameraWarningListener-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class">SafetyCameraWarningListener</a>?</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Object to receive safety camera warner notifications. If a listener is present, notifications about safety speed cameras will be also sent via <a href="sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class">SafetyCameraWarningListener</a>. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Sets the listener to receive safety camera warning notifications.

</div>

## Implementation

``` dart
set safetyCameraWarningListener(SafetyCameraWarningListener? value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

