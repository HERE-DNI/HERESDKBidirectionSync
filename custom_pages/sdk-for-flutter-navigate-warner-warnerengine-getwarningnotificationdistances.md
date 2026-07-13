---
title: "getWarningNotificationDistances method - WarnerEngine class - warner library - Dart API"
slug: "sdk-for-flutter-navigate-warner-warnerengine-getwarningnotificationdistances"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="warner/WarnerEngine-class-sidebar.html" data-below-sidebar="">

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

**Note**: <a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType.custom</a> is not a valid value for this method. Use <a href="sdk-for-flutter-navigate-warner-warnerengine-getcustomwarningnotificationdistances">WarnerEngine.getCustomWarningNotificationDistances</a> to retrieve distances for a specific custom warning type.

- `warningType` The warning type for which the notification distances will be returned. Must not be <a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType.custom</a>.

Returns <a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a>. The warning notification distances for the given `WarnerEngine.getWarningNotificationDistances.warningType`. If `WarnerEngine.getWarningNotificationDistances.warningType` is <a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType.custom</a>, a default <a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a> value is returned.

</div>

## Implementation

``` dart
WarningNotificationDistances getWarningNotificationDistances(WarningType warningType);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

