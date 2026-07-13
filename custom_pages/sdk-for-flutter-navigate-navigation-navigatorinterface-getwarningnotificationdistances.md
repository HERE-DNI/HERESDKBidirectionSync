---
title: "getWarningNotificationDistances method - NavigatorInterface class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-getwarningnotificationdistances"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/NavigatorInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getWarningNotificationDistances</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a></span> <span class="name">getWarningNotificationDistances</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-getWarningNotificationDistances-param-warningType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a></span> <span class="parameter-name">warningType</span></span>

)

</div>

<div class="section desc markdown">

Returns the warning notification distances for the requested warning type.

The return value can be used as the base for configuring warning notification distances. Configure the relevant attributes of this object according to your preferences, and then set it by calling `setWarningNotificationDistances` function with the same warning type and the modified warning notification distances object.

- `warningType` The warning type for which the notification distances will be returned.

Returns <a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a>. The notification distances for the given warning type.

</div>

## Implementation

``` dart
WarningNotificationDistances getWarningNotificationDistances(WarningType warningType);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

